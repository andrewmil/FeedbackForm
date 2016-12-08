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
			'service': request.json['service'],
			'dataType': request.json['dataType'],
			'period': request.json['period'],
			'rating_1': request.json['rating_1'],
			'rating_2': request.json['rating_2'],
			'rating_3': request.json['rating_3'],
			'rating_4': request.json['rating_4'],
			'rating_5': request.json['rating_5'],
			'total': request.json['total']
		}
		records.append(record)
		return jsonify({'satus': 'ok'}), 200
	else:
		return jsonify({'status': 'failed'}), 400
		
if __name__ == "__main__":
	app.run(host= '0.0.0.0')