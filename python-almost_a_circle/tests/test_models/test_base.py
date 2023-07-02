"""Testing of all base files, classes and methods"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import pycodestyle


class TestBase(unittest.TestCase):
    """Test method to_json_string"""

    def test_to_init(self):
        """Method inicial """
        b1 = Base()
        b2 = Base(20)
        self.assertEqual(13, b1.id)
        self.assertEqual(20, b2.id)

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
