from flask import Flask, request, jsonify, render_template
import berkas

app = Flask(__name__)

@app.route('/')
def main():
    return get_cab_names()

__cab_names = None
__data_columns = None
__model = None


@app.route('/get_cab_names', methods=['GET'])
def get_cab_names():
    berkas.load_saved_data()
    response = jsonify({
        'cab_names': berkas.get_cab_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_price', methods=['GET', 'POST'])
def predict_price():
    cab_name = request.form['cab_name']
    distance = float(request.form['distance'])
    surge_multiplier = float(request.form['surge_multiplier'])

    response = jsonify({
        'predicted_price': berkas.get_predicted_price(cab_name,distance,surge_multiplier)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


app.run()