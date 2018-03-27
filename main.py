from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for="rotate">Rotate By: 
                <input type="text" value="{0}" id="rot" name="rot"/>
            </label>
            <textarea id="text" name="text"></textarea>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():

    content = form

    return content

@app.route("/", methods=(['POST']))
def encrypt():

    text = request.form['text']
    rot = int(request.form['rot'])

    encrypt = rotate_string(text, rot)

    return '<h1>', encrypt, '</h1>'

app.run()