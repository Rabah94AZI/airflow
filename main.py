import requests
import json
from datetime import datetime
import os

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def fetch_weather_data(city, api_key, save_path):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        filename = f"{save_path}/weather_data_{city}_{timestamp}.json"
        with open(filename, 'w') as f:
            json.dump(data, f)
        return filename
    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")
        return None

if __name__ == "__main__":
    config_file = "key.json"
    config = load_config(config_file)
    city = config['city']
    api_key = config['api_key']
    save_path = config['save_path']
    
    fetch_weather_data(city, api_key, save_path)
