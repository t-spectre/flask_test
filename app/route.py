from app import app,db
from flask import render_template,redirect,url_for,flash,get_flashed_messages
from models import Task
import forms
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    # return '<h1>fff</h1>'
    tasks=Task.query.all()
    return render_template('index.html',tasks=tasks)

@app.route('/add',methods=['GET','POST'])
def add():
    # return '<h1>fff</h1>'
    form=forms.AddTaskForm()
    if form.validate_on_submit():

        print('Submitted ',form.title.data)
        t=Task(title=form.title.data,date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task is added')
        return redirect(url_for('index'))
    return render_template('add.html',form=form)

@app.route('/edit/<int:task_id>',methods=['GET','POST'])
def edit(task_id):
    task=Task.query.get(task_id)
    form=forms.AddTaskForm()
    if task:
        if form.validate_on_submit():
            task.title=form.title.data
            task.date=datetime.utcnow()
            db.session.commit()
            flash('Task has been updated')
            return redirect(url_for('index'))
        form.title.data=task.title
        return render_template('edit.html',form=form,task_id=task_id)
    return redirect(url_for('index'))
