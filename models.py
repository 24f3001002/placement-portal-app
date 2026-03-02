from app import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable  = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password_hash = db.Column(db.String(200), nullable = False)
    role = db.Column(db.String(7), nullable = False) #company/student
    #time_created = db.Column(db.Datetime).......... should i?



class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), unique=True)
    f_name = db.Column(db.String(20))
    l_name = db.Column(db.String(20))
    department = db.Column(db.String(100))
    cgpa = db.Column(db.Float)
    phone = db.Column(db.String(20))
    resume_path = db.Column(db.String(200))
    is_blacklisted = db.Column(db.Boolean, default=False)



class Company(db.Model):
    __tablename__ = 'companies'
    company_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), unique=True)
    company_name = db.Column(db.String(100), nullable=False)
    hr_fname = db.Column(db.String(20), nullable=False)
    hr_lname = db.Column(db.String(20), nullable=False)
    hr_email = db.Column(db.String(100), nullable=False)
    website = db.Column(db.Text)
    description = db.Column(db.Text)
    approval_status = db.Column(db.String(8), default='pending')  # pending/approved/rejected
    is_blacklisted = db.Column(db.Boolean, default=False)




class PlacementDrive(db.Model):
    __tablename__ = 'placement_drives'
    



class Application(db.Model):
    __tablename__ = 'applications'