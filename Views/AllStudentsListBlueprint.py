from flask import Flask, request, Blueprint, jsonify
from Decorators.Teachers import teachers
from Connection.Connection import db
AllStudents=Blueprint("AllStudents", import_name=__name__)


@AllStudents.route('/all/<string:ders>', methods=['GET'])
@teachers()
def all(ders):
    table_name = ders
    query = f'SELECT * FROM {table_name}'
    result = db.session.execute(query).fetchall()
    if result:
        result = db.session.execute(query).fetchall()
        return jsonify([r._asdict() for r in result])
    else:
        return jsonify({"message": "Failed"})
