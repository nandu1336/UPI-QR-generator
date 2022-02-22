from ast import dump
from pymongo import MongoClient
from bson.json_util import dumps, loads
import json
from config import DB_CONNECTION_STRING, DB_NAME

# import urllib.parse
# DB_CONNECTION_STRING = f"mongodb+srv://{urllib.parse.quote('anandkulkarni91')}:{urllib.parse.quote('Anand@7097')}@cluster0.pvcf8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# collection.insert_one({"firstname": "nanda kishore", "lastname": "sivaraju", "upi_id": "95095095095@ybl", "user_id": "95095095095", "password": "123465789"})   

client = MongoClient(DB_CONNECTION_STRING)
db = client[DB_NAME]

def get_profile_details(k=None,v=None):
    if not k: 
        res = db.users.find({})
        print("res in db_api: ",res)
        # res['status'] = "Scuccess"
        return dumps(res)
    
    res = db.users.find_one({k: v})
    res['status'] = "Success"
    return dumps(res)

def get_transaction_details(t_id):
    return dumps(db.transactions.find({"transaction_id": t_id}))

def get_all_transactions(condition=None):

    if not condition: 
        res = db.transactions.find()
    else:
        # res = db.transactions.find({"user_id": user_id})
        res = db.transactions.find(condition)

    return dumps({"status": "Success", "all_transactions": res})

def store_transaction(transaction):
    res = db.transactions.insert_one({
        "user_id": transaction.user_id,
        "token": transaction.token,
        "transacted_to": transaction.transacted_to,
        "transaction_id": transaction.transaction_id,
        "amount": transaction.amount,
        "transaction_date": transaction.transaction_date,
        "transaction_time": transaction.transaction_time,
    })
    print("res for stor_trasaction:", res)
    return str(res.inserted_id) if res.inserted_id else False