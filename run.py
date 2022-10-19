from Views.AdminBlueprint import Admin
from Views.AllStudentsListBlueprint import AllStudents
from Views.MatematikBlueprint import Matematik
from Views.SosyalBlueprint import Sosyal
from Views.TeacherBlueprint import Teacher
from Views.TurkceBlueprint import Turkce
from Connection.Connection import *
from ErrorHandler.Error import bp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@some-postgres:5432/furkan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'testing'
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
app.register_blueprint(Admin)
app.register_blueprint(AllStudents)
app.register_blueprint(Teacher)
app.register_blueprint(Matematik)
app.register_blueprint(Sosyal)
app.register_blueprint(Turkce)
app.register_blueprint(bp)

if __name__ == '__main__':
    db.init_app(app)
    app.run(host="0.0.0.0",port="5000",debug=True)
