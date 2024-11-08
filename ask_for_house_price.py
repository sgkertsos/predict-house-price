# Import libraries
import requests

# Variables
# The host where the price prediction service resides
url = 'http://127.0.0.1:9696/predict_house_price'

# A sample house
house = {
 'land_size_sqm': 100.0,
 'house_size_sqm': 85.0,
 'no_of_rooms': 1.0,
 'no_of_bathrooms': 1.0,
 'large_living_room': 0.0,
 'parking_space': 1.0,
 'front_garden': 0.0,
 'swimming_pool': 0.0,
 'distance_to_school': 1.6,
 'wall_fence': 0.0,
 'house_age': 6.0,
 'water_front': 0.0,
 'distance_to_supermarket': 0.7,
 'crime_rate_index': 0.29,
 'room_size': 1.0
 }

# Send request to web service
price =  requests.post(url, json=house).json()

# Show price
print(price)