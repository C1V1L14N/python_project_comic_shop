from flask import Flask, render_template, request, redirect, Blueprint
from models.comic import Comic
from models.publisher import Publisher
import repositories.comic_repository as comic_repository
import repositories.publisher_repository as publisher_repository

comic_blueprint = Blueprint("comics", __name__)

@comic_blueprint.route('/comics/add_comic')
def comic_form():
    publishers = publisher_repository.select_all()
    return render_template('comics/add_comic.html', publishers = publishers)

@comic_blueprint.route('/comics', methods=['POST'])
def add():
    name = request.form['name']
    author = request.form['author']
    genre = request.form['genre']
    wholesale_price = request.form['wholesale_price']
    markup = request.form['markup']
    stock_count = request.form['stock_count']
    min_count = request.form['min_count']
    out_of_stock = request.form['out_of_stock']
    publisher_id = request.form['publisher_id']
    publisher = publisher_repository.select(publisher_id)
    comic = Comic(name, author, genre, wholesale_price, markup, stock_count, min_count, out_of_stock, publisher)
    comic_repository.save(comic)
    return redirect('/comics/add_comic')


@comic_blueprint.route('/comics')
def show_all():
    comics = comic_repository.select_all()
    return render_template('comics/index.html', comics = comics)

@comic_blueprint.route('/comics/find_comic')
def find_form():
    return render_template('comics/find_comic.html')

@comic_blueprint.route('/comics', methods=['POST'])
def show_single(id):
    comic = comic_repository.select(id)
    return render_template('comics/index.html', comic = comic)



# def update_comic():


# def destroy():


