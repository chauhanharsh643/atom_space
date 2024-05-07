import urllib.request
import json

req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
response = urllib.request.urlopen(req)

obj = json.loads(response.read().decode('utf-8'))

def format_location(latitude, longitude, decimal_places=4):
    lat_str = "{:.{}f}".format(latitude, decimal_places)
    long_str = "{:.{}f}".format(longitude, decimal_places)
    return "Lat: {} and Long: {}".format(lat_str, long_str)

print(obj['timestamp'])

# storing lat and log inside a variable
latitude = float(obj['iss_position']['latitude'])
longitude = float(obj['iss_position']['longitude'])
formatted_location = format_location(latitude, longitude)
print(formatted_location)

