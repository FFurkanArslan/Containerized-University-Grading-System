from flask import Flask,request,Blueprint,jsonify,make_response
from datetime import datetime, timedelta
from Connection.config import Config
import bcrypt
import jwt
from Connection.Connection import *
Teacher=Blueprint("Teacher",import_name=__name__)

users = Config.MongoDB()
@Teacher.route('/teacherlogin', methods=['POST'])
def teacherlogin():
    email = request.form["email"]
    password = request.form["password"]
    role = request.form["role"]
    dt = datetime.utcnow()+timedelta(seconds=60)
    try:
        user = users.find({"$and": [{"email": email}, {"role": role}]})[0]
    except IndexError:
        return jsonify({"error":"User not found"})
    hashed_pw = user["password"]
    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        token = jwt.encode({
            'email': email,
            'password': password,
            'role': role,
            'exp': dt
        }, app.config['SECRET_KEY'])
        res = make_response("Successful", 200)
        res.set_cookie(
            "JWT",
            value=token,
            expires=dt,
            httponly=True)
        return res
    else:
        return jsonify({"error": "Wrong password"})
