# Problem from Topcoder
# Once the company does not allow statement reproduction, this is the link for it:
# https://community.topcoder.com/stat?c=problem_statement&pm=14056
import math
from unittest.case import TestCase


def combinations_in_building(building_floors, consecutive_floors, floors_cluster):
    if building_floors < consecutive_floors:
        return 0

    occupied_floors = consecutive_floors * floors_cluster
    if occupied_floors > building_floors:
        return 0

    free_floors = building_floors - occupied_floors
    return math.factorial(floors_cluster + free_floors) // (
        math.factorial(floors_cluster) * math.factorial(free_floors))


class BuildingsCombinationTests(TestCase):
    def test_building_floors_less_then_consecutive(self):
        self.assertEqual(0, combinations_in_building(1, 3, 1))
        self.assertEqual(0, combinations_in_building(2, 3, 1))

    def test_cluster_bigger_then_build(self):
        self.assertEqual(0, combinations_in_building(1, 1, 2))
        self.assertEqual(0, combinations_in_building(2, 1, 3))
        self.assertEqual(0, combinations_in_building(8, 3, 3))

    def test_1_consecutive_floor_ranging_building_floors(self):
        self.assertEqual(1, combinations_in_building(1, 1, 1))
        self.assertEqual(2, combinations_in_building(2, 1, 1))
        self.assertEqual(3, combinations_in_building(3, 1, 1))

    def test_1_consecutive_floor_ranging_floors_cluster(self):
        self.assertEqual(4, combinations_in_building(4, 1, 1))
        self.assertEqual(6, combinations_in_building(4, 1, 2))
        self.assertEqual(4, combinations_in_building(4, 1, 3))

    def test_2_consecutive_floors_ranging_floors_cluster(self):
        self.assertEqual(4, combinations_in_building(5, 2, 1))
        self.assertEqual(1, combinations_in_building(4, 2, 2))
        self.assertEqual(3, combinations_in_building(5, 2, 2))
