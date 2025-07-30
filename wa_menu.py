from pywebio.output import *
import current_weather as cw
import future_weather as fw
import pywebio
from pywebio.session import run_js
import test_compatibility


def app_menu():
    """ Run this to update program's JSON structure """
    #test_compatibility.get_program_json_structure()
    """ Run this to check program's compatibility with weather API"""
    #test_compatibility.test_json_compatibility()
    main_menu()


def main_menu():
    pywebio.output.clear()
    put_text('Hlavní nabídka').style('color: Black; font-size: 50px')
    oc_api_option()
    show_copyright()


def oc_api_option():
    put_table([
        ['One click API funkce',
         put_button('Aktuální počasí v zadané lokaci', onclick=lambda: cw.current_weather_function()),
         put_button("Hodinová předpověd počasí pro následujících 48 hodin",
                    onclick=lambda: fw.hourly_weather()),
         put_button('Denní počasí pro následujících 7 dní', onclick=lambda: fw.daily_weather())
         ],
    ])


def main_menu_button():
    put_button("Zpátky", onclick=lambda: (run_js('window.location.reload()'), main_menu()))


def show_copyright():
    with use_scope('C'):
        put_text('Copyright 2022 by xdostal8 (PEF Mendelu)')
