#!/usr/bin/python
from flask import Blueprint,render_template

appinfo = Blueprint('appinfo',__name__)

@appinfo.route('/appinfo')
def showAppInfo():
    return render_template('index.html')

