from repositories.DataRepository import DataRepository
from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
import time
import threading


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hier mag je om het even wat schrijven, zolang het maar geheim blijft en een string is'

socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)


# THREAD
# START een thread op. Belangrijk!!! Debugging moet UIT staan op start van de
# server, anders start de thread dubbel op
# werk enkel met de packages gevent en gevent-websocket. uninstall eerst eventlet en
# installeer gevent en gevent-socket
def all_out():
    print('*** thread gestart ***')
    while True:
        print('*** We zetten alles uit ***')
        DataRepository.update_status_alle_lampen(0)
        status = DataRepository.read_status_lampen()
        socketio.emit('B2F_alles_uit', {
                      'status': "lampen uit"}, broadcast=True)
        socketio.emit('B2F_status_lampen', {'lampen': status}, broadcast=True)
        time.sleep(10)

threading.Timer(10, all_out).start()

# API ENDPOINTS
@app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."


# SOCKET IO
@socketio.on('connect')
def initial_connection():
    print("A new client connected")
    status = DataRepository.read_status_lampen()
    socketio.emit('B2F_status_lampen', {'lampen': status})


@socketio.on('F2B_switch_light')
def switch_light(payload):
    DataRepository.update_status_lamp(
        payload["lamp_id"], payload["new_status"])
    lamp = DataRepository.read_status_lamp_by_id(payload["lamp_id"])
    print(lamp)
    socketio.emit('B2F_verandering_lamp', {
                  'lamp': lamp['id'], 'status': lamp['status']})


if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0')
