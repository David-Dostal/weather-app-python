import json
import weather_api
import geocoding_api
from genson import SchemaBuilder


def get_program_json_structure():
    """ Updates program's JSON structure to the API one"""
    with open('program_json_data.json', 'w') as f:
        lat, lon = geocoding_api.get_coordinates_for_place("Brno")
        data = weather_api.get_weather(lat, lon)
        json.dump(data, f)
    with open('program_json_data.json', 'r') as f:
        with open('program_json_structure.json', 'w') as f2:
            builder = SchemaBuilder()
            data = json.load(f)
            builder.add_object(data)
            json.dump(builder.to_schema(), f2)


def test_json_compatibility():
    """ Tests, whether the current JSON structure is compatible with the API structure"""
    with open('api_json_data.json', 'w') as f:
        lat, lon = geocoding_api.get_coordinates_for_place("Brno")
        data = weather_api.get_weather(lat, lon)
        json.dump(data, f)
    with open('api_json_data.json', 'r') as f:
        with open('api_json_structure.json', 'w') as f2:
            builder = SchemaBuilder()
            data = json.load(f)
            builder.add_object(data)
            json.dump(builder.to_schema(), f2)
    with open('program_json_structure.json', 'r') as f:
        schema = json.load(f)
    with open('api_json_structure.json', 'r') as f:
        instance = json.load(f)
    # validating, whether the current API format is compatible
    if schema != instance:
        print("Program's JSON structure is not compatible with the API JSON structure")
        exit()
    else:
        print("Program's JSON structure is compatible with the API JSON structure")
