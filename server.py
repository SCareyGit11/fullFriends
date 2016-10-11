from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'notreally'

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mysql = MySQLConnector(app, 'email')
@app.route('/')


def index():
	query = "SELECT * FROM friendsdb"
	emails = mysql.query_db(query)
	print friends
	return render_template('index.html', all_friends=friends)
