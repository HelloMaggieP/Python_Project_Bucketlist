from db.run_sql import run_sql
from models.country import Country
from models.city import City
import repositories.city_repository as city_repo

def save(country):
    sql = "INSERT INTO countries ( name ) VALUES ( %s ) RETURNING id"
    values = [country.name]
    results = run_sql(sql,values)
    country.id = results[0]['id']
    return country 

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['id'])
    return country

#calling countries and the cities attached to them. WORKING
def cities(country):
    cities = []

    sql = "SELECT cities.* FROM cities INNER JOIN countries ON countries.id = cities.country_id WHERE countries.id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['film_locations'], row['country_id'], row['visited'])
        cities.append(city)

    return cities

def update(country):
    sql = "UPDATE countries SET name = %s WHERE id = %s"
    values = [country.name, country.id]
    run_sql(sql, values)

#WORKS BUT NOT WRITTEN TEST FOR THIS - DO NOT NEED FOR MVP
# def delete_all():
#     sql = "DELETE FROM countries"
#     run_sql(sql)

