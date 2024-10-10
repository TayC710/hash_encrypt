from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
import uuid

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
