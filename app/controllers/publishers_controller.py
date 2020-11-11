from flask import Flask, render_template, request, redirect, Blueprint
from models.publisher import Publisher
import repositories.publisher_repository as publisher_repository

publishers_blueprint = Blueprint("publishers", __name__)

@publishers_blueprint.route("/publishers")
def show_all():
    publishers = publisher_repository.select_all()
    return render_template('publishers/index.html', publishers = publishers)

@publishers_blueprint.route('/publishers/add_publisher')
def publisher_form():
    publisher = publisher_repository.select_all()
    return render_template('publishers/add_publisher.html', publisher = publisher)

@publishers_blueprint.route('/publishers', methods=['POST'])
def add_publisher():
    name = request.form['name']
    publisher = Publisher(name)
    
    publisher_repository.save(publisher)
    return redirect('/publishers/add_publisher')


@publishers_blueprint.route("/publishers/<id>/delete", methods=['POST'])
def delete(id):
    publisher_repository.delete(id)
    return redirect('/publishers')


@publishers_blueprint.route('/publishers/find_publisher')
def find_publisher():
    return render_template('/publishers/find_publisher.html')




@publishers_blueprint.route("/publishers/find_publisher_result", methods=['post'])
def publisher_by_name():
    name = request.form['publisher']
    publisher = publisher_repository.find_single_publisher(name)
    print(publisher)
    return render_template('publishers/find_publisher_result.html', publisher = publisher)


@publishers_blueprint.route('/publishers/<id>/edit_publisher')
def edit_form(id):
    publisher = publisher_repository.select(id)
    return render_template('publishers/edit_publisher.html', publisher = publisher)

@publishers_blueprint.route('/publishers/<id>', methods=["POST"])
def update_publisher(id):
    name = request.form['edit_publisher']
    publisher = Publisher(name)
    publisher_repository.update(publisher)
    return redirect('/publishers')
