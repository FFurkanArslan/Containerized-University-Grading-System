from flask import Flask,request,Blueprint,jsonify,make_response
from Decorators.AdminRequired import admin_required
from datetime import datetime, timedelta
from Connection.admindb import adminconn
from Connection.config import Config
import bcrypt
import jwt
from Connection.Connection import *
Admin=Blueprint("Admin",import_name=__name__)
admins = adminconn.MongoDB()
users = Config.MongoDB()
@Admin.route('/adminsignup', methods=['POST'])
def signup():
    fname = request.form["fname"]
    email = request.form["email"]
    role = request.form["role"]
    password = request.form["password"]
    password2 = request.form["password2"]
    if fname == "" or email == "":
        return jsonify({"Validation error": "It cant be empty"})
    if password != password2:
        return jsonify({"error": "Passwords must be same "})
    try:
        admins.find({"email": email})[0]
        return jsonify({"error": "email already in use"})
    except IndexError:
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        admins.insert_one({
            "fname": fname,
            "email": email,
            "role": role,
            "password": hashed_pw
        })
        return jsonify({"message": "Succesful"})


@Admin.route('/adminlogin', methods=['POST'])
def login():
    email = request.form["email"]
    password = request.form["password"]
    role = request.form["role"]
    dt = datetime.now() + timedelta(days=2)
    try:
        user = admins.find({"$and": [{"email": email}, {"role": role}]})[0]
    except IndexError:
        return jsonify({"User not found"})
    hashed_pw = user["password"]
    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        token = jwt.encode({
            'email': email,
            'password': password,
            'role': role,
            'exp': dt
        }, app.config['SECRET_KEY'])
        # print(token)
        res = make_response("Succesfull", 200)
        # print(request.cookies)
        res.set_cookie(
            "JWT",
            value=token,
            expires=dt,
            httponly=True)
        return res
    else:
        return jsonify({"error": "Wrong password"})

@Admin.route('/create_teacher', methods=['POST'])
@admin_required()
def create_teacher():
    fname = request.form["fname"]
    email = request.form["email"]
    role = request.form["role"]
    password = request.form["password"]
    password2 = request.form["password2"]
    if fname == "" or email == "":
        return jsonify({"Validation error": "It cant be empty"})
    if password != password2:
        return jsonify({"error": "Passwords must be same "})
    try:
        users.find({"email": email})[0]
        return jsonify({"error": "email already in use"})
    except IndexError:
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert_one({
            "fname": fname,
            "email": email,
            "role": role,
            "password": hashed_pw
        })
        return jsonify({"message": "Succesful"})


@Admin.route('/delete_teacher', methods=['POST'])
@admin_required()
def delete_teacher():
    email = request.form["email"]
    myquery = {"email": email}
    users.delete_one(myquery)
    return jsonify({"message": "success"})
