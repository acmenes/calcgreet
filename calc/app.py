# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home_page():
    return "This is a calculator!"

@app.route('/add')
def add_num():
    '''
    Add a and b
    '''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)
    return f"<h1>{a} + {b} is {result}</h1>"

@app.route('/sub')
def sub_num():
    '''
    Subtract a and b
    '''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return f"<h1>{a} - {b} is {result}</h1>"

@app.route('/mult')
def mult_num():
    '''
    Multiply a and b
    '''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return f"<h1>{a} x {b} is {result}</h1>"

@app.route('/div')
def div_num():
    '''
    Divide a and b
    '''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return f"<h1>{a} divided by {b} is {result}</h1>"