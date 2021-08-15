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

@countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repo.select(id)
    # line here to show cities when working
    return render_template("countries/show.html", country = country)


# new country
#get country
# post country



#delete country
# @countries_blueprint.route("countries/<id>/delete", methods = ['POST'])
# def delete_country(id):
#     country_repo.delete(id)
#     return redirect('/countries')