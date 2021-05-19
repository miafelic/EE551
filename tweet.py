import tweepy, requests, json, random, datetime
from newJersey import cities
from APIkeys import *
from datetime import datetime

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
newJerseyCity = random.choice(cities)


def postTweet():
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
   CITY = newJerseyCity
   API_KEY = OWM_API_KEY
   UNITS = "imperial"

   URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=" + UNITS
   response = requests.get(URL)
   
   if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      # getting the main dict block
      main = data['main']
      # getting temperature
      temperature = main['temp']
      temp_max = main['temp_max']
      temp_min = main['temp_min']
      # getting the humidity
      humidity = main['humidity']
      # getting the pressure
      pressure = main['pressure']
      # weather report
      report = data['weather']
   else:
      print("Error in the HTTP request")

   if (report[0]['id'] >= 200 and report[0]['id'] <= 232):
      emoji = "\U000026C8"
   elif (report[0]['id'] >= 300 and report[0]['id'] <= 531):
      emoji = "\U0001F327"
   elif (report[0]['id'] >= 600 and report[0]['id'] <= 622):
      emoji = "\U0001F328"
   elif (report[0]['id'] >= 700 and report[0]['id'] <= 781):
      emoji = "\U0001F32B"
   elif (report[0]['id'] >= 801 and report[0]['id'] <= 804):
      emoji = "\U00002601"
   else:
      emoji = "\U0001F31E"

   endl = "\n"
   now = datetime.now()
   dt_string = now.strftime("[%b-%d-%Y %H:%M:%S]")
   api.update_status(dt_string + endl + endl +
     "Weather forecast for " + newJerseyCity + endl + f"\U0001F321 Temperature: {temperature}°F (H: {temp_max}°F L:{temp_min}°F)" + endl + f"\U0001F4A7 Humidity: {humidity}%" + endl + emoji + f" Report: {report[0]['description']}")

postTweet()
