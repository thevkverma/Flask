from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator API"


@app.route('/cal', methods = ['POST'])
def calculator():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    if operation == 'add':
        return str(num1 + num2)
    elif operation == 'sub':
        return str(num1 - num2)
    elif operation == 'mul':
        return str(num1 * num2)
    elif operation == 'div':
        if num2!=0:
            return str(num1 / num2)
        else:
            return "Cannot divide by zero" 


@app.route('/cal_browser', methods = ['GET'])
def calculator_browser():
    operation = request.args.get('operation')
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    if operation == 'add':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2
    elif operation == 'mul':
        return num1 * num2
    elif operation == 'div':
        if num2!=0:
            return num1 / num2
        else:
            return "Cannot divide by zero"              


if __name__ == '__main__':
    app.run(debug = True, port = 5001)    