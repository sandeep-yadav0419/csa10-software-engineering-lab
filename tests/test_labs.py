from pathlib import Path
import importlib.util
import os
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import MagicMock
import pymysql
from werkzeug.security import generate_password_hash

ROOT=Path(__file__).resolve().parents[1]
IMPORT_TEMP=tempfile.TemporaryDirectory()
os.environ['TODO_DB']=str(Path(IMPORT_TEMP.name)/'import.db')

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

simple=[load(f'lab{n}',f'experiments/{path}/app.py') for n,path in [
    (12,'12-flask-kubernetes'),(13,'13-jenkins-pipeline'),
    (14,'14-github-actions-docker'),(19,'19-flask-cicd')]]
todo=load('todo_lab','experiments/16-flask-todo/app.py')
backend=load('backend_lab','experiments/18-multi-container-kubernetes/backend/app.py')
login=load('login_lab','experiments/24-feature-login/login.py')
feature=load('feature_lab','experiments/25-fork-feature/feature.py')

class FlaskEndpointTests(unittest.TestCase):
    def test_home_messages(self):
        expected=['Hello from Flask API!','Hello from CI/CD Docker Pipeline!',
                  'CI/CD Pipeline Updated Successfully!','CI/CD Deployment Successful!']
        for module,text in zip(simple,expected):
            with self.subTest(module=module.__name__):
                response=module.app.test_client().get('/')
                self.assertEqual(response.status_code,200)
                self.assertEqual(response.text,text)

    def test_about_and_health(self):
        for module in simple:
            with self.subTest(module=module.__name__):
                c=module.app.test_client()
                self.assertEqual(c.get('/about').text,'This is a simple Flask API')
                self.assertEqual(c.get('/health').json['status'],'ok')
                self.assertEqual(c.get('/missing').status_code,404)
                self.assertEqual(c.post('/').status_code,405)

class TodoTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.database=str(Path(self.tmp.name)/'todo.db')
        self.app=todo.create_app({'TESTING':True,'DATABASE':self.database})
        self.client=self.app.test_client()
    def tearDown(self):self.tmp.cleanup()
    def test_add_redirect_and_reload(self):
        r=self.client.post('/',data={'task':'  Read lab  '})
        self.assertEqual(r.status_code,303)
        restarted=todo.create_app({'TESTING':True,'DATABASE':self.database})
        self.assertIn('Read lab',restarted.test_client().get('/').text)
    def test_reject_blank_and_long_tasks(self):
        for value in ['', '   ', 'x'*201]:
            self.assertEqual(self.client.post('/',data={'task':value}).status_code,400)
        with sqlite3.connect(self.database) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM todos').fetchone()[0],0)
    def test_length_boundary(self):
        self.assertEqual(self.client.post('/',data={'task':'x'*200}).status_code,303)
    def test_escape_html_and_parameterize_sql(self):
        payload='<script>alert(1)</script>\'; DROP TABLE todos; --'
        self.client.post('/',data={'task':payload})
        page=self.client.get('/').text
        self.assertNotIn('<script>alert(1)</script>',page)
        self.assertIn('&lt;script&gt;',page)
        with sqlite3.connect(self.database) as db:
            self.assertEqual(db.execute('SELECT task FROM todos').fetchone()[0],payload)
    def test_complete_reopen_and_delete(self):
        self.client.post('/',data={'task':'Complete experiment'})
        for expected in [1,0]:
            self.assertEqual(self.client.post('/tasks/1/toggle').status_code,303)
            with sqlite3.connect(self.database) as db:
                self.assertEqual(db.execute('SELECT done FROM todos').fetchone()[0],expected)
        self.assertEqual(self.client.post('/tasks/1/delete').status_code,303)
        self.assertNotIn('Complete experiment',self.client.get('/').text)
    def test_missing_task_and_read_only_get(self):
        self.assertEqual(self.client.post('/tasks/99/toggle').status_code,404)
        self.assertEqual(self.client.post('/tasks/99/delete').status_code,404)
        self.assertEqual(self.client.get('/tasks/1/delete').status_code,405)
    def test_health(self):
        self.assertEqual(self.client.get('/health').json,{'status':'ok'})

class BackendTests(unittest.TestCase):
    def test_liveness_without_database(self):
        def unavailable():raise pymysql.OperationalError('offline')
        c=backend.create_app(unavailable).test_client()
        self.assertEqual(c.get('/health').status_code,200)
        self.assertEqual(c.get('/ready').status_code,503)
        self.assertEqual(c.get('/api/status').status_code,503)
    def test_status_contract_with_mock_database(self):
        # This verifies the response contract, not a live MySQL connection.
        db=MagicMock();cursor=db.__enter__.return_value.cursor.return_value.__enter__.return_value
        cursor.fetchone.return_value={'total':7}
        c=backend.create_app(lambda:db).test_client()
        self.assertEqual(c.get('/ready').json,{'status':'ready'})
        self.assertEqual(c.get('/api/status').json,{'message':'Backend API Running','database':'connected','visits':7})

class FeatureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.users={'admin':generate_password_hash('temporary-test-password')}
    def test_login(self):
        self.assertEqual(login.login('admin','temporary-test-password',self.users),'Login Successful')
        self.assertEqual(login.login('admin','wrong',self.users),'Invalid Credentials')
        self.assertEqual(login.login('nobody','temporary-test-password',self.users),'Invalid Credentials')
    def test_completion_percent(self):
        for done,total,expected in [(0,0,0.0),(0,5,0.0),(1,3,33.33),(5,5,100.0)]:
            self.assertEqual(feature.completion_percent(done,total),expected)
    def test_invalid_counts(self):
        for args in [(-1,2),(3,2),(0,-1)]:
            with self.assertRaises(ValueError):feature.completion_percent(*args)
        for args in [(True,3),(1.5,3),(1,'3')]:
            with self.assertRaises(TypeError):feature.completion_percent(*args)

if __name__=='__main__':unittest.main()
