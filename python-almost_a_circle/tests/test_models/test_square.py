"""Testing of all square files, classes and methods"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import pycodestyle


class TestSquare(unittest.TestCase):
    """Test method to_json_string"""

    def test_init_instance(self):
        """ Method inicial """
        self.assertIsInstance(Square(10), Base)
        self.assertIsInstance(Square(10), Square)
        with self.assertRaises(TypeError):
            Square()
        self.assertEqual(Square(10).id, Square(11).id - 1)

        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

        self.assertEqual(7, Square(10, 2, 2, 7).id)
        self.assertEqual(5, Square(5, 2, 3, 9).size)
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)
        self.assertEqual(0, Square(10).x)
        self.assertEqual(0, Square(10).y)

    def test_size(self):
        """ testing initialization of Square size attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_of_x(self):
        """ testing initialization of Square x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)

    def test_of_y(self):
        """testing initialization of Square y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)

    def size_square(self):
        """ Method size of Square"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_area(self):
        """Method area of class square"""
        self.assertEqual(100, Square(10, 0, 0, 1).area())
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)

    def test_update_args(self):
        """Method update of class square args"""
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))
        s.update(89, 2)
        self.assertEqual(2, s.width)
        self.assertEqual(2, s.height)
        s.update(None)
        correct = "[Square] ({}) 3/4 - 2".format(s.id)
        self.assertEqual(correct, str(s))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_kwargs(self):
        """Method update of class square args"""
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)
        s.update(id=None)
        correct = "[Square] ({}) 1/3 - 9".format(s.id)
        self.assertEqual(correct, str(s))
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/3 - 7".format(s.id)
        self.assertEqual(correct, str(s))
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_dictionary(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
