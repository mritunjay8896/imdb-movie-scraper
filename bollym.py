import pandas as pd
import requests
from bs4 import BeautifulSoup

file_path = 'bolly24.html'
with open(file_path, 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')


movies = [movie.get_text().strip() for movie in soup.find_all('h3', class_='ipc-title__text')]


years = [year.get_text().strip() for year in soup.find_all('span', class_='sc-300a8231-7') if year.get_text().strip().isdigit()]


movies_description = [desc.get_text().strip() for desc in soup.find_all('div', class_='ipc-html-content-inner-div')]


movies_image = [img.get('src').strip() for img in soup.find_all('img', class_='ipc-image') if img.get('src')]


durations = [duration.get_text().strip() for duration in soup.find_all('span', class_='sc-300a8231-7') if 'h' in duration.get_text() and 'm' in duration.get_text()]


min_length = min(len(movies), len(years), len(movies_description), len(movies_image), len(durations))

movies = movies[:min_length]
years = years[:min_length]
movies_description = movies_description[:min_length]
movies_image = movies_image[:min_length]
durations = durations[:min_length]


data = pd.DataFrame({
    'Movie Name': movies,
    'Year': years,
    
    'Image URL': movies_image,
    'Duration': durations  
})


data.to_excel('movie_data.xlsx', index=False)

print("Data has been successfully written to 'movie_data.xlsx'.")
