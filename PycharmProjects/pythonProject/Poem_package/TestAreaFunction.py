import unittest
from Poem_package import area_of_circle
from math import pi


class TestAreaFunction(unittest.TestCase):
    def test_area_test_function(self):
        self.assertAlmostEqual(area_of_circle.area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle.area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle.area_of_circle(2), pi * 2 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, area_of_circle.area_of_circle, -1)
        self.assertRaises(ValueError, area_of_circle.area_of_circle, -5)

    def test_radius_type(self):
        self.assertRaises(TypeError, area_of_circle.area_of_circle, True)
        self.assertRaises(TypeError, area_of_circle.area_of_circle, 2 + 5j)