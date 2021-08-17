from controllers.country_controller import countries
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


@cities_blueprint.route("/cities/new", methods = ['GET'])
def new_entry():
    countries = country_repo.select_all()
    cities = city_repo.select_all()
    return render_template("cities/new.html", countries = countries, cities = cities)


@cities_blueprint.route("/cities/new", methods = ['POST'])
def create_entry():
    country_id      = request.form['country_id']
    city            = request.form['city']
    film_locations  = request.form['film_locations']
    visited         = request.form['visited']
    country         = country_repo.select(country_id) 
    new_entry       = City(city, film_locations, country, visited)
    city_repo.save(new_entry)
    return redirect("/cities")

#GET/ EDIT 'cities/<id>/edit'
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_cities(id):
    city = city_repo.select(id)
    countries = country_repo.select_all()
    return render_template('cities/edit.html', city=city, countries = countries)

#UPDATE / PUT 'cities/<id>
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    country_id      = request.form['country_id']
    city            = request.form['city']
    film_locations  = request.form['film_locations']
    visited         = request.form['visited']
    country         = country_repo.select(country_id)
    updated_city    = City(city, film_locations, country, visited, int(id))
    city_repo.update(updated_city)
    return redirect("/cities")

@cities_blueprint.route("/cities/visited")
def select_visited():
    cities = city_repo.select_visited()
    return render_template("cities/show.html", cities = cities)

@cities_blueprint.route("/cities/not-visited")
def select_not_visited():
    cities = city_repo.select_not_visited()
    return render_template("cities/show.html", cities = cities)

@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repo.delete(id)
    return redirect("/cities")