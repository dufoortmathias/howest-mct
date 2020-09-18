from repositories.DataRepository import DataRepository
from flask import Flask, jsonify, request
from flask_cors import CORS

# Start app
app = Flask(__name__)
CORS(app)

# Custom endpoint
endpoint = '/api/v1'


# ROUTES
@app.route('/')
def index():
    return "PLEASE VISIT API ROUTE"


@app.route(endpoint+'/')
def api():
    return "Welcome to API"


@app.route(endpoint + '/bestemmingen', methods=['GET'])
def read_bestemmingen():
    data = DataRepository.read_bestemmingen()
    if data is not None:
        return jsonify(bestemmingen=data), 200
    else:
        return jsonify(status="error"), 404


@app.route(endpoint + '/treinen', methods=['GET', 'POST'])
def treinen():
    data = DataRepository.read_treinen()
    if request.method == 'GET':
        if data is not None:
            return jsonify(treinen=data), 200
        else:
            return jsonify(status="error"), 404
    elif request.method == 'POST':
        gegevens = DataRepository.json_or_formdata(request)
        print(gegevens)
        data = DataRepository.create_trein(
            gegevens['vertrek'],
            gegevens['bestemming'],
            gegevens['spoor'],
            gegevens['vertraging'],
            gegevens['afgeschaft']
        )
        return jsonify(treinid=data, bestemming=gegevens['bestemming'])
    else:
        return jsonify(message="wrong method")
    


@app.route(endpoint + '/treinen/<id>', methods=['GET', 'PUT', 'DELETE'])
def trein(id):
    if request.method == 'GET':
        data = DataRepository.read_trein(id)
        if data is not None:
            return jsonify(data), 200
        else:
            return jsonify(status="error"), 404
    elif request.method == 'PUT':
        gegevens = DataRepository.json_or_formdata(request)
        DataRepository.update_trein(
            gegevens['vertrek'],
            gegevens['bestemmingID'],
            gegevens['spoor'],
            gegevens['vertraging'],
            gegevens['afgeschaft'],
            id)
        return jsonify(trein_id = id), 200
    elif request.method == 'DELETE':
        data = DataRepository.delete_trein(id)
        if data > 0:
            return jsonify(row_count = data, status="success"), 200
        else:
            return jsonify(row_count = data, status="no update"), 200

@app.route(endpoint + '/treinen/<id>/vertraging', methods=['PUT'])
def update_trein_vertraging(id):
    gegevens = DataRepository.json_or_formdata(request)
    data = DataRepository.update_trein_vertraging(id, gegevens['vertraging'])
    return jsonify(data), 200


@app.route(endpoint + '/treinen/bestemming/<bestemmingid>', methods=['GET'])
def read_treinen_met_bestemming(bestemmingid):
    data = DataRepository.read_treinen_met_bestemming(bestemmingid)
    if data is not None:
        return jsonify(treinen=data), 200
    else:
        return jsonify(status="error"), 404


# Start app
if __name__ == '__main__':
    app.run(debug=True)
