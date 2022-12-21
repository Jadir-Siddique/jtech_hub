from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@views.route('/cart')
def cart():
    return render_template("cart.html")

@views.route('/checkout')
def checkout():
    return render_template("checkout.html")


