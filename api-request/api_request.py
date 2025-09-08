import requests

api_key = "877ad01bfb7bc0405f1951612cfd1d36"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

# Uncomment before deloyment
# def fetch_data():
#     print("Fetching Weather data from weatherstack....")
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         print("API response successfully")
#         return print(response.json())
#     except requests.exceptions.RequestException as e:
#         print(f"Fetching failed: {e}")
#         raise

# fetch_data()

def mock_fetch_data(): 
    # return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-09-05 05:39', 'localtime_epoch': 1757050740, 'utc_offset': '-4.0'}, 'current': {'observation_time': '09:39 AM', 'temperature': 19, 'weather_code': 143, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0006_mist.png'], 'weather_descriptions': ['Mist'], 'astro': {'sunrise': '06:27 AM', 'sunset': '07:21 PM', 'moonrise': '06:30 PM', 'moonset': '03:43 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 91}, 'air_quality': {'co': '508.75', 'no2': '40.33', 'o3': '85', 'so2': '12.765', 'pm2_5': '17.575', 'pm10': '19.425', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 10, 'wind_degree': 228, 'wind_dir': 'SW', 'pressure': 1013, 'precip': 0, 'humidity': 90, 'cloudcover': 75, 'feelslike': 19, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}}
    return {
  "request": {
    "type": "City",
    "query": "New York, United States of America",
    "language": "en",
    "unit": "m"
  },
  "location": {
    "name": "New York",
    "country": "United States of America",
    "region": "New York",
    "lat": "40.714",
    "lon": "-74.006",
    "timezone_id": "America/New_York",
    "localtime": "2025-09-05 05:39",
    "localtime_epoch": 1757050740,
    "utc_offset": "-4.0"
  },
  "current": {
    "observation_time": "09:39 AM",
    "temperature": 19,
    "weather_code": 143,
    "weather_icons": [
      "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0006_mist.png"
    ],
    "weather_descriptions": [
      "Mist"
    ],
    "astro": {
      "sunrise": "06:27 AM",
      "sunset": "07:21 PM",
      "moonrise": "06:30 PM",
      "moonset": "03:43 AM",
      "moon_phase": "Waxing Gibbous",
      "moon_illumination": 91
    },
    "air_quality": {
      "co": "508.75",
      "no2": "40.33",
      "o3": "85",
      "so2": "12.765",
      "pm2_5": "17.575",
      "pm10": "19.425",
      "us-epa-index": "2",
      "gb-defra-index": "2"
    },
    "wind_speed": 10,
    "wind_degree": 228,
    "wind_dir": "SW",
    "pressure": 1013,
    "precip": 0,
    "humidity": 90,
    "cloudcover": 75,
    "feelslike": 19,
    "uv_index": 0,
    "visibility": 10,
    "is_day": "no"
  }
}