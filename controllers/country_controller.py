from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
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


# new country# route /countries/new NOT TESTED
@countries_blueprint.route("/countries/new", methods = ['GET'])
def new_country():
    countries = country_repo.select_all()
    return render_template("countries/new.html", countries = countries)

# CREATE Country
# POST/countries
@countries_blueprint.route("/countries/new", methods = ['POST'])
def create_country():
    country = request.form['country']
    new_country = Country(country) 
    country_repo.save(new_country)
    return redirect("/countries")

#GET Country
@countries_blueprint.route("/countries/<id>/edit")
def edit_countries(id):
    country = country_repo.select(id)
    return render_template('countries/edit.html', country=country)

#POST Country
@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name = request.form['country']
    updated_country = Country(name, int(id))
    country_repo.update(updated_country)
    return redirect("/countries")



#Functionlity not needed for MVP
# @countries_blueprint.route("/countries/<id>/delete", methods = ['POST'])
# def delete_country(id):
#     country_repo.delete(id)
#     return redirect('/countries')