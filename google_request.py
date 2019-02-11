import json
import requests
import urllib
from urllib.parse import quote, urlencode

def get_coordinades(direccion, numero, comuna, ciudad, pais):

    api_token = 'AIzaSyDY3OH74rv5yLKz-z9-v2lYxjr-0BlH3WE'
    api_url_base = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    lugar = direccion + ',' + numero + ',' + comuna + ',' + ciudad + ',' + pais
    lugar = {'address': lugar}

    address = urlencode(lugar)

    key = {'key': api_token}
    key = urlencode(key)

    api_url_base += address + '&' + key

    response = requests.get(api_url_base)

    if response:
	       #print(response.status_code)
	        json_response = json.loads(response.content.decode('utf-8'))
	        return json_response['results'][0]['geometry']['location']
	                #for key,value in json_response.items():
	                   #	print("key: {key} | value: {value}".format(key=key, value=value))
    else:
	       print("Ups! Algo salio mal!!")
