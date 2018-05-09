import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    reviews = db.relationship("Review", backref="book", lazy=True)

    def add_review(self, comment):
        r = Review(comment=comment, book_isbn=self.isbn)
        db.session.add(r)
        db.session.commit()

class Review (db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    comment= db.Column(db.String, nullable=False)
    #what column its going to reference:
    books_isbn = db.Column(db.String, db.ForeignKey("books.isbn"), nullable=False)
    users = db.relationship("User", backref="user", lazy=True)

    def add_user(self, comment):
        u = User(comment=comment, review_id=self.id)
        db.session.add()
        db.session.commit()
#    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

class User (db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    comment= db.Column(db.String, nullable=False)
    review_id = db.Column(db.String, db.ForeignKey("reviews.id"), nullable=False)

