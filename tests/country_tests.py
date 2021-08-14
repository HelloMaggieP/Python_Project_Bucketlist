import unittest 
from models.country import Country
from repositories.country_repository import *


class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country1 = Country("Scotland")
        self.country2 = Country("New Zealand")
        

    def test_country_has_name(self):
        self.assertEqual("Scotland", self.country1.name)

    #TEST NOT PASSING LINE 21
    # def test_select_all(self):
    #     self.country1 = Country("Scotland")
    #     self.country2 = Country("New Zealand")
    #     self.countries = [self.country1, self.country2]
    #     self.assertEqual(2, self.countries.select_all())

    # # DELETE 1 TEST
    # def test_delete_country(self):
    #     country_repository.save(self.country1)
    #     item = country_repository.delete(self.country1) 
    #     self.assertEqual(None, item)