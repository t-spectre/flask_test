from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='ffff'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tasks.db'

db=SQLAlchemy(app)

from route import *   #do it after app!



if __name__=='__main__':
    app.run(debug=True)