#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the string to the console
    return f'{parameter}'

@app.route('/count/<int:integer>')
def count(integer):
    numbers = range(integer)
    result = '\n'.join(str(num) for num in numbers)
    return f'{result}\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
       result= num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation."

    return f'{result}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
