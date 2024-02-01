import pandas as pd

def clean_data(harmonized_df):
    # Handling missing values
    harmonized_df = harmonized_df.fillna(0)

    # Convert 'temperature', 'air_pressure', and 'precipitation' columns to numeric
    harmonized_df['temprature'] = pd.to_numeric(harmonized_df['temperature'], errors='coerce')
    harmonized_df['air_pressure'] = pd.to_numeric(harmonized_df['air_pressure'], errors='coerce')
    harmonized_df['precipitation'] = pd.to_numeric(harmonized_df['precipitation'], errors='coerce')

    # Drop duplicate rows
    harmonized_df = harmonized_df.drop_duplicates()

    return harmonized_df  # Add this line to return the modified DataFrame

if __name__ == "__main__":
    # Read harmonized data from the 'harmonized_data.json' file
    harmonized_json_path = 'harmonized_data.json'
    harmonized_df = pd.read_json(harmonized_json_path, lines=True)

    # Clean the harmonized data using the 'clean_data' function
    cleaned_df = clean_data(harmonized_df)

    # Print a sample of the cleaned data
    print(cleaned_df.head())

    # Save the cleaned data to a new JSON file ('cleaned_data.json')
    cleaned_json_path = 'cleaned_data.json'
    cleaned_df.to_json(cleaned_json_path, orient='records', date_format='iso', lines=True)
