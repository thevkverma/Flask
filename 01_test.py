from flask import Flask

app = Flask(__name__)


@app.route('/hello', methods = ['GET', 'POST'])
def hello_world():
    print("Hello World")
    return "Say hello to yourself as Vivek Kumar Verma"

@app.route('/print', methods = ['GET', 'POST'])
def printing_msg():
    return "print something about me"
if __name__=='__main__':
    app.run(debug=True, port=5000)