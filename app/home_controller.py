#-*- coding: utf-8 -*-
import flask, os
from flask import Flask, request, Markup, redirect, g, abort, flash,Blueprint
from flask.json import jsonify
from flask.templating import render_template
from flask.helpers import make_response

home = Blueprint('home', __name__, template_folder='templates', static_folder='static')

@home.route('/')
def index():
    # Do some stuff
    return render_template('home/index.html')