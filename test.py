
import requests
import json
import requests
import urllib
from urllib.parse import quote, urlencode


api_token = 'AIzaSyDY3OH74rv5yLKz-z9-v2lYxjr-0BlH3WE'
api_url_base = 'https://maps.googleapis.com/maps/api/geocode/json?address='
address = "Antonio+varas+880+providencia+santiago+chile"

key = {'key': api_token}
key = urlencode(key)
api_url_base += address + '&' + key

response = requests.get(api_url_base)


if response:
    json_response = json.loads(response.content.decode('utf-8'))
    print(json_response['results'][0]['geometry']['location'])
else:
    print("hello")