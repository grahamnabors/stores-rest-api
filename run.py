from app import app
from db import db

db.init_app(app)

@app.before_first_request # Before the first request runs it will run this block of code which will create all of the tables unless they exist already.
def create_tables():
    db.create_all()