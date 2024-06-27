import requests
import json
from datetime import datetime

def fetch_weather_data(city, api_key, save_path):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{save_path}/weather_data_{city}_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(data, f)
    return data  # Retourne les données pour le prétraitement

def preprocess_data(data):
    # Exemple de prétraitement simple
    preprocessed_data = {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "wind_deg": data["wind"]["deg"]
    }
    return preprocessed_data
