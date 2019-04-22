from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) # 'precision' specifies the number of numbers after a decimal point

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) # Table_name.column_name
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name

    def save_to_db(self):
        db.session.add(self) # The 'session' is a collection of objects that we will write to the database.
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()