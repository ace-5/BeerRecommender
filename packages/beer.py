import json
import random
from math import floor

import requests

url = 'https://api.punkapi.com/v2/beers'

def random_beer(no_of_suggestion):
    """Returns random beer suggestions. Total number of beer to be suggested is eual to integer value passed as no_of_suggestion"""
    no_of_suggestion = floor(no_of_suggestion)
    returnThis = []
    for i in range (no_of_suggestion):
        returnThis.append(i)
        returnThis[i] = dict()
        response = requests.get(url+'/random')
        data = json.loads(response.text)
        returnThis[i]['name'] = data[0]['name']
        returnThis[i]['tagline'] = data[0]['tagline']
        returnThis[i]['description'] = data[0]['description']
    
    return returnThis

def get_specified_beer(abv_get, abv_lt):
    y = suggest_beer(no_of_suggestion=20, abv_get = abv_get, abv_lt= abv_lt)
    random.shuffle(y)
    return_this = []
    print("SUGGESTION BASED ON YOUR CHOICE")
    for i in range(3):
        return_this.append(json.dumps(y[i], indent=2))
    return return_this

def get_random_beer():
    x = random_beer(3)
    print("RANDOM BEER SUGGESTION")
    return_this = []
    for i in range(3):
        return_this.append(json.dumps(x[i], indent=2))
    return return_this

def suggest_beer(no_of_suggestion=1, abv_get=5, abv_lt= 9):
    """Parameters: no_of_suggestion = Returns firstNumber of beer that you'd like to be suggested\n
                    \t\t\t\tagv_get = Returns all beers with ABV greater than then supplied number\n
                    \t\t\t\tagv_lt = Returns all beers with ABV greater less then supplied number\n
    ABV = Alcohol by Volume"""
    returnThis= []
    params = {
        'per_page':no_of_suggestion,
        'abv_get': abv_get,
        'abv_lt': abv_lt
    }

    response = requests.get(url=url, params=params)
    data  = json.loads(response.text)
    for i in range(no_of_suggestion):
        returnThis.append(i)
        returnThis[i] = {}
        returnThis[i]['name'] = data[i]['name']
        returnThis[i]['tagline'] = data[i]['tagline']
        returnThis[i]['description'] = data[i]['description']
    return returnThis
