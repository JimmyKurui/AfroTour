from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True)


class Destination(db.Model):
    __tablename__ = 'destinations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Country = db.Column(db.String(255), nullable=False)
    area = db.Column(db.String(255), nullable=False)
    Attraction = db.Column(db.Text, nullable=True)
    Accommodations = db.Column(db.Text, nullable=True)
    Activities = db.Column(db.Text, nullable=True)
    Travel_Tips = db.Column(db.Text, nullable=True)
    Transportation = db.Column(db.Text, nullable=True)
    Geometry = db.Column(db.Text, nullable=False)

    # def __init__(self, Country, area, Geometry, Attraction=None, Accommodations=None, Activities=None, Travel_Tips=None, Transportation=None):
    #     self.Country = Country
    #     self.area = area
    #     self.Attraction = Attraction
    #     self.Accommodations = Accommodations
    #     self.Activities = Activities
    #     self.Travel_Tips = Travel_Tips
    #     self.Transportation = Transportation
    #     self.Geometry = Geometry