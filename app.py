#skeleton flask


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


from models import User
from extensions import db

from auth import auth
from admin import admin
from company import company
from student import student

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(company)
app.register_blueprint(student)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///placementapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from models import *


#mian stufff
@app.route('/')
def home():
    return render_template('index.html')
    #return "<h1>Welcome to Placement Portal!</h1>"


#iffy
@app.route('/resume')
def resume():
    return "<h1>Resume Display Page</h1><h5>can be accessed by admin (via application page) and student</h5>"


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
