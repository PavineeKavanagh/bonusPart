
from flask import render_template
from app import app
from systeminfo2.systeminfo2 import get_platform
@app.route('/')
def index():
	returnDict = {}
	returnDict['platform'] = get_platform()
	returnDict['title'] = 'Assignment2b'
	return render_template("index.html", **returnDict)