# Imports
from flask import Flask, request, jsonify
import random
from flask_cors import CORS


# Custom imports
from repositories.DataRepository import DataRepository

# Start app
app = Flask(__name__)
CORS(app)


endpoint = '/api/v1'


# BACKEND - NIET WIJZIGEN!!
# Deze route wordt gebruikt voor het ophalen van de genres in de keuzelijst
@app.route(endpoint + '/elementen', methods=['GET'])
def get_elementen():
    if request.method == 'GET':
        s = DataRepository.read_elements()
        return jsonify(s), 200


@app.route(endpoint + '/elementen/<elementen_id>', methods=['GET'])
def get_element(elementen_id):
    if request.method == 'GET':
        s = DataRepository.read_element_by_atomicnumber(elementen_id)
        return jsonify(s), 200


@app.route(endpoint + '/elementen/types/<type_id>', methods=['GET'])
def get_elementen_by_type(type_id):
    if request.method == 'GET':
        s = DataRepository.read_elements_by_type(type_id)
        return jsonify(s), 200


@app.route(endpoint + '/types', methods=['GET'])
def get_types():
    if request.method == 'GET':
        s = DataRepository.read_types()
        return jsonify(s), 200


# Start app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
