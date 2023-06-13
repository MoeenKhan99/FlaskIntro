# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def addition():
    """Add a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = add(a,b)
    return str(answer)

@app.route("/sub")
def subtraction():
    """Subtract a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = sub(a,b)
    return str(answer)

@app.route("/mult")
def multiplication():
    """Multiply a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = mult(a,b)
    return str(answer)

@app.route("/div")
def division():
    """Divide a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = div(a,b)
    return str(answer)



#Example of working code: in  http://localhost:5000/add?a=10&b=20 should 
# return string response of 30