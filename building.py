# Problem from Topcoder
# Once the company does not allow statement reproduction, this is the link for it:
# https://community.topcoder.com/stat?c=problem_statement&pm=14056
from unittest.case import TestCase


def combinations_in_building(building_floors, consecutive_floors):
    if building_floors < consecutive_floors:
        return 0
    return building_floors // consecutive_floors


class BuildingsTests(TestCase):
    def test_building_floors_less_then_consecutive(self):
        consecutive_floors = 3
        building_floors = 1
        self.assertEqual(0, combinations_in_building(building_floors, consecutive_floors))
        building_floors = 2
        self.assertEqual(0, combinations_in_building(building_floors, consecutive_floors))

    def test_1_consecutive_floor(self):
        consecutive_floors = 1
        building_floors = 1
        self.assertEqual(1, combinations_in_building(building_floors, consecutive_floors))
        building_floors = 2
        self.assertEqual(2, combinations_in_building(building_floors, consecutive_floors))
        building_floors = 3
        self.assertEqual(3, combinations_in_building(building_floors, consecutive_floors))
        building_floors = 4
        self.assertEqual(4, combinations_in_building(building_floors, consecutive_floors))
        building_floors = 5
        self.assertEqual(5, combinations_in_building(building_floors, consecutive_floors))
