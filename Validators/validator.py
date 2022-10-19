from pymongo import MongoClient
from collections import OrderedDict
import sys


class Validator():
    client = MongoClient('mongodb://mongo-server:27017/')
    db = client.Yetkililer
    collist = db.list_collection_names()
    if "Yetki" in collist:
        print("The collection exists.")
    else:
        db.create_collection("Yetki")
    schema = {"$jsonSchema":
            {
                "bsonType": "object",
                "required": ["fname", "email"],
                "properties": {
                    "fname": {
                        "bsonType": "string",
                        "description": "must be a string "
                    },
                    "email": {
                        "bsonType": "object",
                        "description": "must be a string "
                    },
                    "password": {
                        "bsonType": "object",
                        "description": "hashed_pw"
                    },
                    "role":{
                        "bsonType": "string",
                        "description":"role"
                    }
                }
            }}
    cmd =OrderedDict([('collMod', 'Yetki'), ('validator', schema),('validationLevel', 'moderate'), ('validationAction', 'warn')])
    db.command(cmd)
    
