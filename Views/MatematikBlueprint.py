from flask import Flask, request, Blueprint, jsonify
from Models.Math import MathInfo
from Decorators.Teachers import teachers
from Connection.Connection import db
Matematik=Blueprint("Matematik", import_name=__name__)


@Matematik.route('/math_add', methods=['POST'])
@teachers()
def student_math():
    fname = request.form['fname']
    lname = request.form['lname']
    studentID = request.form['studentID']
    studentID_exists = MathInfo.query.filter_by(studentID=studentID).first()
    if studentID_exists:
        return jsonify({'message': 'This studentID already exists'})
    else:
        student = MathInfo(fname=fname, lname=lname, studentID=studentID)
        db.session.add(student)
        db.session.commit()
        return jsonify({"message": "Student successfully added to Math class"})


@Matematik.route('/math_delete/<int:id>', methods=['POST'])
@teachers()
def math_delete(id):
    user_to_delete = MathInfo.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return jsonify({"message": "Student deleted"})
    except:
        return jsonify({"message": "ERROR"})


@Matematik.route("/matematikguncelle/<int:id>", methods=["POST"])
@teachers()
def updatemath(id):
    admin = MathInfo.query.get_or_404(id)
    admin.fname = request.form["fname"]
    admin.lname = request.form["lname"]
    admin.studentID = request.form["studentID"]
    db.session.commit()
    return jsonify({"message": "updated"})


@Matematik.route('/mathlist/<int:id>', methods=['POST'])
@teachers()
def mathlist(id):
    result = db.session.query(MathInfo).filter(MathInfo.id == id)
    for math in result:
        return jsonify("ID:", math.id, "Fname: ", math.fname, "Lname:", math.lname, "StudentID:", math.studentID, "Exam1", math.exam1, "Exam2", math.exam2, "Exam3", math.exam3, "GPA", math.gpa, "Harf Notu", math.lgrades)


@Matematik.route('/matematiksinavgir/<int:id>', methods=['POST'])
@teachers()
def mathsinavgir(id):
    user = MathInfo.query.get(id)
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
