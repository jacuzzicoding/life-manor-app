from flask import Flask, render_template, request, redirect, url_for
from database import SessionLocal, init_db
from models import Task
from datetime import date, datetime

app = Flask(__name__)

init_db()

@app.route('/')
def index():
    session = SessionLocal()
    tasks = session.query(Task).all()
    session.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    session = SessionLocal()
    name = request.form['name']
    deadline = request.form['deadline']
    priority = request.form['priority']
    duration = request.form['duration']
    task = Task(name=name, deadline=deadline, priority=priority, duration=duration)
    session.add(task)
    session.commit()
    session.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)