class City:

    def __init__(self, name, film_locations, country, visited = False, id = None):
        self.name = name
        self.film_locations = film_locations
        self.country = country
        self.visited = visited
        self.id = id
    #ADDED visited= True 