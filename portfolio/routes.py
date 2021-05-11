from flask import render_template, redirect, request
from portfolio import app

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    greeting = 'Welcome to My Portfolio Website'
    return render_template('/index.html', greeting=greeting)

@app.route('/aboutme', methods=['POST', 'GET'])
def aboutme():
    return render_template('aboutme.html')

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')