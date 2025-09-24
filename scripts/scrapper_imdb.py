from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Path to Edge WebDriver
edge_driver_path = "C:\\Users\\vernon\\Downloads\\edgedriver_win64\\msedgedriver.exe"

# Create service object
service = Service(edge_driver_path)

# Launch Edge browser
driver = webdriver.Edge(service=service)

url = 'https://www.imdb.com/chart/top/?ref_=hm_nv_menu'
driver.get(url)
time.sleep(3)  # Wait for the page to load

movie_titles = []
years = []
ratings = []
runtimes = []
condition=[]
votes=[]

# Each movie is inside <li class="ipc-metadata-list-summary-item">
movies = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

for movie in movies:
    # get movie title
    title = movie.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text
    movie_titles.append(title)

    # get year
    spans = movie.find_elements(By.CSS_SELECTOR, "span.cli-title-metadata-item")
    year = spans[0].text if spans else "N/A"
    years.append(year)

    # get runtime
    runtime = spans[1].text if len(spans) > 1 else "N/A"
    runtimes.append(runtime)

    #get condition
    cond=movie.find_elements(By.CSS_SELECTOR, "span.sc-15ac7568-7.cCsint.cli-title-metadata-item")
    condition.append(cond[2].text if len(cond) > 2 else "N/A")

    # get rating safely
    try:
        rating = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text
    except:
        rating = "N/A"
    ratings.append(rating)

    v=movie.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--voteCount')
    votes.append(v.text if v else "N/A")

driver.quit()

# Create dataframe
df = pd.DataFrame({
    "Movie_title": movie_titles,
    "Year": years,
    "Ratings": ratings,
    "Runtime": runtimes,
    "Age_limit": condition,
    "Votes": votes
})

print(df.head())
print(len(df))


df.to_csv('imdb_top_250_movies.csv', index=False)