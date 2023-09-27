# Importing necessary libraries
from os import environ
from requests import get
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
api_key = environ.get('API_KEY')

# Define the URL for the Google Maps Distance Matrix API
url = "https://maps.googleapis.com/maps/api/distancematrix/json"

# Input the starting point, destination, fuel consumption per 100 kilometers and the price of gasoline
print('You have to input data in this way: "City, address"')
origin = input('Where do you start your journey? ')
destination = input('Where are you going? ')
consumption = float(input('How much fuel does your car burn (l/100 km/h? '))
price = float(input('What is the price of gasoline (zl)? '))

# Define the payload for the API request
payload = {
    'origins': origin,
    'destinations': destination,
    'key': api_key
}

# Make a GET request to the Google Maps Distance Matrix API
response = get(url, payload)

# Parse the JSON response
body = response.json()

# Extract the distance and duration from the API response
distance = body['rows'][0]['elements'][0]['distance']
duration = body['rows'][0]['elements'][0]['duration']

# Calculate the cost of the trip based on distance, fuel consumption, and gasoline price
cost = round(price * distance['value'] / 1000 * consumption / 100, 2)

# Print the cost of the trip rounded to two decimal places
print(f'The cost of the trip is: {cost} zl')