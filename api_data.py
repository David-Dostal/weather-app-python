import pytz
from datetime import datetime
import pandas as pd
import user_input_functions as uif


def get_weather_data(type_of_period, param):
    """ Cuts weather data by the desired time period(hourly,...) and parameters,
    then converts it into a readable list (through a panda format)  """
    place, weather_data = uif.get_weather_data()
    df = pd.json_normalize(weather_data[type_of_period])
    times = df["dt"]
    temps = []
    feel_temps = []
    pressures = []
    humids = []
    formatted_times = format_time(times)
    if type_of_period == "hourly":
        if "Teplota" in param:
            temps = df["temp"].tolist()
        if "Pocitová teplota" in param:
            feel_temps = df["feels_like"].tolist()
    if type_of_period == "daily":
        if "Teplota" in param:
            temps = df["temp.day"].tolist()
        if "Pocitová teplota" in param:
            feel_temps = df["feels_like.day"].tolist()
    if "Tlak vzduchu" in param:
        pressures = df["pressure"].tolist()
    if "Vlhkost vzduchu" in param:
        humids = df["humidity"].tolist()

    return [formatted_times, temps, feel_temps, pressures, humids], place


def format_time(times):
    formatted_times = []
    for dt in times.to_list():
        time_formatted = datetime.fromtimestamp(dt, pytz.timezone('Europe/Prague'))
        formatted_times.append(time_formatted.strftime("%a %H"))

    return formatted_times
