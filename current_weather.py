from pywebio.output import *
import pywebio
import wa_menu
import user_input_functions as uif


def current_weather_function():
    pywebio.output.clear()  # clears the main menu page
    wa_menu.main_menu_button()
    params = uif.get_actual_params()
    if not params:
        pywebio.output.popup("Error", "Nezadán žádný parametr k zobrazení")
        wa_menu.main_menu()
    else:
        place, weather_data = uif.get_weather_data()
        query = structure_query(weather_data, params)
        popup_current_weather(place, query)


def structure_query(weather_data, params):
    """ Structures weather data into a list of commands based on the user's specified parameters"""
    query = []
    if "Obrázek" in params:
        query.append((put_row([
            put_text('Aktuální počasí'),
            put_image(f'https://openweathermap.org/img/w/{weather_data["current"]["weather"][0]["icon"]}.png')
        ], size='80%')))
    if "Teplota" in params:
        query.append(
            put_row([put_text('Teplota'), put_text(str(weather_data['current']['temp']) + ' C')], size='80%'), )
    if "Pocitová teplota" in params:
        query.append(
            put_row([put_text('Pocitová teplota'), put_text(str(weather_data['current']['feels_like']) + ' C')],
                    size='80%'), )
    if "Tlak vzduchu" in params:
        query.append(put_row([put_text('Tlak vzduchu'), put_text(str(weather_data['current']['pressure']) + ' hPa')],
                             size='80%'), )
    if "Vlhkost vzduchu" in params:
        query.append(put_row([put_text('Vlhkost vzduchu'), put_text(str(weather_data['current']['humidity']) + ' %')],
                             size='80%'), )
    if not params:
        query.append(put_row([put_text("Nebyly zadány žádné parametry.")]))
    return query


def popup_current_weather(place, query):
    """ Pop-ups a window with desired weather information """
    if not place:
        place = "Vaše lokace"
    title = "Počasí v lokaci: " + place
    popup(title, query)
    wa_menu.main_menu()
