"""Testing of all rectangle files, classes and methods"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import pycodestyle


class TestRectangle(unittest.TestCase):
    """Test for class Rectangle"""

    def test_to_init(self):
        """Method init for class Rectangle """
        r1 = Rectangle(3, 4)
        r2 = Rectangle(4, 2)
        self.assertEqual(3, r1.width)
        self.assertEqual(4, r1.height)
        self.assertEqual(0, r1.x)
        self.assertEqual(0, r1.y)
        self.assertEqual(1, r1.id)
        self.assertRaises(TypeError, Rectangle, "3", 4)
        self.assertRaises(TypeError, Rectangle, "3", 4)
        self.assertRaises(ValueError, Rectangle, -1, 3)
        self.assertRaises(ValueError, Rectangle, 1, -3)
        self.assertRaises(ValueError, Rectangle, 0, 3)
        self.assertIsInstance(Rectangle(10, 2), Base)
        r_1 = Rectangle(10, 2)
        r_2 = Rectangle(2, 10)
        self.assertEqual(r_1.id, r_2.id - 1)
        r2 = Rectangle(4, 5, 2, 1)
        self.assertEqual(4, r2.width)
        self.assertEqual(5, r2.height)
        self.assertEqual(2, r2.x)
        self.assertEqual(1, r2.y)
        self.assertEqual(11, r2.id)
        self.assertRaises(TypeError, Rectangle, 4, 5, "2", 1)
        self.assertRaises(TypeError, Rectangle, 4, 5, 2, "1")
        self.assertRaises(ValueError, Rectangle, 4, 5, -2, 1)
        self.assertRaises(ValueError, Rectangle, 4, 5, 2, -1)

    def test_pycodestyle_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py',
                                    'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")


if __name__ == '__main__':
    unittest.main()
