import sys
from flask import Flask, render_template, request

from handlers import upload_csv_handler

app = Flask(__name__)
app.config.from_pyfile('config.py')

GET = 'GET'
POST = 'POST'


@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/upload", methods=[POST])
def upload_file():
    uploaded_file = request.files['File']
    return upload_csv_handler.get_counts(uploaded_file)

if __name__ == "__main__":
    app.run()
