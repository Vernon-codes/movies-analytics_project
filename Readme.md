# IMDb Top 250 Movies Analytics

![IMDb Logo](https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg)

## Project Overview
This project performs **exploratory data analysis (EDA)** and **visual analytics** on the IMDb Top 250 movies dataset. The goal is to extract insights about movie ratings, votes, durations, and trends over time.  

**Key Features:**  
- Cleaned and preprocessed dataset of IMDb Top 250 movies  
- Univariate, bivariate, and multivariate analysis  
- Time-based analysis (movies per decade, average ratings)  
- Advanced visualizations including word clouds, boxplots, and correlation heatmaps  
- Database integration with MySQL for storing the cleaned dataset  

---

## Table of Contents
1. [Dataset](#dataset)  
2. [Technologies](#technologies)  
3. [Setup](#setup)  
4. [Usage](#usage)  
5. [EDA and Visualizations](#eda-and-visualizations)  
6. [Database Integration](#database-integration)  
7. [Project Structure](#project-structure)  
8. [License](#license)  

---

## Dataset
- Source: IMDb Top 250 movies dataset (scraped From Internet movie database)  
- Columns include:  
  - `Title` – Movie name  
  - `Year` – Release year  
  - `Rating` – IMDb rating  
  - `Votes` – Number of votes  
  - `Duration` – Movie length in minutes   
  - `Age_limit` – Age rating (G, PG, PG-13, R…)  

---

## Technologies
- Python 3.10+  
- Pandas & NumPy – Data manipulation  
- Matplotlib & Seaborn – Visualization  
- SQLAlchemy & MySQL Connector – Database integration  
- dotenv – Environment variable management
- Jupyter Notebook - Data Cleaning and EDA

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/Vernon-codes/movies-analytics_project.git
cd movies_analytics_project
```
### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4.Configure environment variables
```bash
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_DB=imdb_top250
MYSQL_PORT=3306
```
### 5.Usage
- Run EDA Notebook

## Project Structure
```
movies-analytics_project/
│
├── data/
│ ├── cleaned/
│ │ └── cleaned_imdb_top250.csv
│ └── raw/
│ ├── imdb_top_250_movies.csv
│ └── movies.csv
│
├── notebooks/
│ └── EDA_ANALYSIS.ipynb
│
├── scripts/
│ ├── api_fetch.py
│ ├── db_operations.py
│ └── scrapper_imdb.py
│
├── venv/
│
├── .env
├── LICENSE
├── README.md
└── requirements.txt
```
## LICENSE
- This project is licensed under the [MIT License](https://github.com/Vernon-codes/movies-analytics_project/blob/main/LICENSE) – see the LICENSE file for details.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## Acknowledgements
- IMDb Top 250 Movies Dataset
- Python libraries: Pandas, Seaborn, Matplotlib
- Learnings from documentation

## Author
- Name: Vernon Alva
- Email: codewithvernon@gmail.com
- GitHub: [Vernon-codes](https://github.com/Vernon-codes)



