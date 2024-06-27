import os

api_key = os.getenv('API_KEY')

if api_key:
    print(f"API Key for our khra project : {api_key}")
else:
    print("API Key not found!")
