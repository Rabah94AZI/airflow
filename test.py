import os

api_key = os.getenv('API_KEY')

if api_key:
    print(f"API Key: {api_key}")
else:
    print("API Key not found!")
