from pymongo import MongoClient
from config import DB_CONNECTION_STRING, DB_NAME

# import urllib.parse
# DB_CONNECTION_STRING = f"mongodb+srv://{urllib.parse.quote('anandkulkarni91')}:{urllib.parse.quote('Anand@7097')}@cluster0.pvcf8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# collection.insert_one({"firstname": "nanda kishore", "lastname": "sivaraju", "upi_id": "95095095095@ybl", "user_id": "95095095095", "password": "123465789"})   

client = MongoClient(DB_CONNECTION_STRING)
db = client[DB_NAME]
