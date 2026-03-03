from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')
    #return "<h1>Login Page</h1>"

@auth.route('/student_signup')
def student_signup():
    return render_template('student_signup.html')
    #return "<h1>Sign Up Page for students</h1>"

@auth.route('/company_signup')
def company_signup():
    return render_template('company_signup.html')
    #return "<h1>Sign Up Page for companies</h1>"