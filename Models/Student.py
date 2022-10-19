from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from Connection.Connection import db
from flask_login import UserMixin

class StudentInfo(db.Model,UserMixin):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(40), nullable=False)
    lname = db.Column(db.String(40), nullable=False)
    studentID = db.Column(db.Integer())
    exam1 = db.Column(db.Integer(), default=0)
    exam2 = db.Column(db.Integer(), default=0)
    exam3 = db.Column(db.Integer(), default=0)
    gpa = db.Column(db.Integer(), default=0)
    lgrades = db.Column(db.String(255), default=' ')


    def __init__(self, fname,lname,studentID):
        self.fname = fname
        self.lname = lname
        self.studentID = studentID


db.create_all()

