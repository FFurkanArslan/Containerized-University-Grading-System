from flask import Flask, request, Blueprint, jsonify
from Models.Turkish import TurkishInfo
from Decorators.Teachers import teachers
from Connection.Connection import *
from flask_sqlalchemy import SQLAlchemy
Turkce = Blueprint("Turkce", import_name=__name__)


@Turkce.route('/turkish_add', methods=['POST'])
@teachers()
def student_turkish():
    fname = request.form['fname']
    lname = request.form['lname']
    studentID = request.form['studentID']
    studentID_exists = TurkishInfo.query.filter_by(studentID=studentID).first()
    if studentID_exists:
        return jsonify({'message': 'This studentID already exists'})
    else:
        student = TurkishInfo(fname=fname, lname=lname, studentID=studentID)
        db.session.add(student)
        db.session.commit()
        return jsonify({"message": "Student successfully added to Turkish class"})


@Turkce.route('/turkish_delete/<int:id>', methods=['POST'])
@teachers()
def turkish_delete(id):
    user_to_delete = TurkishInfo.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return jsonify({"message": "Student deleted"})
    except:
        return jsonify({"message": "ERROR"})


@Turkce.route("/turkceguncelle/<int:id>", methods=["POST"])
@teachers()
def updateturkish(id):
    admin = TurkishInfo.query.get_or_404(id)
    admin.fname = request.form["fname"]
    admin.lname = request.form["lname"]
    admin.studentID = request.form["studentID"]
    db.session.commit()
    return jsonify({"message": "updated"})


@Turkce.route('/turkishlist/<int:id>', methods=['POST'])
@teachers()
def turkishlist(id):
    result = db.session.query(TurkishInfo).filter(TurkishInfo.id == id)
    for turkish in result:
        return jsonify("ID:", turkish.id, "Fname: ", turkish.fname, "Lname:", turkish.lname, "StudentID:", turkish.studentID, "Exam1", turkish.exam1, "Exam2", turkish.exam2, "Exam3", turkish.exam3, "GPA", turkish.gpa, "Harf Notu", turkish.lgrades)


@Turkce.route('/turkcesinavgir/<int:id>', methods=['POST'])
@teachers()
def turkishsinavgir(id):
    user = TurkishInfo.query.get(id)
    user.exam1 = request.form['exam1']
    user.exam2 = request.form['exam2']
    user.exam3 = request.form['exam3']
    user.gpa = (int(user.exam1)+int(user.exam2)+int(user.exam3))/3
    user.lgrades = []

    if user.gpa >= 91 and user.gpa <= 100:
        user.lgrades = "AA"
    elif user.gpa >= 81 and user.gpa < 91:
        user.lgrades = "BA"
    elif user.gpa >= 71 and user.gpa < 81:
        user.lgrades = "BB"
    elif user.gpa >= 61 and user.gpa < 71:
        user.lgrades = "CB"
    elif user.gpa >= 51 and user.gpa < 61:
        user.lgrades = "CC"
    elif user.gpa >= 41 and user.gpa < 51:
        user.lgrades = "DC"
    elif user.gpa >= 33 and user.gpa < 41:
        user.lgrades = "DD"
    elif user.gpa >= 21 and user.gpa < 33:
        user.lgrades = "FD"
    elif user.gpa >= 0 and user.gpa < 21:
        user.lgrades = "FF"
    else:
        return jsonify({"Message": "Invalid Input!"})
    db.session.commit()
    return jsonify({"message": "Succes"})
