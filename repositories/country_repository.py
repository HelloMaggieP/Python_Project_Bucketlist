from db.run_sql import run_sql
from models.country import Country
from models.city import City
import repositories.city_repository as city_repo

def select_all(country):
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['id'])
        countries.append(country)
    return countries


# new country
#get country
# post country
def add_country():
    pass


#delete country
def delete():
    pass
