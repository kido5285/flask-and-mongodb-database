from flask import Flask
from app import app
from user import models

@app.route('/user/signup', methods=['GET'])
def signup():
    return models.handleUser().signup()  