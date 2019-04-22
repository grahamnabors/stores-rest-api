import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # Telling SQLAlchemy that a column named 'id' is the Primary Key)
    username = db.Column(db.String(80)) # '80 limits the size of the username'
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self) # The 'session' is a collection of objects that we will write to the database.
        db.session.commit()

    @classmethod # We are not using 'self' anywhere in this method so it is probably worth while to make it a Class Method. Change 'self' to 'cls' for Class Methods. As well as 'User' to 'cls'.
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() # Returns the FIRST ROW found.

    @classmethod # We are not using 'self' anywhere in this method so it is probably worth while to make it a Class Method. Change 'self' to 'cls' for Class Methods. As well as 'User' to 'cls'.
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first() # (column_name = argument_name)