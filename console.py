from models.country import Country
from models.city import City

import repositories.country_repository as country_repo
import repositories.city_repository as city_repo

#use repositories and their functions to clear the table. 

#Countries 
country1 = Country('Scotland')
country_repo.save(country1)

country2 = Country("New Zealand")
# country_repo.save(country2)

country3 = Country("USA")
# country_repo.save(country3)

# Cities
city1 = City("Edinburgh", "Avengers - Infinity War, Waverley Station", country1)
city_repo.save(city1)
# city2 = City("Glasgow", "Batman, City Center", country1)
# city_repo.save(city2)
# city3 = City("Balater", "The Crown- Baloral Castle", country1)
# city_repo.save(city3)

# city4 = City("Matamata", "Lord Of The Rings - Hobbiton", country2)
# city_repo.save(city4)
# city5 = City("Auckland", "Chronicles of Narnia", country2)
# city_repo.save(city5)
# city6 = City("Wellington", "King Kong, Lyall Bay", country2)
# city_repo.save(city6)

# city7 = City("New York", "Breakfast at Tiffany's - Times Square ", country3)
# city_repo.save(city7)
# city8 = City("Washington DC", "Die Hard", country3)
# city_repo.save(city8)
# city9 = City("Los Angeles", "Once Upon a time in Hollywood - Simi Valley", country3)
# city_repo.save(city9)

# result = country_repo.select()

# for country in result:
#     print(country.__dict__)