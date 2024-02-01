# Weather ETL Pipeline

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline for processing weather forecast data from various APIs. The goal is to harmonize the data, cleanse it, and stage it into an SQL database for further analysis and visualization.

## Project Structure

The project is organized into the following modules:

- `raw_data.py`: Downloads raw weather forecast data from an API and saves it as a JSON file.
- `harmonized.py`: Processes the raw data, harmonizes it into a structured format, and saves it as a JSON file.
- `cleansing.py`: Defines functions for cleaning the harmonized data.
- `staged.py`: Stages the cleansed data into an SQL table and provides a sample query for data retrieval.

## Usage

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Obtain API keys:

    - OpenWeatherData API key: [OpenWeatherMap API](https://openweathermap.org/api)
    - Other API keys as needed.

3. Run the pipeline:

    ```bash
    python raw_data.py
    python harmonized.py
    python cleansing.py
    python staged.py
    ```

4. View the results:

    - The cleansed data will be available in an SQL table named 'weather_data'.
    - Sample query results and data visualization will be printed.

## Configuration

- Replace placeholders for API keys in `raw_data.py` with your actual keys.
- Adjust parameters in the code, such as location coordinates, as needed.

