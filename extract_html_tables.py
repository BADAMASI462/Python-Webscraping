# WEB SCRAPING

# Extracting tables from websites
# First, install the required libraries:
# pip install pandas
# pip install lxml

import pandas as pd  

# Use pd.read_html() to fetch tables from a website
table = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')

# Get the number of tables found on the page
num_tables = len(table)

# Extract the first table (index 0) from the list of tables
first_table = table[0]
print(first_table)

# Extracting CSV files from websites
# To read a CSV file from a website, use pd.read_csv() with the file's URL
csv_data = pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E0.csv')

# Rename columns in the dataframe (e.g., 'FTHG' to 'home' and 'FTAG' to 'away')
csv_data.rename(columns={'FTHG': 'home', 'FTAG': 'away'}, inplace=True)
