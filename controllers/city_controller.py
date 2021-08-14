from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repo

    cities_blueprint = Blueprint("countries", __name__)