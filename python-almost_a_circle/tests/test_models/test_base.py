import unittest
from models.base import Base

class To_json_string(unittest.TestCase):
    """comentario"""

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))


if __name__ == '__main__':
    unittest.main()
