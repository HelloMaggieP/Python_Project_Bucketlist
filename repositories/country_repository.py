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



# def select_all(country):
#     countries = []

#     sql = "SELECT * FROM countries"
#     results = run_sql(sql)

#     for row in results:
#         country = Country(row['name'], row['id'])
#         countries.append(country)
#     return countries

# def select(id):
#     country = None
#     sql = "SELECT * FROM countries WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         country = Country(result['name'], result['id'])
#     return country


# new country
#get country
# post country
# def add_country():
#     pass


#delete country
# # def delete(id):
#     # sql = "DELETE FROM countries WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

