from flask import Flask

app = Flask(__name__)

# /welcome to return "Welcome"
@app.route('/welcome')
def welcome():
    return "welcome!"

# /welcome/home to return "Welcome Home"
@app.route('/welcome/home')
def welcome_home():
    return "Welcome Home!"

#/welcome/back to return "Welcome Back"
@app.route ('/welcome/back')
def welcome_back():
    return "Welcome Back!"