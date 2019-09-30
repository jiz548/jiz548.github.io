from flask import Flask, render_template, url_for, request, redirect, flash
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

