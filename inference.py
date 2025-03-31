import json
import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

with open("energy_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/invocations', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = np.array(data['features'])
    predictions = model.predict(input_data)
    return jsonify({"predictions": predictions.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)