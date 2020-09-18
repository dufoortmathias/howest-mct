from repositories.DataRepository import DataRepository
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Custom endpoint
endpoint = '/api/v1'


@app.route('/')
def index():
    # kom ik op de route? Dan redirect ik naar /klanten
    return redirect(endpoint + '/klanten', code=302)


#########  Klanten  #########

@app.route(endpoint + '/klanten')
def klanten():
    if request.method == 'GET':
        data = DataRepository.read_klanten()
        # kan none returnen bij fout of geen records
        if data is not None:
            return jsonify(data), 200
        else:
            return jsonify(message="error"), 404
    elif request.method == 'POST':
        # haal de data op uit de request via de hulpfunctie
        gegevens = DataRepository.json_or_formdata(request)
        DataRepository.create_klant(
            gegevens['FNaam'],
            gegevens['VNaam'],
            gegevens['Straat'],
            gegevens['Nummer'],
            gegevens['Postcode'],
            gegevens['Gemeente']
        )


@app.route(endpoint + '/klanten/<id>', methods=['GET', 'PUT'])
def klant(id):
    if request.method == 'GET':
        # READ
        data = DataRepository.read_klant(id)
        if data is not None:
            return jsonify(data), 200
        else:
            return jsonify(message="error"), 404
    elif request.method == 'PUT':
        # UPDATE
        gegevens = DataRepository.json_or_formdata(request)
        data = DataRepository.update_klant(
            gegevens['FNaam'],
            gegevens['VNaam'],
            gegevens['Straat'],
            gegevens['Nummer'],
            gegevens['Postcode'],
            gegevens['Gemeente'],
            id
        )
        if data > 0:
            return jsonify(KlantID=id), 200
        elif data == 0:
            # geen fouten in sql maar alle data was identiek
            return jsonify(message="Geen aanpassingen"), 200
        else:
            # fouten in sql
            return jsonify(message="error"), 404
    elif request.method == 'DELETE':
        data = DataRepository.delete_klant(id)
        return jsonify(status=data), 200
    

#########  Bestemmingen  #########
@app.route(endpoint + '/bestemmingen')
def bestemmingen():
    if request.method == 'GET':
        data = DataRepository.read_bestemmingen()
        # kan none returnen bij fout of geen records
        if data is not None:
            return jsonify(data), 200
        else:
            return jsonify(message="error"), 404
    elif request.method == 'POST':
        # haal de data op uit de request via de hulpfunctie
        gegevens = DataRepository.json_or_formdata(request)
        DataRepository.create_bestemming(
            gegevens['Afkorting'],
            gegevens['Voluit'],
            gegevens['Land'],
            gegevens['TypeVlucht'],
        )
    else:
        return jsonify(message="wrong method")


@app.route(endpoint + '/bestemmingen/<id>', methods=['GET', 'PUT'])
def bestemming(id):
    if request.method == 'GET':
        # READ
        data = DataRepository.read_bestemming(id)
        if data is not None:
            return jsonify(data), 200
        else:
            return jsonify(message="error"), 404
    elif request.method == 'PUT':
        # UPDATE
        gegevens = DataRepository.json_or_formdata(request)
        data = DataRepository.update_bestemming(
            gegevens['Afkorting'],
            gegevens['Voluit'],
            gegevens['Land'],
            gegevens['TypeVlucht'],
            id
        )
        if data > 0:
            return jsonify(BestemmingID=id), 200
        elif data == 0:
            # geen fouten in sql maar alle data was identiek
            return jsonify(message="Geen aanpassingen"), 200
        else:
            # fouten in sql
            return jsonify(message="error"), 404
    elif request.method == 'DELETE':
        data = DataRepository.delete_bestemming(id)
        return jsonify(status=data), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
