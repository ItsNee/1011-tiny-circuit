import time
import flask
from flask import Flask, request, redirect, url_for, session, escape, jsonify
import os, subprocess
import base64
import string
from random import *
import requests
from bs4 import BeautifulSoup as bs
import json
import random
import os.path
import requests 
from bs4 import BeautifulSoup as bs 
import os.path 
import json 
import random 

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

def api_key_check(apiKey):
    print(apiKey)
    validApiKeys = ["4E3473D72D60DB88FED0856034CE4A2A", "9038e7c65fef9dbb9d3adfd41e9d2550", "45fa0c8e9fc3a1d6d343541320f91cf5"]
    apiKeyStatus = any(apiKeyey in apiKey for apiKeyey in validApiKeys)
    if (apiKeyStatus == False):
        return '''<h1>Invalid API Key</h1>'''
    return "Welcome Slatt."



def hash_id(hash):
    badChars = ["&", "&&", "`", "``", "|", "||", ";", "os.", "\n", "0x0a", " "]
    hash = hash.decode("utf-8")
    for element in hash:
        print(element)
        badCheck = any(hashy in hash for hashy in badChars)
        if (badCheck == True):
            return '''<h1>I trusted u lol...</h1>'''
    out = subprocess.Popen("hashid -m '" + hash + "'", shell=True, stdout=subprocess.PIPE).stdout.read()
    #out = out.decode('utf-8')
    #return jsonify(out)
    return out


@app.route('/', methods=['GET'])
def home():
    return '''<h1>You Discovered TINYSHIT API!!</h1>
<p>-SLATT</p>'''

@app.route('/api', methods=['GET'])
def api():
    return '''<h1>Pls stop here :(</h1>
<p>Criezz</p>'''

@app.route('/api/4E3473D72D60DB88FED0856034CE4A2A/windows/upload/<b64>')
def detect_hash(b64):
    b64 = str(b64)
    b64 = base64.b64decode(b64)
    return b64

@app.route('/api/4E3473D72D60DB88FED0856034CE4A2A/domain2ip/<domain>')
def domain_2_ip(domain):
    domain = str(domain)
    domain = base64.b64decode(domain)
    return domain2Ip(domain)

@app.route('/api/instadp/<username>')
def instadp(username):
    username = str(username)
    username = base64.b64decode(username)
    return instadpp(username)

@app.route('/api/bd62bc7a3dcaae984c3a618854319a78/b00tme')
def bootPc():
    return bootMyPc()

@app.route('/api/v1/passwdGen')
def passwdGen():
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(11, 16)))
    return password

@app.route('/api/<apiKey>/hello/<text>')
def testFunction(apiKey, text):
    api_key_check(apiKey)
    apiKey = str(apiKey)
    text = str(text)
    return api_key_check(apiKey)

app.run(host='0.0.0.0', port=6969)