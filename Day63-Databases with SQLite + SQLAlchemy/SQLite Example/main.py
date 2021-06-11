import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#SQLite version###########################
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'JK Rowling', '9.5')")
# db.commit()

#SQLAlchemy version

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
#
# db.create_all()

# new_book = Book(title="Bananas", author="Harambe Monke", rating=8)
# db.session.add(new_book)
# db.session.commit()

all_books = db.session.query(Book).all()
print(all_books)

# book = Book.query.filter_by(title="How to Poo").first()
# print(book.author)

# book_to_update = Book.query.filter_by(title="How to Poo").first()
# book_to_update.title = "How to Drop a Huge Shit"
# db.session.commit()

# book_id = 2
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Fuck Your Mother"
# db.session.commit()

book_id = 3
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()