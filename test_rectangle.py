import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    """
    Набор unit-тестов для функций area и perimeter
    """
    
    def test_area_normal(self):
        # обычный случай: стороны 10 и 5
        result = area(10, 5)
        self.assertEqual(result, 50)
    
    def test_area_zero_side(self):
        # одна сторона равна 0
        result = area(10, 0)
        self.assertEqual(result, 0)

    def test_area_square(self):
        # прямоугольник с равными сторонами (квадрат)
        result = area(4, 4)
        self.assertEqual(result, 16)

    def test_perimeter_normal(self):
        # обычный случай: стороны 10 и 5
        result = perimeter(10, 5)
        self.assertEqual(result, 30)

    def test_perimeter_zero_side(self):
        # одна сторона равна 0
        result = perimeter(10, 0)
        self.assertEqual(result, 20)

    def test_perimeter_square(self):
        # прямоугольник с равными сторонами
        result = perimeter(4, 4)
        self.assertEqual(result, 16)

if __name__ == "__main__":
    unittest.main()