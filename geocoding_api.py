import requests
from geopy.geocoders import Nominatim


class PlaceNotFound(Exception):
    pass


def get_coordinates_for_place(place_name: str) -> tuple:
    geolocator = Nominatim(user_agent="weatherApp")
    location = geolocator.geocode(place_name)
    if location:
        return location.latitude, location.longitude
    else:
        raise PlaceNotFound(f"Location {place_name} not found")


def get_coordinates_current_location() -> tuple:
    r = requests.get("http://ip-api.com/json")
    return r.json()["lat"], r.json()["lon"]


def get_place_per_coords(lat, lon):
    geolocator = Nominatim(user_agent="weatherApp")
    location = geolocator.reverse(str(lat) + ", " + str(lon))
    address = location.address
    return address
