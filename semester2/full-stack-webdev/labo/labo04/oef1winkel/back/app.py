from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # dit zorgt ervoor dat ik straks geen CORS errors krijg


dictStock = {100: {'naam': 't-shirt', 'prijs': 18},
             101: {'naam': 'pull', 'prijs': 22},
             102: {'naam': 'koffie tas', 'prijs': 11}
             }


@app.route('/')
def hello_world():
    return 'ga naar de API url'


@app.route('/api/v1/products', methods=['GET'])
def products():
    return jsonify(dictStock), 200


@app.route('/api/v1/payment', methods=['POST'])
def payment():
    aantal = int(request.form['aantal'])
    product_id = int(request.form['product'])
    product = dictStock[product_id]
    prijs = int(product["prijs"])
    naam = product["naam"]
    totaal = prijs * aantal

    if aantal < 1 and product_id in dictStock.keys():
        return jsonify(status = "error"), 500
    else:
        return f"bestelling van {naam}: totale prijs: {totaal}", 201


if __name__ == '__main__':
    app.run()
