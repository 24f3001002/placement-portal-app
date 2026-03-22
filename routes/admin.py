# # from flask import Blueprint, render_template

# # admin = Blueprint('admin', __name__)

# # @admin.route('/admin')
# # def admin():
# #     return render_template('admin.html')
# #     #return "<h1>Admin Dashboard</h1>"

# # @admin.route('/drive')
# # def viewdrive():
# #     return render_template('drive.html')
# #     #return "<h1>Drive Page</h1><p> Descripton of specifc drive</p><h5>can be accessed by admin and student</h5>"

# # @admin.route('/applications')
# # def stdapplication():
# #     return render_template('applications.html')
# #     #return "<h1>Student's Drive Application</h><p> **for a specific drive</p><h5>can be accessed by admin and student</h5>"

# from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# from extensions import db
# from models import User, Student, Company, PlacementDrive, Application
# from functools import wraps
# from flask_login import login_required, current_user

# admin = Blueprint('admin', __name__, url_prefix='/admin')


# def admin_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if not current_user.is_authenticated or current_user.role != 'admin':
#             flash('Admin access required.', 'danger')
#             return redirect(url_for('auth.login'))
#         return f(*args, **kwargs)
#     return decorated_function


# # ─── Admin Dashboard ────────────────────────────────────────────────────────

# @admin.route('/')
# @login_required
# @admin_required
# def dashboard():
#     # Registered & approved companies
#     companies = (
#         db.session.query(Company)
#         .filter(Company.approval_status == 'approved')
#         .all()
#     )

#     # Companies awaiting approval
#     pending_companies = (
#         db.session.query(Company)
#         .filter(Company.approval_status == 'pending')
#         .all()
#     )

#     # All placement drives
#     drives = db.session.query(PlacementDrive).all()

#     # All students
#     students = db.session.query(Student).all()

#     # All applications (with student + drive info)
#     applications = (
#         db.session.query(Application, Student, PlacementDrive, Company)
#         .join(Student, Application.student_id == Student.student_id)
#         .join(PlacementDrive, Application.drive_id == PlacementDrive.drive_id)
#         .join(Company, PlacementDrive.company_id == Company.company_id)
#         .order_by(Application.applied_time.desc())
#         .all()
#     )

#     return render_template(
#         'admin/admin.html',
#         companies=companies,
#         pending_companies=pending_companies,
#         drives=drives,
#         students=students,
#         applications=applications,
#     )


# # ─── Company Management ──────────────────────────────────────────────────────

# @admin.route('/company/<int:company_id>/approve', methods=['POST'])
# @login_required
# @admin_required
# def approve_company(company_id):
#     company = Company.query.get_or_404(company_id)
#     company.approval_status = 'approved'
#     db.session.commit()
#     flash(f'{company.company_name} approved.', 'success')
#     return redirect(url_for('admin.dashboard'))


# @admin.route('/company/<int:company_id>/reject', methods=['POST'])
# @login_required
# @admin_required
# def reject_company(company_id):
#     company = Company.query.get_or_404(company_id)
#     company.approval_status = 'rejected'
#     db.session.commit()
#     flash(f'{company.company_name} rejected.', 'warning')
#     return redirect(url_for('admin.dashboard'))


# @admin.route('/company/<int:company_id>/blacklist', methods=['POST'])
# @login_required
# @admin_required
# def blacklist_company(company_id):
#     company = Company.query.get_or_404(company_id)
#     company.is_blacklisted = not company.is_blacklisted

#     if company.is_blacklisted:
#         # Cancel all open drives for this company
#         PlacementDrive.query.filter_by(
#             company_id=company_id, status='pending'
#         ).update({'status': 'cancelled'})

#     db.session.commit()
#     state = 'blacklisted' if company.is_blacklisted else 'reinstated'
#     flash(f'{company.company_name} {state}.', 'info')
#     return redirect(url_for('admin.dashboard'))


# # ─── Student Management ──────────────────────────────────────────────────────

# @admin.route('/student/<int:student_id>/blacklist', methods=['POST'])
# @login_required
# @admin_required
# def blacklist_student(student_id):
#     student = Student.query.get_or_404(student_id)
#     student.is_blacklisted = not student.is_blacklisted
#     db.session.commit()
#     state = 'blacklisted' if student.is_blacklisted else 'reinstated'
#     flash(f'{student.f_name} {student.l_name} {state}.', 'info')
#     return redirect(url_for('admin.dashboard'))


# # ─── Drive Detail ─────────────────────────────────────────────────────────────

# @admin.route('/drive/<int:drive_id>')
# @login_required
# @admin_required
# def drive_detail(drive_id):
#     drive = PlacementDrive.query.get_or_404(drive_id)
#     company = Company.query.get(drive.company_id)
#     applications = (
#         db.session.query(Application, Student)
#         .join(Student, Application.student_id == Student.student_id)
#         .filter(Application.drive_id == drive_id)
#         .all()
#     )
#     return render_template(
#         'admin/drive.html',
#         drive=drive,
#         company=company,
#         applications=applications,
#     )


# @admin.route('/drive/<int:drive_id>/complete', methods=['POST'])
# @login_required
# @admin_required
# def mark_drive_complete(drive_id):
#     drive = PlacementDrive.query.get_or_404(drive_id)
#     drive.status = 'complete'
#     db.session.commit()
#     flash('Drive marked as complete.', 'success')
#     return redirect(url_for('admin.drive_detail', drive_id=drive_id))


# # ─── Student Application History ─────────────────────────────────────────────

# @admin.route('/student/<int:student_id>/applications')
# @login_required
# @admin_required
# def student_applications(student_id):
#     student = Student.query.get_or_404(student_id)
#     applications = (
#         db.session.query(Application, PlacementDrive, Company)
#         .join(PlacementDrive, Application.drive_id == PlacementDrive.drive_id)
#         .join(Company, PlacementDrive.company_id == Company.company_id)
#         .filter(Application.student_id == student_id)
#         .order_by(Application.applied_time.desc())
#         .all()
#     )
#     return render_template(
#         'admin/applications.html',
#         student=student,
#         applications=applications,
#     )