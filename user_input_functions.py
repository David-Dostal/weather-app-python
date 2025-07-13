from weather_api import get_weather
from geocoding_api import get_coordinates_current_location
from geocoding_api import get_coordinates_for_place
from geocoding_api import get_place_per_coords
import pywebio.input as input1


def get_weather_data():
    """ Gets weather data of the inputted city """
    guiding_txt = "Lokace - Město (Nechte prázdné pro použití aktuální polohy)"
    user_input = input1.input_group('Počasí', [input1.input(guiding_txt, name='place')])
    place = user_input['place']
    if place:
        lat, lon = get_coordinates_for_place(place)
    else:
        lat, lon = get_coordinates_current_location()
        place = get_place_per_coords(lat, lon)
    return place, get_weather(lat, lon)


def get_actual_params():
    params = ["Obrázek", "Teplota", "Pocitová teplota", "Tlak vzduchu", "Vlhkost vzduchu"]
    return input1.checkbox("Zobrazit: ", options=params)


def get_future_params():
    params = ["Teplota", "Pocitová teplota", "Tlak vzduchu", "Vlhkost vzduchu"]
    return input1.checkbox("Zobrazit: ", options=params)
