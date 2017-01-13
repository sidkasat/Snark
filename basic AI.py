# Weather API Key- 92a57da05bade1303dc604b93103e2bb
# Mapquest API Key- XowhqcVIUGYZwMapL48R1Su4TULO3cAw
# Irvine City -ID => 5257570
import http.client
import urllib.request
import urllib.parse
import json
import sys
import pyowm
import spotipy

sp=spotipy.Spotify()
owm=pyowm.OWM('92a57da05bade1303dc604b93103e2bb')
def weather():
    # Search for current weather in Irvine (USA)
    try:
        observation = owm.weather_at_place('Irvine,us')
        w = observation.get_weather()
        #print(w)                      # <Weather - reference time=2013-12-18 09:20,
                                      # status=Clouds>

        # Weather details
        print("Weather in Irvine, USA-")
        print("Wind Speed and Direction:",w.get_wind()['speed'],"mph and",w.get_wind()['deg'], "deg")                  # {'speed': 4.6, 'deg': 330}
        print("Humidity:",w.get_humidity()," %")
        print("Temperature(C):",w.get_temperature('celsius')['temp'], "C     Max Temp-",w.get_temperature('celsius')['temp_max'],"C       Min Temp- ",w.get_temperature('celsius')['temp_min'],"C")  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        return True
    except:
        print("Weather ERROR")
        return False
    
def joke():
    url='http://tambal.azurewebsites.net/joke/random'
    try:
        response=urllib.request.urlopen(url)
        x=response.read().decode()
        info=json.loads(x)
        print(info['joke'])
        return True
    except:
        print("Joke ERROR")
        return False
            
def quote():
    url='http://quotes.stormconsultancy.co.uk/random.json'
    try:
        response=urllib.request.urlopen(url)
        x=response.read().decode()
        info=json.loads(x)
        print("Quote by {}: {}".format(info['author'],info['quote']))
        return True
    except:
        print("Quote ERROR")
        return False

def songs():
    results = sp.search(q='weezer', limit=20)
    for ((i, t) in enumerate(results['tracks']['items'])):
        print (' ', i, t['name'])

     
hi= ['hi','hi!','hello','hello!','sup','wake up', 'whats up?',	'hi', 'howdy', 'hey', 'hiya', 'ciao', 'aloha']
bye= ['bye','cya','ttyl','later','later!','bye!','cya!']
weather_names= ['1','first','tell me the weather','what\'s the weather?','','weather', 'weather?','weather!','weather.']
joke_names=['3','joke','joke!','joke?','make me laugh']
quote_names=['5','quote','quote?','quote!','motivate me']
song_names=['songs','song','album','artist']


print("Hi! I am Allo-II, your personal assistant. How can I help you?")
while True:
    userInput= input()
    if userInput.lower() in hi:
        print("Hello!")
        print("I can do these stuff: \n\
              1) Find the weather for you in your location\n\
              2) Find directions to some place\n\
              3) Tell you a joke!!\n\
              4) Play a game with you?\n\
              5) Tell me a quote!\n\
              6) Songs by artist\n\
              6) More coming your way.\n\
              You can either select options or say whatever you want.\
              Eg: 'Tell me the weather' or '1'")
#Add different elifs to add more questions/ statements
    elif userInput.lower() in weather_names:
        x=weather()
        if not(x):
            print("Sorry couldn't connect! You can try something else for now?")
    elif userInput.lower() in joke_names:
        x=joke()
        if not(x):
            print("Sorry couldn't connect! You can try something else for now?")
    elif userInput.lower() in quote_names:
        x=quote()
        if not(x):
            print("Sorry couldn't connect! You can try something else for now?")
    elif userInput.lower() in bye:
        print("Bye!")
        break
    else:
        print("I did not understand what you said! Please try again") 




''' EXTRA STUFF/ OPTIONAL
############################     Weather URL        #########################
"""
    url='http://api.openweathermap.org/data/2.5/forecast/city?id=5257570&APPID=92a57da05bade1303dc604b93103e2bb'
    try:
        response=urllib.request.urlopen(url)
        x=response.read()
        print("X",x)
        info=json.loads(x)
        print(info)
        return True
    except:
        print("WEATHER ERROR ")
        return False"""
        
'''
