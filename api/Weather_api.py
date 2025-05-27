import os
import requests
from dotenv import load_dotenv, find_dotenv

# load api key
load_dotenv(".env", override=True)
weather_api_key = os.getenv('WEATHER_API_KEY')
opencage_api_key = os.getenv('OPENCAGE_API_KEY')

while True:
    # get variables of lat and lng
    city = input("Would you like to check the weather in which city?:").strip()
    if city.lower in ['quit','stop','exit']:
        print("👋 Goodbye!")
        break
    # Geocoding: Get lat/lon from city name
    opencage_url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={opencage_api_key}"
    opencage_response = requests.get(opencage_url)
    opencage_data = opencage_response.json()

    try:
        lat = opencage_data['results'][0]['geometry']['lat']
        lon = opencage_data['results'][0]['geometry']['lng']
    except (IndexError, KeyError):
        print("❌ City not found. Please try again.")
        continue

    # get weather information
    url = f"https://api.openweathermap.org/data/2.5/forecast?units=metric&cnt=1&lat={lat}&lon={lon}&appid={weather_api_key}"
    response = requests.get(url)
    data = response.json()
    try:
        temperature = data['list'][0]['main']['temp']
        description = data['list'][0]['weather'][0]['description']
        wind_speed = data['list'][0]['wind']['speed']
    except (KeyError, IndexError):
        print('Unable to fetch the data. Please try another city')
        continue

    # return imformation as output
    weather_string = f"""The current temperature of {city} is {temperature}°C. 
    It is currently {description},
    with a wind speed of {wind_speed}m/s.
    """

    print(weather_string)
