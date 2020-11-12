from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/person/')
def hello():
    return jsonify(dict(name='Sandeep', address='India'))


@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))


# @app.before_request
# def before():
#     print('This is executed before each request.')


@app.route('/teapot/')
def teapot():
    # a = input('Enter name')
    # print(a)
    return "Would you like some tea?"


app.run()
