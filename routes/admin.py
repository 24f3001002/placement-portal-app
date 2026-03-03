from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def admin():
    return render_template('admin.html')
    #return "<h1>Admin Dashboard</h1>"

@admin.route('/drive')
def viewdrive():
    return render_template('drive.html')
    #return "<h1>Drive Page</h1><p> Descripton of specifc drive</p><h5>can be accessed by admin and student</h5>"

@admin.route('/applications')
def stdapplication():
    return render_template('applications.html')
    #return "<h1>Student's Drive Application</h><p> **for a specific drive</p><h5>can be accessed by admin and student</h5>"
