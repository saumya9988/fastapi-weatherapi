import requests
from app.core.config import settings

def get_coordinates(city_name: str):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={settings.OPENWEATHERMAP_API_KEY}"
    geo_response = requests.get(geo_url)

    if geo_response.status_code != 200 or not geo_response.json():
        return None, None

    geo_data = geo_response.json()[0]
    return geo_data["lat"], geo_data["lon"]

def get_weather_data(city_name: str):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city_name}&units=metric&appid={settings.OPENWEATHERMAP_API_KEY}"
    )
    response = requests.get(url)
    print("Weather API URL:", url)
    print("Status:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:
        return None

    data = response.json()
    try:
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except (KeyError, IndexError) as e:
        print("Parsing error:", e)
        return None
