#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>")
def routed(parameter):
    print(f"{parameter}")
    return f"{parameter}"


@app.route("/count/<int:parameter>")
def count(parameter):
    result = "\n".join(str(i) for i in range(parameter))
    # print(result)
    return result + "\n"


@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
