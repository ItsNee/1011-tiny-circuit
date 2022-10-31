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
import mysql.connector

app = flask.Flask(__name__)
#app.config["DEBUG"] = True
connection = mysql.connector.connect(host='localhost',database='1011db',user='nee',password='password')

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()


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

@app.route('/api/windows/init/<hostname>')
def detect_hash(hostname):
    hostname = str(hostname)
    mySql_insert_query = "INSERT INTO windows (hostname) VALUES ('{}') ".format(hostname)
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()
    return "DABALYOU"

app.run(host='0.0.0.0', port=80)