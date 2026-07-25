
from flask import Flask, render_template, request
from scrappers.amazon_scraper import amazon_scraper_data
from scrappers.book_scraper import book_data
from scrappers.mutual_funds import get_data
from scrappers.jsonplaceholder_api import get_posts
from scrappers.worldpopulation import get_population_data
from scrappers.fakestore import get_products
from scrappers.TVMaze import get_shows
from scrappers.currency_api import get_currency
from scrappers.books_dynamic import get_books
from scrappers.imdb_dynamic import get_movies
from scrappers.youtube_dynamic import get_videos
from scrappers.github_trending import get_repositories
from scrappers.netflix_dynamic import get_netflix
from scrappers.universities_api import get_universities
from math import ceil
from flask import redirect, url_for

import requests

from scrappers.mutual_funds import get_data
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/portfolio")
def portfolio():
   return render_template("portfolio.html")
@app.route("/learnmore")
def learnmore():
   return render_template("learnmore.html")
@app.route("/minor1")
def minor1():
   return render_template("minor1.html")
@app.route("/minor2")
def minor2():
   return render_template("minor2.html")
@app.route("/major")
def major():
   return render_template("major.html")
@app.route("/webscraping")
def webscraping():
   return render_template("webscraping.html")
@app.route("/staticscraping")
def staticscraping():
   return render_template("staticscraping.html")
@app.route("/amazonscraping")
def amazonscraping():
    products = amazon_scraper_data()
    print(products)          
    print(len(products))     
    return render_template("amazonscraping.html",products=products)
@app.route("/bookscraping")
def bookscraping():
    books = book_data()
    return render_template("bookscraping.html",books=books)
@app.route("/mutual_funds")
def mutual_funds():
    scraped_data = get_data()
    return render_template("mutual_funds.html", data=scraped_data)
@app.route("/worldpopulation")
def worldpopulation():
    data = get_population_data()
    return render_template("worldpopulation.html", data=data)
@app.route("/apiscraping")
def apiscraping():
    return render_template("apiscraping.html")

@app.route("/jsonplaceholder-api")
def jsonplaceholder_api():
    posts = get_posts()
    return render_template("jsonplaceholder_api.html", data=posts )
@app.route("/fakestore")
def fakestore():
    products = get_products() 
    return render_template("fakestore.html",products=products )

@app.route("/universities")
def universities():
    data = get_universities()
    return render_template("universities.html", data=data)
@app.route("/tvmaze")
def tvmaze():
    data = get_shows()
    return render_template("TVMaze.html", data=data)

@app.route("/currency-api")
def currency_api():
    data = get_currency()
    return render_template("currency_api.html", data=data)
    url = "https://api.frankfurter.app/latest?from=USD&to=INR,EUR,GBP,JPY,AUD,CAD"
@app.route("/dynamicscraping")
def dynamicscraping():
    return render_template("dynamicscraping.html")

@app.route("/books_dynamic")
def books_dynamic():

    books = get_books()


    return render_template(
        "books_dynamic.html",
        books=books,
        total_books=len(books)
    )

@app.route("/refresh_books")
def refresh_books():

    return redirect(
        url_for("books_dynamic")
    )
@app.route("/imdb_dynamic")
def imdb_dynamic():
    movies = get_movies()
    return render_template("imdb_dynamic.html",movies=movies)
@app.route("/youtube_dynamic")
def youtube_dynamic():
    videos = get_videos()
    return render_template(
        "youtube_dynamic.html",
        videos=videos
    )
@app.route("/github_trending")
def github_trending():

    repositories = get_repositories()

    return render_template(
        "github_trending.html",
        repositories=repositories
    )
@app.route("/netflix_dynamic")
def netflix_dynamic():

    movies=get_netflix()

    return render_template(
        "netflix_dynamic.html",
        movies=movies
    )
@app.route("/myinternshipjourney")
def myinternshipjourney():
    return render_template("myinternshipjourney.html")
@app.route('/notebook')
def notebook():

    return render_template('notebook.html')

if __name__ == "__main__":
    app.run(debug=True, port=5002)

