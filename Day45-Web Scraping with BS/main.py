from bs4 import BeautifulSoup
import requests

with open("top_100_movies_article.html") as web_file:
    web_html = web_file.read()

soup = BeautifulSoup(web_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
print(movies)

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")



