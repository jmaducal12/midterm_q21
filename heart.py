from flask import Flask, jsonify, request

app = Flask(__name__)

heart_info = [
    {"heart_id": "1", "date": "04/15/2021", "heart_rate": "85bpm"},
    {"heart_id": "2", "date": "04/19/2022", "heart_rate": "110bpm"},
    {"heart_id": "3", "date": "04/23/2022", "heart_rate": "92bpm"},
]


@app.route("/heart_info", methods=['GET'])
def getHearts():
    return jsonify(heart_info)


@app.route("/heart_info", methods=['POST'])
def add_hearts():
    heart = request.get_json()
    heart_info.append(heart)
    return {'id': len(heart_info)}, 200


@app.route('/heart_info/<int:index>', methods=['DELETE'])
def delete_heart(index):
    heart_info.pop(index)
    return 'The heart rate has been deleted', 200


if __name__ == "__main__":
    app.run()