from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.country_repository as country_repo

#save cities 
def save(city):
    sql = "INSERT INTO cities (name, film_locations, country_id) VALUES (%s, %s, %s) RETURNING id"
    values = [city.name, city.film_locations, city.country.id]
    results = run_sql(sql, values)
    city.id = results[0]['id']
    return city

# all cities

# new city
# get city
# post city


#delete city

#delete all cities
def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)