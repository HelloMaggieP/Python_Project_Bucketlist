from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repo

countries_blueprint = Blueprint("countries", __name__)

# all countries 
@countries_blueprint.route("/countries")
def countries():
    countries = country_repo.select_all()
    return render_template("countries/index.html", countries = countries)

# new country
#get country
# post country



#delete country
# @countries_blueprint.route("countries/<id>/delete", methods = ['POST'])
# def delete_country(id):
#     country_repo.delete(id)
#     return redirect('/countries')