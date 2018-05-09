import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

#def main():
#    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
#    for flight in flights:
#        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")
def main():
    books = db.execute("SELECT isbn, title, author, year FROM books").fetchall()
    for book in books:
        print(f"{book.isbn}, title: {book.title}, author: {book.author}, publication year: {book.year}.")


if __name__ == "__main__":
    main()
