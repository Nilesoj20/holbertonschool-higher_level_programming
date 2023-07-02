"""Testing of all base files, classes and methods"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):
    """Test method to_json_string"""

    def test_to_init(self):
        """Method inicial """
        b1 = Base()
        b2 = Base(20)
        self.assertEqual(3, b1.id)
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
        Rectangle.save_to_file([rec1, rec2])
        file_1 = rec1.to_dictionary()
        file_2 = rec2.to_dictionary()
        file_total = [file_1, file_2]
        str_json = Rectangle.to_json_string(file_total)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.readline(), str_json)


if __name__ == '__main__':
    unittest.main()
