from datetime import datetime as dt
from lib2to3.pytree import Base

class BaseModel:
    def set_datetime(self):
        d = str(dt.now()).split(" ")
        
        self.registered_date = d[0]
        self.registered_time = d[1]


class User(BaseModel):
    def __init__(self, fullname, merchant_name, primary_upi_id, user_id, password, finger_auth = False):
        self.fullname = fullname 
        self.merchant_name = merchant_name
        self.primary_upi_id = primary_upi_id
        self.user_id = user_id
        self.password = password
        self.finger_auth = finger_auth

        self.set_datetime()

    

class Transaction(BaseModel): 
    def __init__(self, user_id, token, transacted_to, transaction_id, amount) -> None:
        self.user_id = user_id
        self.token = token
        self.transacted_to = transacted_to
        self.transaction_id = transaction_id
        self.amount = amount
        d = str(dt.now()).split(" ")
        
        self.transaction_date = d[0]
        self.transaction_time = d[1]

        # self.set_datetime()
        