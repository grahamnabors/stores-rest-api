from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') # We have a relationship with 'ItemModel', SQLAlchemy goes into 'item.py' and checks for the 'store_id'.
    # When using 'lazy='dynamic'' then 'self.items' in def json(self) you need to use '.all()'

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name

    def save_to_db(self):
        db.session.add(self) # The 'session' is a collection of objects that we will write to the database.
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()