import os
import urllib.request
import json

api = os.environ['api']

def get_weather(city):

  url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  #print(result)
  temp_c = round(result['main']['temp']-273.15,2)
  return temp_c