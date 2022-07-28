import os
from flask import Flask, render_template
from twilio.rest import Client
from weather import get_weather
from space import space
from hp import get_hp

app = Flask('app')

@app.route('/')
def start():
  return render_template('index.html')

@app.route('/sms')
def message():
  account_sid = os.environ['sid']
  auth_token = os.environ['auth']

  #get data
  weather = get_weather('sudbury')
  sp = space()
  hp = get_hp()
  
  # creating log file
  message_log = f"Hello Krishno! The temperature in your city is {weather} degrees celcius. Please note the number of people in space today is {sp}. Today you will be visited by {hp}. Good day!\n"
  
  f = open("log.txt", "a") #logging
  f.write(message_log)
  f.close()


  
  client = Client(account_sid, auth_token)
  message = client.messages \
                  .create(
                       body=f"Hello Krishno! The temperature in your city is {weather} degrees celcius. Please note the number of people in space today is {sp}. Today you will be visited by {hp}. Good day!",
                       from_='+19377125751',
                       to='+16475427243'
                   )
  print(message.sid)
  if message.sid != "":
    msg = 'sms sent successfully'
    return render_template('smssent.html',msg=msg)
  else:
    msg = 'there was a problem'
    return render_template('smssent.html',msg=msg)


app.run(host='0.0.0.0', port=8080)