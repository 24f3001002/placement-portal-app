#skeleton flask


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import User
from extensions import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///placementapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from models import *


#mian stufff
@app.route('/')
def home():
    return render_template('index.html')
    #return "<h1>Welcome to Placement Portal!</h1>"

@app.route('/login')
def login():
    return "<h1>Login Page</h1>"

@app.route('/student_signup')
def signup():
    return "<h1>Sign Up Page for students</h1>"

@app.route('/company_signup')
def signup():
    return "<h1>Sign Up Page for companies</h1>"

#iffy
# @app.route('/setup')
# def setup():
#     return "<h1>Initial Setup Page</h1>"



#admin stuff
@app.route('/admin')
def admin():
    return "<h1>Admin Dashboard</h1>"

@app.route('/drive')
def viewdrive():
    return "<h1>Drive Page</h1><p> Descripton of specifc drive</p><h5>can be accessed by admin and student</h5>"

@app.route('/applications')
def stdapplication():
    return "<h1>Student's Drive Application</h><p> **for a specific drive</p><h5>can be accessed by admin and student</h5>"

#companyyyyyyy
@app.route('/company')
def company():
    return "<h1>Company Dashboard</h1>"

@app.route('/drivelist')
def drivelist():
    return "<h1>Specific Drive's Application Page</h1><p> List of students applied for that drive</p><h5>can be accessed by company only</h5>"

# @app.route('/studentappdecision')
# def studentappdecision():
#     return "<h1>Student Application Decision</h1><p>Accept/Reject/Waitlist</p>"

@app.route('/createdrive')
def createdrive():
    return "<h1>Create Drive Page</h1><h5>can be accessed by company only</h5>"

#iffy
@app.route('/resume')
def resume():
    return "<h1>Resume Display Page</h1><h5>can be accessed by admin (via application page) and student</h5>"

#Studentssss
@app.route('/student')
def student():
    return "<h1>Student Dashboard</h1>"

@app.route('/complist')
def complist():
    return "<h1>View Companies' list</h1><h5> can be accessed by student only</h5>"

@app.route('/history')
def history():
    return "<h1>Student Application History Page</h1><h5>can be accessed by student only</h5>"

# @app.route('/viewdive')
# def viewdive():
#     return "<h1>View Drive Details Page</h1>"

@app.route('/profile')
def profile():
    return "<h1>Student Profile Page</h1> <h5>can be accessed by student only</h5>"

@app.route('/edit_profile')
def edit_profile():
    return "<h1>Edit Student Profile Page</h1> <h5>can be accessed by student only</h5>"

# @app.route('/editprofile')
# def editprofile():
#     return "<h1>Edit Student Profile Page</h1>"



#db module 2
# Database Configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskmaster.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize SQLAlchemy
# db = SQLAlchemy(app)

# #now we make tableeee
# class Task(db.Model):
#     # Table name (optional - defaults to class name in lowercase)
#     __tablename__ = 'tasks'
    
#     # Columns
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     status = db.Column(db.String(20), default='pending')
#     priority = db.Column(db.String(10), default='medium')
    
#     # String representation (for debugging)
#     def __repr__(self):
#         return f'<Task {self.id}: {self.title}>'






if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        db.create_all()

    #make admin user after!!!!!
        admin = User.query.filter_by(role='admin').first()
        if not admin:
            admin = User(
                user_id = 1000,
                username='admin',
                email='24f3001002@ds.study.iitm.ac.in',
                password_hash='password1526',
                role='admin'
                )
            db.session.add(admin)
            db.session.commit()

    app.run(debug=True)
