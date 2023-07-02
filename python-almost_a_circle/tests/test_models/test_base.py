"""Testing of all base files, classes and methods"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import pycodestyle
import os


class TestBase(unittest.TestCase):
    """Test method to_json_string"""

    def test_to_init(self):
        """Method inicial """
        b1 = Base()
        b2 = Base(20)
        self.assertEqual(13, b1.id)
        self.assertEqual(20, b2.id)
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_instance_private(self):
        """testing initialization of Square pivate attribute """
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_id(self):
        """testing initialization of Square id attribute """
        self.assertEqual("hello", Base("hello").id)
        self.assertEqual(5.5, Base(5.5).id)
        self.assertEqual(complex(5), Base(complex(5)).id)
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)
        self.assertEqual(True, Base(True).id)
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)
        self.assertEqual((1, 2), Base((1, 2)).id)
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)
        self.assertEqual(range(5), Base(range(5)).id)
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_to_json_string_(self):
        """Method to_json_string """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual("[]", Base.to_json_string([]))
        self.assertEqual("[]", Base.to_json_string(None))
        self.assertEqual(str, type(json_dictionary))
        js = json.dumps([{'width': 5, 'height': 8}])
        self.assertEqual(js, Base.to_json_string([{'width': 5, 'height': 8}]))
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)
        s1 = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s1.to_dictionary()])) == 39)
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json_string(self):
        """Method to from_json_string """
        self.assertEqual([], Base.from_json_string(""))
        self.assertEqual([], Base.from_json_string(None))
        js = json.loads('[{"width": 5, "height": 8}]')
        lis = Base.from_json_string('[{"width": 5, "height": 8}]')
        self.assertEqual(js, lis)
        self.assertEqual(list, type(js))

    def test_save_to_file(self):
        """Method to save_to_file"""
        rec1 = Rectangle(4, 5)
        rec2 = Rectangle(6, 7)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.readline(), '[]')

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.readline(), '[]')
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53, "Error")
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105, "Error")

    def test_create(self):
        """Method to create"""
        r1 = Rectangle(3, 5, 1)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertAlmostEqual(r1.id, 1)
        self.assertAlmostEqual(r2.id, 1)
        self.assertAlmostEqual(r2, r2)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)

    def test_load_from_file(self):
        """Method load_from_file """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertAlmostEqual(list_output[0].id, 3)
        self.assertAlmostEqual(list_output[0].x, 2)
        self.assertAlmostEqual(list_output[0].width, 10)
        self.assertAlmostEqual(list_output[0].height, 7)
        self.assertAlmostEqual(list_output[0].y, 8)
        self.assertAlmostEqual(list_output[1].id, 4)
        self.assertAlmostEqual(list_output[1].x, 0)
        self.assertAlmostEqual(list_output[1].width, 2)
        self.assertAlmostEqual(list_output[1].height, 4)
        self.assertAlmostEqual(list_output[1].y, 0)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        sinput = [s1, s2]
        Square.save_to_file(sinput)
        soutput = Square.load_from_file()
        self.assertAlmostEqual(soutput[0].id, 7)
        self.assertAlmostEqual(soutput[0].width, 5)
        self.assertAlmostEqual(soutput[0].height, 5)
        self.assertAlmostEqual(soutput[0].x, 0)
        self.assertAlmostEqual(soutput[0].y, 0)
        self.assertAlmostEqual(soutput[1].id, 8)
        self.assertAlmostEqual(soutput[1].width, 7)
        self.assertAlmostEqual(soutput[1].height, 7)
        self.assertAlmostEqual(soutput[1].x, 9)
        self.assertAlmostEqual(soutput[1].y, 1)

    def test_pycodestyle_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py',
                                    'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")


if __name__ == '__main__':
    unittest.main()
