# Problem from Topcoder
# Once the company does not allow statement reproduction, this is the link for it:
# https://community.topcoder.com/stat?c=problem_statement&pm=14056
from unittest.case import TestCase


def combinations_in_building(building_floors, consecutive_floors, floors_cluster):
    if building_floors < consecutive_floors:
        return 0
    total_floor = consecutive_floors * floors_cluster
    if total_floor > building_floors:
        return 0


class BuildingsTests(TestCase):
    def test_building_floors_less_then_consecutive(self):
        self.assertEqual(0, combinations_in_building(1, 3, 1))
        self.assertEqual(0, combinations_in_building(2, 3, 1))

    def test_cluster_bigger_then_build(self):
        self.assertEqual(0, combinations_in_building(1, 1, 2))
        self.assertEqual(0, combinations_in_building(2, 1, 3))
        self.assertEqual(0, combinations_in_building(8, 3, 3))
