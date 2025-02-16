import os
import requests

# Stored api key locally
api_key = os.getenv("Weather_app_API_key")

def get_data(place ,forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    # Gets data and stores it in JSON format
    request = requests.get(url)
    data = request.json()
    # Since data gets updated every 3 hours, we have 8 data points for each day
    filtered_data = data['list']
    filtered_data = filtered_data[:8 * forecast_days]
    return filtered_data

if __name__ == "__main__":
    get_data(place="kansas", forecast_days=3)




