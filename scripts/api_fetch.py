import os # for environment variables  
#We use os to interact with the computer in a safe and flexible way—so our Python programs
#can read/write files, get system info, and work with environment variables without breaking on different systems.
import requests # for making HTTP requests
#Requests is a Python library that makes it easy to send HTTP requests and handle responses,
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file 
load_dotenv() # go read the env file and load the variables into the environment
api_key=os.getenv('OMDB_API_KEY') # get the value of the API_KEY variable from the environment
p={'apikey':api_key,}
movies=['The Shawshank Redemption','The Godfather','The Dark Knight','Pulp Fiction','Forrest Gump']
important_features=['Title','Year','Rated','Released','Runtime','Genre','Language','Country','Awards','imdbID','Type']
all_movies_titles=[]
for title in movies:
    p={'apikey':api_key,'t':title,'important_features':important_features}
    response=requests.get('https://www.omdbapi.com/',params=p)
    if response.status_code == 200:
        data = response.json()
        # Filter only the important features
        filtered_data = {k: data.get(k, None) for k in important_features}
        all_movies_titles.append(filtered_data)
    else:
        print(f"Error fetching data for {title}: {response.status_code}")
df=pd.DataFrame(all_movies_titles)
print(df)
# df.to_csv('movies.csv',index=False)

#important features
# 1.title 
# 2.year
# 3.rated
# 4.released
# 5.Runtime
# 6.type
# 7.genre
# 8.country
# 9.language
