import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    
    def post(self):
        data = UserRegister.parser.parse_args() # force=True means you DO NOT need the ContentType Header to be 'application/json' # silent=True does not return an error, instead returns 'None'

        if UserModel.find_by_username(data['username']): # Essentially this line is: if User.find_by_username(data['username']) is not None:
           return {"message": "A user with that username already exists"}, 400 # If we 'return' then no other code below is ran

        user = UserModel(**data) # Same as: 'UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully"}, 201 # 201 means 'Created'