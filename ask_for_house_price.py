# Import libraries
import requests
import json

def predict_house_price(house):

    # The host where the price prediction service resides
    url = 'http://predict_service:9696/predict_house_price'

    # Send request to web service
    response = requests.post(url, json=house).json()

    # return house price
    # return(type(response))
    return(response['house_price'])