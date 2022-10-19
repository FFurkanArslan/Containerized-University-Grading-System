from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@some-postgres:5432/furkan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='testing'
app.config["JWT_TOKEN_LOCATION"] = ["headers","cookies"]
def dbConnect():
    global engine, connection, metaData
    engine = db.create_engine(
        'postgresql://postgresql:mysecretpassword@some-postgres:5432/furkan')
    connection = engine.connect()
    metaData = db.MetaData()
    print('Connected to PostgreSQL DB.')


db = SQLAlchemy(app)

migrate = Migrate(app, db)
