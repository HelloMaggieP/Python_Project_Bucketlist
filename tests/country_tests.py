import unittest 
from models.country import Country
from repositories.country_repository import *


class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country1 = Country("Scotland")
        self.country2 = Country("New Zealand")
        

    def test_country_has_name(self):
        self.assertEqual("Scotland", self.country1.name)


