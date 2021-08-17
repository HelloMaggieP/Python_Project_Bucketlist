from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.country_repository as country_repo

#save cities 
def save(city):
    sql = "INSERT INTO cities (name, film_locations, country_id, visited) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [city.name, city.film_locations, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

#NOT TESTED
# # select all cities
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['film_locations'], row['country_id'],row['id'],row['visited'])
        cities.append(city)
    return cities

#NOT TESTED
# #select one city
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        city = City(result['name'], result['film_locations'], result['country_id'], result['visited'])
    return city

#NOT NEEDED DELETE WHEN SURE ITS NOT NEEDED
def select_visited():
    cities =[]

    sql = "SELECT * FROM cities WHERE visited = True"
    results = run_sql(sql)

    for row in results:
        country = country_repo.select(row['country_id'])
        city = City(row['name'], row['film_locations'], country, row['visited'], row['id'])
        cities.append(city)
    return cities

# DON"T NEED THIS FUNCTIONALITY I DONT THINK 
# def countries(city):
#     countries = []

#     sql = "SELECT cities.* FROM cities INNER JOIN countries ON countries.id = cities.country_id WHERE countries.id = %s"
#     values = [city.country_id]
#     results = run_sql(sql, values)

#     for row in results:
#         country = Country(row['name'], row['id'])
#         countries.append(country)
        
#     return countries

# #delete city
def delete(id):
    sql = "DELETE FROM cities where id = %s"
    values = [id]
    run_sql(sql,values)

# #delete all cities
def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)