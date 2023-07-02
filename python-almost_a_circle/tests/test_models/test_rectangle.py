"""Testing of all rectangle files, classes and methods"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test for class Rectangle"""
    def test_inicio(self):
        """Method init for class Rectangle """
        r1 = Rectangle(3, 4)
        r2 = Rectangle(4, 2)
        self.assertEqual(3, r1.width)
        self.assertEqual(4, r1.height)
        self.assertEqual(0, r1.x)
        self.assertEqual(0, r1.y)
        self.assertEqual(15, r1.id)
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
        self.assertEqual(25, r2.id)
        self.assertRaises(TypeError, Rectangle, 4, 5, "2", 1)
        self.assertRaises(TypeError, Rectangle, 4, 5, 2, "1")
        self.assertRaises(ValueError, Rectangle, 4, 5, -2, 1)
        self.assertRaises(ValueError, Rectangle, 4, 5, 2, -1)
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)


if __name__ == '__main__':
    unittest.main()
