import os, sys, requests, time, json
from flask import Flask, request, send_from_directory, render_template
import numpy as np

app = Flask(__name__, template_folder='site', static_url_path='')

sys.path.append("include")
import tools
from login import _login
_login_ = _login()
from getdata import _getdata
_getdata_ = _getdata()
from reg import _reg
_reg_ = _reg()

##############################################
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/reg')
def reg():
    return render_template("reg.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/account')
def account():
    return render_template("account.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")
### -------------------------------------- ###
@app.route('/doReg', methods=['GET','POST'])
def doReg():
    print("Regging: " + request.form['login'] + ", " + request.form['pass'])
    return _reg_.doReg(request.form['login'], request.form['pass'], request.form['fullname'], request.form['valute'])

@app.route('/checkLogin', methods=['GET','POST'])
def checkLogin():
    print("Getting data: " + request.form['login'] + ", " + request.form['pass'])
    return _login_.checkUserLogin(request.form['login'], request.form['pass'])

@app.route('/getUserData', methods=['GET','POST'])
def getUserData():
    return json.dumps(_getdata_.getAllData(request.form['login']))

@app.route('/sendMoney', methods=['GET','POST'])
def sendMoney():
    return _getdata_.getMoney(request.form['login'])

@app.route('/changeValute', methods=['GET','POST'])
def changeValute():
    return _getdata_.changeUserValute(request.form['login'])
##############################################

def Main():
	print("Starting UFS's System...")
	app.run(debug=True, port=666)

Main()