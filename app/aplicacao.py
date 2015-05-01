#-*- coding: utf-8 -*-
import flask, os
from flask import Flask, request, Markup, redirect, g, abort, flash
from flask.json import jsonify
from flask.templating import render_template
import config
from flask.helpers import make_response
import datetime
#Blueprints
from home_controller import home

app = Flask(__name__)
app.config.from_pyfile("config.py")
email = config.settingEmail(app)
app.register_blueprint(home)

def run():
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port = port)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def detect_user_language():
	#Setando ano na variável global pega no meu pé
	g.ano = datetime.date.today().year