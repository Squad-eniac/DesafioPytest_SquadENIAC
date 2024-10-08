import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from introducao_a_testes_no_python.exercise import str_to_bool


class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)

    def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1)

if __name__ == '__main__':
    unittest.main()