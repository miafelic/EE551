# EE551 Final Project: TweeterBot 

We created a Twitter bot (@TweeterBot2021) by using Tweepy and OpenWeatherMap API

# HOW TO RUN
## Notes before starting
- You will need to generate your own API keys
  - Instructions for Twitter API: https://realpython.com/twitter-bot-python-tweepy/#using-tweepy
  - Instructions for OpemWeatherMap API: https://openweathermap.org/api
- Once you get your API keys, replace them in the APIkeys.py file accordingly
## 1. Clone this repository
## 2. Paste the following commands to the terminal (We used Linux)
```
$ cd EE551
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install tweepy
$ pip install requests
$ pip freeze > requirements.txt
```
## 3. Now that the virtual environment is running, run the command
```
$ python tweet.py
```
## Demo
![Demo](https://i.imgur.com/WGqOM16.jpeg)
