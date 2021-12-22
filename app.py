import dotenv
from flask import Flask, render_template, session
from functools import wraps
from dotenv import load_dotenv
from pathlib import Path

from werkzeug.utils import redirect
from user import models
import pymongo

app = Flask(__name__)
app.secret_key = "b'_5#y2L'F4Q|8\z'n?!f4^x[]}ec]}{][f|]}{t}r5$df%dfg54{}"

#database
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.user_login_system

#routes
@app.route('/user/signup', methods=['POST'])
def signup():
    return models.handleUser().signup()  

@app.route('/user/signout')
def signout():
    return models.handleUser().destroysession()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user/login', methods=['POST'])
def login():
    return models.handleUser().login()

#check if login
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()