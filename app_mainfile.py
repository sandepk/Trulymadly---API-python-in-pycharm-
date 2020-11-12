from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

app.debug = True


# @app.before_request
# def before():
#     return "TrulyMadly requests you to enter your name"


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    file = open('C:\\Users\\lappy\\Desktop\\TrulyMadly\\projects\\flaskProject\\data.json', 'r')
    json_input = file.read()
    print(json_input)
    return jsonify(processed_text)


@app.route('/persons/')
def persons():
    return "PersonsList"


if __name__ == '__main__':
    app.run()
