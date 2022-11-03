import time
import flask
from flask import Flask, request, redirect, url_for, session, escape, jsonify
import os, subprocess
import base64
from random import *
import os.path
import requests
from bs4 import BeautifulSoup as bs 
import os.path 
import json 
import random
import mysql.connector

app = flask.Flask(__name__)
#app.config["DEBUG"] = True
connection = mysql.connector.connect(host='127.0.0.1',database='1011db',user='nee',password='password')

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
def initboi(hostname):
    hostname = str(hostname)
    try:
        mySql_insert_query = "INSERT INTO windows (hostname) VALUES ('{}') ".format(hostname)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/windows/upd/<hostname>/password_hashes/<value>')
def password_hashesboi(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE windows set password_hashes='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/windows/upd/<hostname>/startup_applications/<value>')
def startup_applicationsboi(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE windows set startup_applications='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/windows/upd/<hostname>/autoruns/<value>')
def autorunsboi(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE windows set autoruns='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/windows/upd/<hostname>/scheduled_tasks/<value>')
def scheduled_tasksboi(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE windows set scheduled_tasks='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/windows/upd/<hostname>/user_accounts/<value>')
def user_accountsboi(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE windows set user_accounts='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/windows/upd/<hostname>/active_connections/<value>', methods=['POST'])
def active_connectionsboi(hostname, value):
    hostname = str(hostname)
    value = str(value)
    headers = flask.request.headers
    data = flask.request.data
    # insertValue = base64.b64decode(value).decode('utf-8')
    insertValue = base64.b64decode(data.decode('utf-8'))
    try:
        mySql_insert_query = "UPDATE windows set active_connections='{}' where hostname='{}'".format(data.decode('utf-8'), hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/windows/upd/<hostname>/command_history/<value>')
def command_historyboi(hostname, value):
    hostname = str(hostname)
    value = str(value)
    headers = flask.request.headers
    data = flask.request.data
    insertValue = base64.b64decode(value).decode('utf-8')
    # insertValue = base64.b64decode(data.decode('utf-8'))
    try:
        mySql_insert_query = "UPDATE windows set command_history='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/windows/upd/<hostname>/nondefault_services/<value>', methods=['POST'])
def nondefault_servicesboi(hostname, value):
    hostname = str(hostname)
    value = str(value)
    headers = flask.request.headers
    data = flask.request.data
    # insertValue = base64.b64decode(value).decode('utf-8')
    insertValue = base64.b64decode(data.decode('utf-8'))
    try:
        mySql_insert_query = "UPDATE windows set nondefault_services='{}' where hostname='{}'".format(data.decode('utf-8'), hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/windows/upd/<hostname>/network_config/<value>')
def network_configboi(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE windows set network_config='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"


############################################################################################################################
@app.route('/api/linux/init/<hostname>')
def initboi2(hostname):
    hostname = str(hostname)
    try:
        mySql_insert_query = "INSERT INTO linux (hostname) VALUES ('{}') ".format(hostname)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/linux/upd/<hostname>/password_hashes/<value>')
def password_hashesboi2(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE linux set password_hashes='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/linux/upd/<hostname>/command_history/<value>')
def command_historyboi2(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE linux set command_history='{}' where hostname='{}'".format(value, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/linux/upd/<hostname>/network_config/<value>')
def network_configboi2(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE linux set network_config='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/linux/upd/<hostname>/crontab_entries/<value>')
def crontab_entriesboi2(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE linux set crontab_entries='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/linux/upd/<hostname>/user_accounts/<value>')
def user_accountsboi2(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE linux set user_accounts='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/linux/upd/<hostname>/active_connections/<value>')
def active_connectionsboi2(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE linux set active_connections='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"

@app.route('/api/linux/upd/<hostname>/last_logins_ssh/<value>')
def last_logins_sshboi2(hostname, value):
    hostname = str(hostname)
    value = str(value)
    insertValue = base64.b64decode(value).decode('utf-8')
    try:
        mySql_insert_query = "UPDATE linux set last_logins_ssh='{}' where hostname='{}'".format(insertValue, hostname) 
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        return("Failed: {}".format(error))
    return "DABALYOU"


app.run(host='0.0.0.0', port=6969)