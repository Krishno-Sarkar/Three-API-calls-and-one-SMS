import urllib.request
import json

def space():
  url = 'http://api.open-notify.org/astros.json'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  number = result['number']
  
  return number