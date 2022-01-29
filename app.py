from flask import Flask, request, Blueprint
from . import auth
from .auth import User

app = Flask(__name__)

# app = Blueprint('api', __name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["POST"])
def login():
    f = request.form 
    return auth.is_user_valid(f['user_id'], f['password'])

    
@app.route("/register",methods=["POST"])    
def regiseter():
    f = request.form  
    user = User(f['fullname'], f['merchant_name'], f['primary_upi_id'], f['user_id'],f['password'],f['finger_auth'])

    # chech if the user is already registered
    if auth.is_user_already_registered(user) :
        return {"status": "Success", "message": "User Already Exists", "token": ""}

    # create new entery in the table
    uu_id = auth.add_new_user(user)
    if uu_id:
        return {"status": "Success", "message": "User Successfully Registered", "token": uu_id}
    