from datetime import datetime
import typing
import strawberry
import db_api


@strawberry.input
@strawberry.type
class Transaction:
    _id:  str
    amount:  str
    registered_date: datetime
    registered_time: datetime
    token:  str
    traansacted_to:  str
    transaction_date: datetime
    transaction_time: datetime
    transaction_id:  str
    user_id:  str

@strawberry.input
@strawberry.type
class User: 
    _id: typing.Optional[str]
    fullname: typing.Optional[str]
    merchant_name: typing.Optional[str]
    password: typing.Optional[str]
    primary_upi_id: typing.Optional[str]
    registered_date: typing.Optional[str]
    registered_time: typing.Optional[str]
    user_id: typing.Optional[str]    

def get_transactions(condition: Transaction) -> str:
    print("get_transactions called")
    # return db_api.get_all_transactions(condition)

def get_users(user_id: str = None, fullname: str=None, merchant_name: str=None , primary_upi_id: str=None ) -> str:
    print("get_users called with id : ", user_id)
    return db_api.get_profile_details(user_id)

@strawberry.type
class Query:
    transactions: typing.List[Transaction] = strawberry.field(resolver=get_transactions)
    users: typing.List[User] = strawberry.field(resolver=get_users)

@strawberry.type
class Mutation: 
    @strawberry.field
    def add_user(self, user: User) -> str:
        print("add user in graphql is invoked with user: ",user)
        return "Success"
         
    @strawberry.field
    def add_transaction(self, transaction: Transaction) -> str: 
        print("add__transaction in graphql is invoked with transaction: ",transaction)
        return "success"


schema = strawberry.Schema(query=Query, mutation=Mutation)        