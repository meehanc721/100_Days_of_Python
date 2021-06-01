from flask import Flask, render_template
from datetime import date
import random
import requests

app = Flask(__name__)

@app.route('/')
def home():
    todays_date = date.today()
    return render_template("index.html", year=todays_date.year)

@app.route("/guess/<name>")
def guess(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    data = response.json()
    gender = data["gender"]
    return render_template("guess.html", name=name, gender=gender)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog.html", blog_posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)


