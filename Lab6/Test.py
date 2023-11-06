import unittest
import math
from Modul import calculate_circle_area, calculate_circle_diameter, calculate_circle_radius

class TestCircleCalculations(unittest.TestCase):
    
    def test_calculate_circle_area(self):
        self.assertAlmostEqual(calculate_circle_area(1), math.pi)  # Проверяем для радиуса 1
        self.assertAlmostEqual(calculate_circle_area(0), 0)       # Проверяем для радиуса 0
        self.assertAlmostEqual(calculate_circle_area(5), 25 * math.pi)  # Проверяем для радиуса 5
    
    def test_calculate_circle_diameter(self):
        self.assertEqual(calculate_circle_diameter(1), 2)  # Проверяем для радиуса 1
        self.assertEqual(calculate_circle_diameter(0), 0)  # Проверяем для радиуса 0
        self.assertEqual(calculate_circle_diameter(5), 10)  # Проверяем для радиуса 5
    
    def test_calculate_circle_radius(self):
        self.assertEqual(calculate_circle_radius(2), 1)  # Проверяем для диаметра 2
        self.assertEqual(calculate_circle_radius(0), 0)  # Проверяем для диаметра 0
        self.assertEqual(calculate_circle_radius(10), 5)  # Проверяем для диаметра 10

if __name__ == '__main__':
    unittest.main()
