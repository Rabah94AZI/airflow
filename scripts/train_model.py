import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model(data_path, model_path):
    # Chargez les données prétraitées
    data = pd.read_json(data_path)
    X = data[["temperature", "humidity", "pressure", "wind_speed", "wind_deg"]]
    y = data["target"]  

    # Entraînez un modèle de régression linéaire simple
    model = LinearRegression()
    model.fit(X, y)

    # Sauvegardez le modèle
    joblib.dump(model, model_path)
