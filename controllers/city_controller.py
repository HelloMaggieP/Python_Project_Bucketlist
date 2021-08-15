from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repo

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repo.select_all()
    return render_template("cities/index.html", cities = cities)

@cities_blueprint.route("/cities/<id>")
def show(id):
    city = city_repo.select(id)
    country = city_repo.countries(city)
    return render_template("cities/show.html", city=city, country=country)
