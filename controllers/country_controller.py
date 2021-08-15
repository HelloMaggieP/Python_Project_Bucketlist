from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repo
import repositories.city_repository as city_repo

countries_blueprint = Blueprint("countries", __name__)

# all countries 
@countries_blueprint.route("/countries")
def countries():
    countries = country_repo.select_all()
    return render_template("countries/index.html", countries = countries)

#calling countries and the cities attached to them. NOT wWORKING
@countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repo.select(id)
    cities = country_repo.cities(country)
    return render_template("countries/show.html", country = country, cities = cities)


# new country# route /countries/new
@countries_blueprint.route("/countries/new", methods = ['GET'])
def new_country():
    countries = country_repo.select_all()
    cities = city_repo.select_all()
    return render_template("countries/new.html", countries = countries, cities = cities)


# post country route /countries method post

#update / metho put 


#delete country
@countries_blueprint.route("/countries/<id>/delete", methods = ['POST'])
def delete_country(id):
    country_repo.delete(id)
    return redirect('/countries')