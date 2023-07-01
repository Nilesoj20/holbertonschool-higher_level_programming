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
        self.assertEqual(1, b1.id)
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

    
if __name__ == '__main__':
    unittest.main()
