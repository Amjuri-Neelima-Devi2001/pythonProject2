import unittest
from Test_programs import program3
class My_unit_test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(program3.index_list())