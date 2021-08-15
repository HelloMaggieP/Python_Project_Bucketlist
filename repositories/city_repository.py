import re
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

#NOT TESTED
# # select all cities
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['film_locations'], row['country_id'], row['id'])
        cities.append(city)
    return cities

#NOT TESTED
# #select one city
# def select(id):
#     city = None
#     sql = "SELECT * FROM cities WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)

#     if result is not None:
#         city = City(result['name'], result['film_locations'], result['country_id'], result['id'])
#     return city

#NOT TESTED
# #delete city
# def delete(id):
#     sql = "DELETE FROM cities where id = %s"
#     values = [id]
#     run_sql(sql,values)

# #delete all cities
# def delete_all():
#     sql = "DELETE FROM cities"
#     run_sql(sql)