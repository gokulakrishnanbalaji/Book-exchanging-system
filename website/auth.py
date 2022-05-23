
import email
from flask import Blueprint, render_template, request, flash, redirect, url_for

from website import views
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:

            if check_password_hash(user.password, password):
                flash('Logged in successfully!')
                login_user(user, remember=True)
                
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.')
        else:
            flash('Username does not exist.')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register',methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        print('hi')
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        regno=request.form.get('regno')
        phno=request.form.get('phno')
        city=request.form.get('city')

        user = User.query.filter_by(email=email).first()
        print(user)
        if user:
            flash("Email already present")
        elif len(email)<4:
            flash("Email must be greater than 4 character")
        else:
            new_user=User(name=name,email=email,password=generate_password_hash(
                password, method='sha256'),regno=regno,city=city,phno=phno)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

            return redirect(url_for('views.home'))
    return render_template("registration.html", user=current_user)
