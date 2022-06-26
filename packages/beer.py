import requests
import json

url = 'https://api.punkapi.com/v2/beers'

def random(no_of_suggestion):
    """Returns random beer suggestions. Total number of beer to be suggested is eual to integer value passed as no_of_suggestion"""
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