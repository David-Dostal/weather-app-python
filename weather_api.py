import requests

appid = "your_api_key_here"  # Replace with your actual OpenWeatherMap API key


class WeatherAPIError(Exception):
    pass


def get_weather(lat: float, lon: float) -> dict:
    request_data = {
        "lat": lat,
        "lon": lon,
        "appid": appid,
        "units": "metric"
    }
    r = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=request_data)
    if r.status_code == 200:
        return r.json()
    else:
        raise WeatherAPIError()
