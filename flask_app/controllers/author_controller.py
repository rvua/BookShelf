from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.author import Author

@app.route('/new_author', methods=["POST"])
def new_author():
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
    }

    Author.create_author(data)
    return redirect('/books')