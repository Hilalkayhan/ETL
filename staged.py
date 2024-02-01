import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Import the 'harmonized_df' DataFrame from the 'harmonized' module
from harmonized import harmonized_df

# Define the database connection URL
database_url = 'sqlite:///weather_data.db'

# Define a function to stage the data into SQL tables
def stage_data_to_sql(harmonized_df, database_url):
    # Create a SQLAlchemy engine
    engine = create_engine(database_url)

    # Staging the data into an SQL table
    harmonized_df.to_sql('weather_data', con=engine, index=False, if_exists='replace')

stage_data_to_sql(harmonized_df, database_url)

sql_query = 'SELECT * FROM weather_data'

engine = create_engine(database_url)

# Read the staged data from the SQL table into a DataFrame
staged_data_from_sql = pd.read_sql(sql_query, con=engine)

# Print the resulting DataFrame
print(staged_data_from_sql)

# Visualize the data using Matplotlib
plt.plot(staged_data_from_sql['date'], staged_data_from_sql['temperature'], label='Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Over Time')
plt.legend()
plt.show()
