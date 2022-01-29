from flask import Flask, request, Blueprint
import auth, json
from models import User, Transaction
import db_api


app = Flask(__name__)
# app.register_blueprint()

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
    

@app.route("/profile")
def get_profile():
    user_id = request.args.get('user_id')
    return db_api.get_profile_details(user_id)
    
@app.route("/transaction", methods=["GET","POST"])
def transaction():
    if request.method == "GET":
        t_id = request.args.get()
        print("get transaction detailas called with transaction id: ", t_id)
        return db_api.get_transaction_details(t_id)

    elif request.method == "POST":
        f = request.form
        t = Transaction(f['user_id'], f['token'], f['transacted_to'], f['transaction_id'], f['amount'])
        if db_api.store_transaction(t):
            return {"status": "Success", "message": "Transaction Successfully Created"}
        
        return {"status": "Success", "message": "Transaction Failed"}

@app.route("/transactions")
def get_all_transactions():
    return db_api.get_all_transactions(request.args.get('user_id'))
    # return {"status": "Success", "all_transactions": db_api.get_all_transactions(request.args.get('user_id'))}

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")