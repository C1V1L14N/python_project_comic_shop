from flask import FLASK, render_template, request, redirect, Blueprint
from models.comic import Comic
import repositories.comic_repository as comic_repository

comic_blueprint = Blueprint("comics", __name__)

