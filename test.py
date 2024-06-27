import os

api_key = os.getenv('api_wether')

if api_key:
    print(f"API Key: {api_key}")
else:
    print("API Key not found!")