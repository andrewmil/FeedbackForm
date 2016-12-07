from flask import Flask, request, jsonify

app = Flask(__name__)

records=[]

@app.route("/")
def displayRecords():
	return jsonify({'records':records})

@app.route('/data/ONS/satisfaction', methods=['POST'])
def create_task():
	if request.headers['Content-Type'] == 'application/json' and request.headers['Authorization'] == 'Bearer abcdrandomtokenthings':
		record = {
			'_id': request.json['_id'],
			'_timestamp': request.json['_timestamp'],
			'very dissatisfied': request.json['very dissatisfied'],
			'dissatisfied': request.json['dissatisfied'],
			'neither': request.json['neither'],
			'satisfied': request.json['satisfied'],
			'very satisfied': request.json['very satisfied']
		}
		records.append(record)
		return jsonify({'satus': 'ok'}), 200
	else:
		return jsonify({'status': 'failed'}), 400
		
if __name__ == "__main__":
	app.run(host= '0.0.0.0')