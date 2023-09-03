from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_user import UserManager
from flask_user import UserMixin
from flask import Blueprint, render_template, redirect, url_for
from flask_user import login_required, current_user, roles_required
from flask_bcrypt import Bcrypt  # Import Bcrypt for password hashing

# Routes blueprints

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(views)
        
app.config.from_object('config')
# app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/afrotour'  # Replace with your MySQL database URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

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

    def __init__(self, Country, area, Geometry, Attraction=None, Accommodations=None, Activities=None, Travel_Tips=None, Transportation=None):
        self.Country = Country
        self.area = area
        self.Attraction = Attraction
        self.Accommodations = Accommodations
        self.Activities = Activities
        self.Travel_Tips = Travel_Tips
        self.Transportation = Transportation
        self.Geometry = Geometry

user_manager = UserManager(app, db, User)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
