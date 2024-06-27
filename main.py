import requests
import json

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to get data: {response.status_code}, {response.text}")
        return None

if __name__ == "__main__":
    city = "Paris"
    api_key = "04021105db5527bbe09d188106e8418e"  
    data = fetch_weather_data(city, api_key)
    if data:
        print(json.dumps(data, indent=4))
