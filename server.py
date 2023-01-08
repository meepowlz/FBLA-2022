import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from functools import wraps
import users


# Allows environment variables to be accessed
load_dotenv()


# An instance of the Flask class is created
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Session(app)
port = 8080


# Check if user is logged in for pages requiring a logged-in account
def check_session():
    def decorator(function):
        @wraps(function)
        def wrapper():
            if not session.get('student_number'):
                return redirect(url_for('login_page'))
            return function()
        return wrapper
    return decorator


@app.route("/reset")
def reset_session():
    session.clear()
    return redirect(url_for('login_page'))


# Splash page for the website w/ basic info
@app.route("/")
def splash_page():
    return render_template("base.html")


# Account dashboard for logged-in users
@app.route("/dashboard", methods=["GET", "POST"])
@check_session()
def dashboard_page():
    return render_template("dashboard.html", student_number=session['student_number'])


# Login and Sign-Up page
@app.route("/login", methods=["GET", "POST"])
def login_page():
    if session.get('student_number'):
        return redirect(url_for('dashboard_page'))

    if request.method == "GET":
        error_sign_up = request.args.get('error_sign_up', "")
        error_login = request.args.get('error_login', "")
        return render_template("login.html", error_sign_up=error_sign_up, error_login=error_login)

    if request.method == "POST":
        if request.form['btn'] == "Sign Up":
            new_user_info = {}
            for element_name, value in request.form.items():
                new_user_info[element_name] = value
            new_user_info.pop('btn')

            if users.add_user(new_user_info):
                session['student_number'] = request.form.get('student_number')
                return redirect(url_for('dashboard_page'))
            else:
                return redirect(url_for('login_page',
                                        error_sign_up=f"Student Number {request.form.get('student_number')} is in use."))

        elif request.form['btn'] == "Login":
            if users.check_user(request.form.get('student_number')):
                session['student_number'] = request.form.get('student_number')
                return redirect(url_for('dashboard_page'))
            else:
                return redirect(url_for('login_page',
                                        error_login=f"Student Number {request.form.get('student_number')} does not exist."))


# Flask app is run, allowing access of the webpage at localhost:8080 in a web browser
app.run(host="localhost", port=port)
