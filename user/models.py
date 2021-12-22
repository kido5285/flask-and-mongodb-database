from flask import Flask, json, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid

class handleUser:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user)

    def login(self):
        print(request.form, 'login')
        user = db.users.find_one({"email": request.form.get('email')})

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user), 200
        
        return jsonify({"error": "Invalid Credential"}), 401


    def signup(self):
        print(request.form, 'post request')
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": pbkdf2_sha256.encrypt(request.form.get('password'))
        }
        
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "email already in use"}), 400

        if db.users.insert_one(user):
            return self.start_session(user), 200
        
        return jsonify({"error": "Signup failed"}), 400

    def destroysession(self):
        session.clear()
        return redirect('/')