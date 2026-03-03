from flask import Blueprint, render_template

student = Blueprint('student', __name__)

@student.route('/student')
def student():
    return render_template('student.html')
    #return "<h1>Student Dashboard</h1>"

@student.route('/complist')
def complist():
    return render_template('complist.html')
    #return "<h1>View Companies' list</h1><h5> can be accessed by student only</h5>"

@student.route('/history')
def history():
    return render_template('history.html')
    #return "<h1>Student Application History Page</h1><h5>can be accessed by student only</h5>"


@student.route('/student_profile')
def profile():
    return render_template('student_profile.html')
    #return "<h1>Student Profile Page</h1> <h5>can be accessed by student only</h5>"

@student.route('/student_edit_profile')
def edit_profile():
    return render_template('student_edit_profile.html')
    #return "<h1>Edit Student Profile Page</h1> <h5>can be accessed by student and student profile only</h5>"