import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
user = os.getenv('MYSQL_USER')          # fixed typo
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')          # removed duplicate
data_base = os.getenv('MYSQL_DB')

# Create SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{data_base}")

# Load CSV
df = pd.read_csv('D:\\Development\\API_WEBSCRAPPING\\API_Web\\movies_analytics_project\\data\\raw\\imdb_top_250_movies.csv')
df_cleaned=pd.read_csv('D:\Development\API_WEBSCRAPPING\API_Web\movies_analytics_project\data\cleaned\cleaned_imdb_top_250_movies.csv')

# Insert into MySQL (table will be created automatically)
df.to_sql(name='movie', con=engine, if_exists='replace', index=False)
df_cleaned.to_sql(name='cleaned_movie', con=engine, if_exists='replace', index=False)
print("Data inserted successfully")

# Verify data insertion and read the data from mysql to pandas dataframe 
query_df = pd.read_sql("SELECT * FROM movie;", engine)
cleaned_query_df = pd.read_sql("SELECT * FROM cleaned_movie;", engine)

print(query_df.head())
print()
print()
print(cleaned_query_df.head())






