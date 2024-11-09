# import libraries
import pickle

import numpy as np

from flask import Flask
from flask import request
from flask import jsonify

# Variables
model_file='model.bin'

# Load model
with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# Create Flask app
app = Flask('predict_service')

# Create predict function
@app.route('/predict_house_price', methods=['POST'])
def predict():
    # Get house characteristics
    house = request.get_json()

    # Get house price prediction
    X_house = dv.transform([house])
    house_price = int(np.expm1(model.predict(X_house)[0]))

    result = {
        'house_price': house_price
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)