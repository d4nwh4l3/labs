import requests

API_KEY = "DEMO_KEY"
BASE_URL = "https://api.nasa.gov/planetary/apod"

def fetch_apod(date=None):
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")
