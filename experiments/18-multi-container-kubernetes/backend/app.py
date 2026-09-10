"""Backend for the Nginx Flask MySQL Kubernetes experiment."""
import os
from flask import Flask
import pymysql

def connect_db():
    return pymysql.connect(host=os.environ.get('DB_HOST','mysql-service'),
        user=os.environ.get('DB_USER','lab'),password=os.environ.get('DB_PASSWORD',''),
        database=os.environ.get('DB_NAME','lab'),connect_timeout=3,read_timeout=3,
        write_timeout=3,autocommit=True,cursorclass=pymysql.cursors.DictCursor)

def create_app(connection_factory=None):
    app=Flask(__name__)
    connect=connection_factory or connect_db

    @app.get('/')
    def home():
        return {'message':'Backend API Running'}

    @app.get('/health')
    def health():
        # Liveness is independent of the database to avoid restart loops.
        return {'status':'ok'}

    @app.get('/ready')
    def ready():
        try:
            with connect() as db:
                with db.cursor() as cursor:
                    cursor.execute('SELECT 1')
                    cursor.fetchone()
            return {'status':'ready'}
        except pymysql.MySQLError:
            return {'status':'waiting_for_database'},503

    @app.get('/api/status')
    def status():
        try:
            with connect() as db:
                with db.cursor() as cursor:
                    cursor.execute('CREATE TABLE IF NOT EXISTS visits (id INT PRIMARY KEY, total INT NOT NULL)')
                    cursor.execute('INSERT INTO visits (id,total) VALUES (1,1) ON DUPLICATE KEY UPDATE total=total+1')
                    cursor.execute('SELECT total FROM visits WHERE id=1')
                    total=cursor.fetchone()['total']
            return {'message':'Backend API Running','database':'connected','visits':total}
        except pymysql.MySQLError:
            return {'message':'Database is not ready. Retry after the MySQL pod becomes ready.'},503
    return app

app=create_app()
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000,debug=False)
