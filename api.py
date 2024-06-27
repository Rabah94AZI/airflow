from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Chargez le modèle
model = joblib.load("model.pkl")

@app.route('/predict', methods=['GET'])
def predict():
    temperature = float(request.args.get('temperature'))
    humidity = float(request.args.get('humidity'))
    pressure = float(request.args.get('pressure'))
    wind_speed = float(request.args.get('wind_speed'))
    wind_deg = float(request.args.get('wind_deg'))

    data = pd.DataFrame([[temperature, humidity, pressure, wind_speed, wind_deg]],
                        columns=["temperature", "humidity", "pressure", "wind_speed", "wind_deg"])
    prediction = model.predict(data)[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
