from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for="rotate">Rotate By: 
                <input type="text" value="0" name="rot"/>
            </label>
            <textarea name="text">{0}</textarea>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():

    content = form

    return form.format(content)

@app.route("/", methods=(['POST']))
def encrypt():

    encrypt_text = rotate_string(request.form['text'], int(request.form['rot']))

    return '<h1>' + form.format(encrypt_text) + '</h1>'

app.run()