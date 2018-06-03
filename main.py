import os, sys, requests, time, json
from flask import Flask, request, send_from_directory, render_template
import numpy as np

sys.path.append("include")
import tools


mainServer = Flask(__name__, template_folder='site/main', static_url_path='')
brokerServer = Flask(__name__, template_folder='site/broker', static_url_path='')

@mainServer.route('/')
@mainServer.route('/index')
def index():
    user = { 'username': '1' }
    return render_template("index.html")
    
@brokerServer.route('/')
@brokerServer.route('/index')
def index():
    user = { 'username': '1' }
    return render_template("index.html")

def Main():
	print("Starting Fintech System...")
	mainServer.run(port=80)
	brokerServer(port=81)

Main()

# 