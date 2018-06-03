import os, sys, requests, time, json
from flask import Flask, request, send_from_directory, render_template
import numpy as np

sys.path.append("include")
import tools
from login import _login
_login_ = _login()
from getdata import _getdata
_getdata_ = _getdata()
from reg import _reg
_reg_ = _reg()

app = Flask(__name__, template_folder='site', static_url_path='')

#####################################################################
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/reg')
def reg():
    return render_template("reg.html")

@app.route('/account')
def account():
    return render_template("account.html")
### ------------------------------------------------------------- ###
@app.route('/doReg', methods=['GET','POST'])
def doReg():
    print("Regging: " + request.form['login'] + ", " + request.form['pass'])
    return _reg_.doReg(request.form['login'], request.form['pass'], request.form['fullname'], request.form['email'], request.form['phone'])

@app.route('/checkLogin', methods=['GET','POST'])
def checkLogin():
    print("Getting data: " + request.form['login'] + ", " + request.form['pass'])
    return _login_.checkUserLogin(request.form['login'], request.form['pass'])

@app.route('/getUserData', methods=['GET','POST'])
def getUserData():
    print("Getting data: " + request.form['login'] + ", " + request.form['pass'])
    return "ok"

@app.route('/getEID', methods=['GET','POST'])
def getEID():
    print("Getting data: " + request.form['login'])
    return _getdata_.getEID(request.form['login'])

@app.route('/myMoney', methods=['GET','POST'])
def myMoney():
    print("Getting data: " + request.form['login'])
    return _getdata_.myMoney(request.form['login'])

@app.route('/parseMyDays', methods=['GET','POST'])
def parseMyDays():
    #return _getdata_.parseDays(request.form['day'])
    _getdata_.doAll(request.form['day'])
#####################################################################

def Main():
	print("Starting UFS's System...")
	app.run(debug=True, port=777)

Main()