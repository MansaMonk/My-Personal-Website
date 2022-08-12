from flask import Flask, flash, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "haile" #secret key (necessary for session usage)
app.config['SERVER_NAME'] = "https://www.haile.tech" 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #removes a possible warning (not tracking all mods to database)
# app.permanent_session_lifetime = timedelta(minutes=5)

#db = SQLAlchemy(app) #column = pieces of info, rows = individual items

# class users(db.Model): #sql table
#     _id = db.Column("id", db.Integer, primary_key=True) #every single row has to have a different id (to prevent errors)
#     name = db.Column(db.String(100))#max length of string is 100 characters
#     email = db.Column(db.String(100))
    
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email



@app.route("/") # adding a "/" to the end of the base domain will bring user to homepage
def home():
    return render_template("index.html", content="Testing")

@app.route("/<path>")
def unknown(path): # when an unavailable page is requested
    return render_template("error404.html")
    
# @app.route("/view")
# def view():
#     return render_template("view.html", values=users.query.all())

# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         session.permanent = True # makes session permanent
#         user = request.form["nm"]
#         session["user"] = user # storing value/info in a session
#         found_user = users.query.filter_by(name=user).first() #finds user
#         if found_user:
#             session["email"] = found_user.email
#         else:
#             usr = users(user, "")
#             db.session.add(usr) #adds usr to table
#             db.session.commit() #must commit anytime you make a change to db
#         flash("Login Successful!")
#         return redirect(url_for("user")) # redirects to blank page with usr
#     else:
#         if "user" in session: # checking if logged in
#             flash("Already logged in!")
#             return redirect(url_for("user"))
#         return render_template("login.html") # if request.method == GET

# @app.route("/user", methods=["POST", "GET"])
# def user():
#     email = None
#     if "user" in session: # checking if user is logged in
#         user = session["user"] # retrieving session data
#         if request.method == "POST":
#             email = request.form["email"]
#             session["email"] = email #add email to session
#             found_user = users.query.filter_by(name=user).first()
#             found_user.email = email #changes user email
#             db.session.commit()

#             flash("Email was saved!")
#         else: # if request is "GET"
#             if "email" in session:
#                 email = session["email"]
#         return render_template("user.html", email=email)
#     else:
#         flash("You are not logged in!")
#         return redirect(url_for("login"))

# @app.route("/about")
# def aboutme():
#     return render_template("aboutme.html")

# @app.route("/test") # adding a "/" to the end of the base domain will bring user to homepage
# def test():
#     return render_template("new.html")

# @app.route("/<name>") # /(anything) 
# def user(name):
#     return f"Hello {name}!"

# @app.route("/admin/") #redirects to homepage if not authorized admin user
# def admin():
#     return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    db.create_all() #creates db if it doesn't already exist, IMPORTANT (place before run)
    app.run(debug=True) #debug=True detects changes and auto-updates