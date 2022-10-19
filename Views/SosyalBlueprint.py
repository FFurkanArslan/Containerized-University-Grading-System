from flask import Flask, request, Blueprint, jsonify
from Models.Socials import SocialsInfo
from Decorators.Teachers import teachers
from Connection.Connection import db
Sosyal = Blueprint("Sosyal", import_name=__name__)

@Sosyal.route("/sosyaladd", methods=['POST'])
@teachers()
def SosyalAdd():
    fname = request.form['fname']
    lname = request.form['lname']
    studentID = request.form['studentID']
    studentID_exists = SocialsInfo.query.filter_by(studentID=studentID).first()
    if studentID_exists:
        return jsonify({'message': 'This studentID already exists'})
    else:
        student = SocialsInfo(fname=fname, lname=lname, studentID=studentID)
        db.session.add(student)
        db.session.commit()
        return jsonify({"message": "Student successfully added to Sosyal Bilgiler class"})


@Sosyal.route('/sosyaldelete/<int:id>', methods=['POST'])
@teachers()
def SosyalDelete(id):
    user_to_delete = SocialsInfo.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return jsonify({"message": "Student deleted"})
    except:
        return jsonify({"message": "ERROR"})


@Sosyal.route("/sosyalguncelle/<int:id>", methods=["POST"])
@teachers()
def SosyalUpdate(id):
    admin = SocialsInfo.query.get_or_404(id)
    admin.fname = request.form["fname"]
    admin.lname = request.form["lname"]
    admin.studentID = request.form["studentID"]
    db.session.commit()
    return jsonify({"message": "updated"})


@Sosyal.route('/sosyallist/<int:id>', methods=['POST'])
@teachers()
def sosyallist(id):
    result = db.session.query(SocialsInfo).filter(SocialsInfo.id == id)
    for social in result:
        return jsonify("ID:", social.id, "Fname: ", social.fname, "Lname:", social.lname, "StudentID:", social.studentID, "Exam1", social.exam1, "Exam2", social.exam2, "Exam3", social.exam3, "GPA", social.gpa, "Harf Notu", social.lgrades)


@Sosyal.route('/sosyalsinavgir/<int:id>', methods=['POST'])
@teachers()
def sosyalsinavgir(id):
    user = SocialsInfo.query.get(id)
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
