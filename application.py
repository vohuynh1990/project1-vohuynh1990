from flask import Flask, render_template, jsonify, request
from models import *
from flask_session import Session

import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)



@app.route("/")
def registration():
    return render_template("registration.html")


@app.route("/user", methods=["POST","GET"])
def user():
    if session.get("emails") is None:
        session["emails"] = []
    if request.method=="POST":
        email= request.form.get("email")
        session[user_id].append(email)
    #Password = request.form.get("pwd")
        return render_template("userinfo.html", emails=emails) #,password=pwd)

@app.route("/index")
def index():
    books = Book.query.all()
    #additional argument that the 1st variable books to be defined in index.htm to be equal to books in python file
    return render_template("index.html", books=books)

@app.route("/index/write", methods=["POST"])
def write():
    """Write a review."""

    # Get form information.
    comment = request.form.get("comment")
    try:
        book_isbn = int(request.form.get(book_isbn))
    except ValueError:
        return render_template("error.html", message="Invalid book isbn number.")

    # Make sure the book exists.
    book = Book.query.get(book_isbn)
    if not book:
        return render_template("error.html", message="No such book with that isbn.")

    # Add review.
    book.add_review(comment)
    return render_template("success.html")


@app.route("/books")
def books():
    """List all books."""
    books = Book.query.all()
    return render_template("books.html", books=books)


@app.route("/books/<string:book_isbn>")
def book(book_isbn):
    """List details about a single book."""

    # Make sure book exists.
    book = Book.query.get(book_isbn)
    if book is None:
        return render_template("error.html", message="No such book.")

    # Get all reviews.
    reviews = book.reviews
    return render_template("book.html", book=book, reviews=reviews)


@app.route("/api/books/<string:book_isbn>")
def book_api(book_isbn):
    """Return details about a single book."""

    # Make sure book exists.
    book = Book.query.get(book_isbn)
    if book is None:
        return jsonify({"error": "Invalid isbn"}), #404

    # Get all reviews.
    reviews = book.reviews
    comments = []
    for review in reviews:
        comments.append(review.comment)
    return jsonify({
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "reviews": comments
        })

