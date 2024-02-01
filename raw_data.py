import requests
import json

api_key = "api_key"
lat = 59.3293  # Latitud för Stockholm
lon = 18.0686  # Longitud för Stockholm

#Construct the URL for the Openweatherdata API request
url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json"

# Make an HTTP GET request to the Openweatherdata API
response = requests.get(url, headers={'Authorization': f'Token {api_key}'})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    #Save the raw forecast data to a JSON file
    with open('raw_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print("Data sparad som raw_data.json")

else:
    #Print an error message if the request was not successful
    print(f"Error: {response.status_code}, {response.text}")


