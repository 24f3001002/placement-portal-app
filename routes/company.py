from flask import Blueprint, render_template

company = Blueprint('company', __name__)


@company.route('/dashboard')
def dashboard():
    return render_template('company.html')

# @company.route('/company')
# def company():
#     return render_template('company.html')
#     #return "<h1>Company Dashboard</h1>"

@company.route('/drivelist')
def drivelist():
    return render_template('drivelist.html')
    #return "<h1>Specific Drive's Application Page</h1><p> List of students applied for that drive</p><h5>can be accessed by company only</h5>"

@company.route('/createdrive')
def createdrive():
    return render_template('createdrive.html')
    #return "<h1>Create Drive Page</h1><h5>can be accessed by company only</h5>"

@company.route('/company_profile')
def company_profile():
    return render_template('company_profile.html')
    #return "<h1>Company Profile Page</h1><h5>can be accessed by company only</h5>"

@company.route('/company_edit_profile')
def company_edit_profile():
    return render_template('company_edit_profile.html')
    #return "<h1>Company Edit Profile Page</h1><h5>can be accessed by company and company profile only</h5>"