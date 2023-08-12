from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, Student, Teacher
from werkzeug.security import check_password_hash
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queue.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if "name" in request.form:
            name = request.form.get("name")

        elif "student_id" in request.form:
            student_id = request.form.get("student_id")
    new_students = Student.query.filter_by(served=False).order_by(Student.id.desc())
    served_students = Student.query.filter_by(served=True).order_by(Student.id.desc())
    return render_template('index.html', new_students=new_students, served_students=served_students)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form.get('name')
    new_student = Student(name=name)
    db.session.add(new_student)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/serve_student', methods=['POST'])
def serve_student():
    student_id = request.form.get('student_id')
    student = Student.query.get(student_id)
    student.served = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        teacher = Teacher.query.filter_by(username=username).first()

        if teacher and check_password_hash(teacher.password, password):
            session['teacher'] = True  # Add teacher to the session
            flash('Logged in successfully as teacher!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)