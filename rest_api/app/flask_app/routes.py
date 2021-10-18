from . import app
from flask import render_template,  url_for, flash, redirect, request, abort, session, make_response, jsonify
from datetime import datetime



@app.route("/", methods = ['GET','POST'])
def echo():
    if request.method == 'GET':
        text = ''
        msg = request.args.get('msg','')
        return render_template('page.html', method = 'get', msg = msg,text = text, timestamp = datetime.now())

    if request.method == 'POST':
        msg = ''
        text = request.form['text']
        return render_template('page.html', method = 'post', msg = msg,text=text, timestamp = datetime.now())


@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'),400
