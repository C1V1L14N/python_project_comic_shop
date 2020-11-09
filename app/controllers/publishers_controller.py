from flask import Flask, render_template, request, redirect, Blueprint
from models.publisher import Publisher
import repositories.publisher_repository as publisher_repository

publishers_blueprint = Blueprint("publishers", __name__)

@publishers_blueprint.route("/publishers")
def show_all():
    publishers = publisher_repository.select_all()
    return render_template('publishers/index.html', publishers = publishers)