from flask_app import app
from flask import render_template, redirect, session, request


@app.route("/books")
def books():
    return render_template("books.html")