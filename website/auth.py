from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password): # type: ignore
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")

        data = request.form
        print(data)

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        if len(email) < 4:  # type: ignore  
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2: # type: ignore  
            flash('First name must be greater than 1 character.', category='error')
        elif len(password) < 7: # type: ignore  
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(name=name, email=email, phone=phone, password=generate_password_hash(password, method='sha256')) # type: ignore  
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
        return redirect(url_for('views.dashboard'))

    return render_template("signup.html", user=current_user)

