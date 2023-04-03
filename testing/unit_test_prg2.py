import unittest
from Test_Programs import program1
class My_test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(program1.add_two(10,20),30)
    def test_case2(self):
        self.assertEqual(program1.add_two(-10,20),10)
    def test_case3(self):
        self.assertEqual(program1.add_two(10,-20),-10)
    def test_case4(self):
        self.assertEqual(program1.add_two(-10,-20),-30)

