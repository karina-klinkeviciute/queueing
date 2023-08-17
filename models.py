from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
    served = db.Column(db.Boolean, default=False)

class Teacher(db.Model):
    name = db.Column(db.String(100), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


# code for teacher creation from Python command line:

"""
from app import app, db  # Import the Flask app and db object from your app
from models import Teacher  # Import the Teacher model
from werkzeug.security import generate_password_hash

# Create an application context
app.app_context().push()

# Create a database session
session = db.session

# Replace "your_username_here" and "your_password_here" with actual values
username = "your_username_here"
password = "your_password_here"
name = "your_name"

# Create a new teacher user and add it to the session
new_teacher = Teacher(name=name, username=username, password=generate_password_hash(password))
session.add(new_teacher)
session.commit()

print("Teacher user created successfully.")

"""