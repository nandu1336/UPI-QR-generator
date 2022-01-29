from .db_api import db
from datetime import datetime as dt

class User:
    def __init__(self, fullname, merchant_name, primary_upi_id, user_id, password, finger_auth = False):
        self.fullname = fullname 
        self.merchant_name = merchant_name
        self.primary_upi_id = primary_upi_id
        self.user_id = user_id
        self.password = password
        self.finger_auth = finger_auth

        self.set_datetime()

    def set_datetime(self):
        d = str(dt.now()).split(" ")
        
        self.registered_date = d[0]
        self.registered_time = d[1]
        

def is_user_already_registered(user):
    collection = db.users
    return collection.find_one({"user_id": user.user_id})
        
def add_new_user(user):  
    collection = db.users  
    res = collection.insert_one(
        {"fullname": user.fullname, 
        "merchant_name": user.merchant_name, 
        "primary_upi_id": user.primary_upi_id, 
        "user_id": user.user_id, 
        "password": user.password,
        "registered_date": user.registered_date,
        "registered_time": user.registered_time
        })

    return str(res.inserted_id) if res.inserted_id else False

def is_user_valid(user_id, password):
    collection = db.users
    user = collection.find_one({"user_id": user_id})
    if user:
        if password == user['password']:
            return {"status": "Success", "message": "User Successfully Logged In", "token": str(user['_id'])}
        else:
            return {"status": "Success", "message": "Login Failed. Please Check Your Username and Password", "token": ""}
    
    return {"status": "Success", "message": "Login Failed. Please Register to Continue", "token": ""}
