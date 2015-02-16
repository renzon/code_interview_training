# a turtle moves from 2D point 0,0. First element in array indicate the turtle's move to North. Next move to east, next to South, next to West and so on.
#
# Read an array of movements and indicate when the turtle cross a path which it has already crossed.
#
# example: [1,2,3, 4] does not cross
# [2,2,2,2] cross on item with index 3 (in zero based array)

from itertools import cycle


def crossing_lines(line_a, line_b):
    def crossing_point(point_a, point_b):
        return point_a[0] <= point_b[0] <= point_a[1] or \
               point_a[1] <= point_b[0] <= point_a[0] or \
               point_b[0] <= point_a[0] <= point_b[1] or \
               point_b[1] <= point_a[0] <= point_b[0]

    return crossing_point((line_a[0], line_a[2]), (line_b[0], line_b[2])) and \
           crossing_point((line_a[1], line_a[3]), (line_b[1], line_b[3]))


def path_iterator(path):
    line = [0, 0, 0, 0]
    directions = cycle(['North', 'East', 'South', 'West'])
    for length in path:
        direction = next(directions)
        line[0] = line[2]
        line[1] = line[3]
        if direction == 'North':
            line[3] += length
            yield list(line)
        elif direction == 'South':
            line[3] -= length
            yield list(line)
        elif direction == 'East':
            line[2] += length
            yield list(line)
        else:
            line[2] -= length
            yield list(line)


def has_turtle_crossed_path(path):
    lines = [l for l in path_iterator(path)]
    for i, line in enumerate(lines[:-1]):
        for idx in range(i+3, len(lines)):
            if crossing_lines(line, lines[idx]):
                return idx
    return -1


import unittest


class TurtlePathTests(unittest.TestCase):
    def test_no_crossing(self):
        self.assertEqual(-1, has_turtle_crossed_path([1, 2, 3, 4]))

    def test_crossing(self):
        self.assertEqual(3, has_turtle_crossed_path([2, 2, 2, 2]))


class LineCrossingTests(unittest.TestCase):
    def test_no_crossing(self):
        self.assertFalse(crossing_lines((0, 0, 0, 2), (0, -1, 1, -1)))

    def test_crossing(self):
        self.assertTrue(crossing_lines((0, 0, 0, 2), (-1, 1, 1, 1)))


class PathTests(unittest.TestCase):
    def test_generation(self):
        it = path_iterator([2, 2, 2, 2])
        line = next(it)
        self.assertEqual([0, 0, 0, 2], line)
        line = next(it)
        self.assertEqual([0, 2, 2, 2], line)
        line = next(it)
        self.assertEqual([2, 2, 2, 0], line)
        line = next(it)
        self.assertEqual([2, 0, 0, 0], line)


