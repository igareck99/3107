from sqlalchemy import *
from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),
                     nullable = False,
                     unique = True)
    password = db.Column(db.String(250),
                         nullable=False)

    @property
    def serialize(self):
        return {'id': self.id, 'name': self.name}