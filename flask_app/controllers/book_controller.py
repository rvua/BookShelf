from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.author import Author
from flask_app.models.book import Book

#=========================
# Main Page / Dashboard 
#=========================
@app.route("/books")
def books():
    all_books = Book.get_books_with_authors()
    return render_template("books.html", all_books = all_books)

#=========================
# Create Routes 
#=========================
@app.route("/books/new")
def new_book():
    authors = Author.get_all_authors()
    return render_template("new_book.html", authors = authors)

@app.route("/create_book", methods=["POST"])
def create_book():
    data = {
         "title": request.form['title'],
         "pages": request.form['pages'],
         "language": request.form['language'],
         "author_id": request.form['author_id'],
         "description": request.form['description'],
     }
    Book.create_book(data) 
    return redirect("/books")