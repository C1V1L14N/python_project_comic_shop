from flask import Flask, render_template, request, redirect, Blueprint
from models.comic import Comic
from models.publisher import Publisher
import repositories.comic_repository as comic_repository
import repositories.publisher_repository as publisher_repository
import pdb

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


@comic_blueprint.route('/comics/by_name/find_comic_result', methods=['POST'])
def show_single():
    name = request.form['name']
    comic = comic_repository.find_single_comic(name)    
    return render_template('comics/find_comic_result.html', comics = [comic])

@comic_blueprint.route('/comics/by_publisher/find_comic_result', methods=['POST'])
def comics_by_publisher():
    publisher_name = request.form['publisher']
    
    comics = comic_repository.find_comics_by_publisher(publisher_name)
    publishers = publisher_repository.select_all()    
    return render_template('comics/find_comic_result.html', publishers = publishers, comics = comics)



@comic_blueprint.route('/comics/<id>/edit_comic')
def edit_comic(id):
    comic = comic_repository.select(id)
    publishers = publisher_repository.select_all()
    return render_template('comics/edit_comic.html', comic = comic, publishers = publishers)


@comic_blueprint.route('/comics/<id>', methods=["POST"])
def update_comic(id):
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
    comic = Comic(name, author, genre, wholesale_price, markup, stock_count, min_count, out_of_stock, publisher, id)
    comic_repository.update(comic)
    return redirect('/comics')


@comic_blueprint.route("/comics/<id>/delete", methods=['POST'])
def delete(id):
    comic_repository.delete(id)
    return redirect('/comics')


