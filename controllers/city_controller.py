from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repo
import repositories.country_repository as country_repo
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

@cities_blueprint.route("/cities/<id>/delete")
def delete_city(id):
    city_repo.delete(id)
    return redirect("/cities")

@cities_blueprint.route("/cities/new", methods = ['GET'])
def new_entry():
    countries = country_repo.select_all()
    cities = city_repo.select_all()
    return render_template("cities/new.html", countries = countries, cities = cities)

#NOT TESTED IF WORKING
@cities_blueprint.route("/cities", methods = ['POST'])
def create_entry():
    country = request.form['country']
    city = request.form['city']
    film_locations = request.form['film_locations']
    country = country_repo.select(country)
    city = city_repo.select(city)
    new_entry = City(city, film_locations, country)
    country_repo.save(new_entry)
    return redirect("/cities")