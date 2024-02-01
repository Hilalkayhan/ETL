#Import necessary libraries
import json
import pandas as pd
from cleansing import clean_data
import matplotlib.pyplot as plt

# Read raw data from the 'raw_data.json' file
with open('raw_data.json', 'r') as json_file:
    raw_data = json.load(json_file)

time_series = raw_data.get('timeSeries', [])

# Define empty lists to store extracted data
dates = []
temperatures = []
air_pressures = []
precipitations = []

# Iterate through time series and extract data
for time_entry in time_series:
    date = pd.to_datetime(time_entry['validTime'])
    if date:

        dates.append(date)
        
        # Extract temperature data
        temperature_entry = next((param['values'][0] for param in time_entry['parameters'] if param['name'] == 't'), None)
        temperatures.append(temperature_entry)

        # Extract air pressure data
        air_pressure_entry = next((param['values'][0] for param in time_entry['parameters'] if param['name'] == 'msl'), None)
        air_pressures.append(air_pressure_entry)

        # Extract precipitation data
        precipitation_entry = next((param['values'][0] for param in time_entry['parameters'] if param['name'] == 'pmean'), None)
        precipitations.append(precipitation_entry)

# Create a dictionary to store the harmonized data
harmonized_data = {
    "date": dates,  
    "temperature": temperatures,
    "air_pressure": air_pressures,
    "precipitation": precipitations
}

# Create a DataFrame from the dictionary
harmonized_df = pd.DataFrame(harmonized_data)

# Save the harmonized data to a JSON file
harmonized_json_path = 'harmonized_data.json'
harmonized_df.to_json(harmonized_json_path, orient='records', date_format='iso', lines=True)

# Print a sample of the harmonized data
print(harmonized_df.head())

# Clean the harmonized data using the 'clean_data' function from the 'cleansing' module
cleaned_df = clean_data(harmonized_df)

# Visualize the data using Matplotlib
plt.plot(harmonized_df['date'], harmonized_df['temperature'], label='Temperature')
plt.plot(harmonized_df['date'], harmonized_df['air_pressure'], label='Air Pressure')
plt.plot(harmonized_df['date'], harmonized_df['precipitation'], label='Precipitation')
plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Harmonized Weather Data')
plt.legend()
plt.show()
