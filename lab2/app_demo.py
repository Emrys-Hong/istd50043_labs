from flask import Flask, abort, jsonify, request
import json
import datetime

# setting up
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
	return {'greeting': 'have a nice day'}

@app.route('/hello/<name>', methods=['GET'])
def greet(name):
	return {'greeting': "Hello {}. Have a nice day".format(name)}

@app.route('/query', methods=['GET'])
def query():
	if not request.json or (not 'query' in request.json):
		return {'error': 'request not properly formatted'};
	
	msg = request.json['query']
	return {'result': 'query received', 'msg': msg}

@app.route('/insert', methods=['POST'])
def insert():
	if not request.json or (not 'data' in request.json):
		return {'error': 'request not properly formatted'};
	
	msg = request.json['data']
	return {'result': 'insert query received', 'data': msg}

app.run(debug=True, host="0.0.0.0")
