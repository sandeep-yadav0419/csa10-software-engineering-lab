"""Single-user lab To Do app with SQLite persistence and escaped HTML."""
import os
import sqlite3
from pathlib import Path
from flask import Flask, abort, redirect, render_template, request, url_for

def create_app(config=None):
    app=Flask(__name__)
    app.config.update(DATABASE=os.environ.get('TODO_DB', str(Path(__file__).with_name('todos.db'))), MAX_CONTENT_LENGTH=16384)
    if config:
        app.config.update(config)
    Path(app.config['DATABASE']).parent.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(app.config['DATABASE']) as db:
        db.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT NOT NULL, done INTEGER NOT NULL DEFAULT 0)')

    def connect():
        db=sqlite3.connect(app.config['DATABASE'], timeout=10)
        db.row_factory=sqlite3.Row
        return db

    @app.route('/', methods=['GET','POST'])
    def index():
        if request.method=='POST':
            task=request.form.get('task','').strip()
            if not task or len(task)>200:
                abort(400, 'Task must contain 1 to 200 characters.')
            with connect() as db:
                db.execute('INSERT INTO todos(task) VALUES (?)',(task,))
            return redirect(url_for('index'), code=303)
        with connect() as db:
            todos=db.execute('SELECT * FROM todos ORDER BY id DESC').fetchall()
        return render_template('index.html',todos=todos)

    @app.post('/tasks/<int:task_id>/toggle')
    def toggle(task_id):
        with connect() as db:
            changed=db.execute('UPDATE todos SET done=1-done WHERE id=?',(task_id,)).rowcount
        if not changed:
            abort(404)
        return redirect(url_for('index'),code=303)

    @app.post('/tasks/<int:task_id>/delete')
    def delete(task_id):
        with connect() as db:
            changed=db.execute('DELETE FROM todos WHERE id=?',(task_id,)).rowcount
        if not changed:
            abort(404)
        return redirect(url_for('index'),code=303)

    @app.get('/health')
    def health():
        with connect() as db:
            db.execute('SELECT 1').fetchone()
        return {'status':'ok'}
    return app

app=create_app()
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000,debug=False)
