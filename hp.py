import urllib.request
import json
import random

def get_hp():

  url = 'http://hp-api.herokuapp.com/api/characters'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  
  char = random.randint(1,99)
  
  #print(f"{result[char]['actor']}")
  actor = result[char]['actor']
  if result[char]['gender']=='female':
    return f"{actor} who is a female"
  else:
    return f"{actor} who is a male"