from flask import render_template,request
from application import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')