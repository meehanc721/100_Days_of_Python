from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
from datetime import date

API_KEY = "suckalemon"
API_SEARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie/"
MOVIE_INFO_ENDPOINT = "https://api.themoviedb.org/3/movie/"
IMAGE_API_URL = "https://image.tmdb.org/t/p/w500/"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class EditForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

#Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-10-movies.db'
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Create Table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=False)
db.create_all()

# new_movie = Movie(
#     title="Pulp Fiction",
#     year=1994,
#     description="Q tarantino does lots of crazy shit with a cool cast.",
#     rating=9.9,
#     ranking=3,
#     review="That is a tasty burger.",
#     img_url="https://wallpapercave.com/wp/wp7665395.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    edit_form = EditForm()
    movie_id = request.args.get('id')
    movie_selected = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        #Update record
        movie_selected.rating = edit_form.rating.data
        movie_selected.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return  render_template("edit.html", movie=movie_selected, form=edit_form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    # delete record
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_to_search = add_form.title.data
        response = requests.get(url=API_SEARCH_ENDPOINT, params={"api_key": API_KEY, "query": movie_to_search})
        search_data = response.json()
        return render_template("select.html", search_results=search_data["results"])
    return render_template("add.html", form=add_form)


@app.route("/find")
def find_movie_details():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_info_api = f"{MOVIE_INFO_ENDPOINT}{movie_api_id}"
        response = requests.get(url=movie_info_api, params={"api_key": API_KEY})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            img_url=f"{IMAGE_API_URL}{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('rate_movie', id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=False)
