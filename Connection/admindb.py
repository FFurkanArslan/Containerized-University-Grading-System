from pymongo import MongoClient
import os
from dotenv import load_dotenv
from Validators.adminvalidation import AdminValidation
from dotenv import load_dotenv
import os


load_dotenv()



MONGO_URI = os.getenv("MONGO_URI")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")
print(MONGO_URI)


class adminconn():
    def MongoDB():
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DATABASE]
        records=db.Admin
        return records
