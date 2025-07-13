import pywebio
import wa_menu
import user_input_functions as uif
from pywebio import output
import graph
import api_data


def hourly_weather():
    """ Gets hourly weather data of the inputted city for the next 48 hrs """
    pywebio.output.clear()  # clears the main menu page
    wa_menu.main_menu_button()
    params = uif.get_future_params()
    if not params:
        output.popup("Error", "Nezadán žádný parametr k zobrazení")
        wa_menu.main_menu()
        return
    weather_data, loc = api_data.get_weather_data("hourly", params)
    show_locality(loc)
    graph.draw_graph(weather_data)


def daily_weather():
    """ Gets daily weather data of the inputted city for the next 8 days """
    pywebio.output.clear()  # clears the main menu page
    wa_menu.main_menu_button()
    params = uif.get_future_params()
    if not params:
        output.popup("Error", "Nezadán žádný parametr k zobrazení")
        wa_menu.main_menu()
        return
    weather_data, loc = api_data.get_weather_data("daily", params)
    show_locality(loc)
    graph.draw_graph(weather_data)


def show_locality(locality):
    pywebio.output.put_text(locality).style('color: Black; font-size: 35px')
