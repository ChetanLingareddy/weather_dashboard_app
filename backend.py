import os
import requests

api_key = os.getenv("Weather_app_API_key")

def get_data(place ,forecast_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    request = requests.get(url)
    data = request.json()
    filtered_data = data['list']
    filtered_data = filtered_data[:8 * forecast_days]
    if kind == "Temperature":
        filtered_data = [value["main"]["temp"] for value in filtered_data]
    if kind == "Sky":
        filtered_data = [value["weather"][0]["main"] for value in filtered_data]
    return filtered_data

if __name__ == "__main__":
    get_data(place="kansas", forecast_days=3, kind="Sky")




