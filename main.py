from pywebio import start_server
import wa_menu

""" Starts the weather app server, initializes the app menu and tests, whether the used API is still compatible 
with this version of program 
 """
if __name__ == '__main__':
    start_server(wa_menu.app_menu, debug=True, port=5000)
