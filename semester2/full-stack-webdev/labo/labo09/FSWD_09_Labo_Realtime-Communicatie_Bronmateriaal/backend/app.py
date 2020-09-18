from flask_socketio import SocketIO
from repositories.DataRepository import DataRepository
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, date

# Start app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsASecretKey'

# stel CORS in op routes en socket
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

# Custom endpoint
endpoint = '/api/v1'


# ROUTES
@app.route('/')
def info():
    return jsonify(info='Please go to the endpoint ' + endpoint)


@app.route(endpoint + '/progress/today', methods=["DELETE"])
def progress_today():
    data = DataRepository.delete_total_progress(date.today())
    print('Data is :', data)
    socketio.emit('B2F_clear', {'amount': 0})
    return jsonify(info='wissen gelukt'), 200


@app.route(endpoint + '/progress', methods=["GET"])
def get_progress():
    data = DataRepository.read_logging()
    print('Data is :', data)
    return jsonify(data), 200

# # SOCKET.IO EVENTS
@socketio.on('connect')
def initial_connection():
    print("A new connection opened")
    # send to the client
    data = DataRepository.read_total_progress(date.today())
    if data['amount']:
        previous_progress = data['amount']
    else:
        previous_progress = 0
    socketio.emit('B2F_connected', {'currentProgress': previous_progress})


@socketio.on('F2B_new_logging')
def addProgress(json):
    new_amount = json['amount']
    row_inserted = DataRepository.create_log(datetime.now(), new_amount)
    if row_inserted > 0:
        print("hoeveelheid succesvol toegevoegd: ", new_amount)
        socketio.emit('B2F_addProgress', {'amount': new_amount})

# START THE APP
if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
