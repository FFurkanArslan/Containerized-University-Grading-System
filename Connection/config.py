from pymongo import MongoClient
import os
from dotenv import load_dotenv
from Validators.validator import Validator
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")
print(MONGO_URI)


class Config():
    def MongoDB():
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DATABASE]
        records=db.Yetki
        return records
