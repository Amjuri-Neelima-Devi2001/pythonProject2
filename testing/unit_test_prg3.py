import unittest
from Test_Programs import program2
class My_test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(program2.rlist1([10,20,30]),[30,20,10])
    def test_case2(self):
        self.assertEqual(program2.rlist1([-1.2,1.3,1.6]),[1.6,1.3,-1.2])
    def test_case3(self):
        self.assertEqual(program2.rlist1(['a','b','c']),['c','b','a'])
    def test_case4(self):
        self.assertEqual(program2.rlist1(['hello','neel','devi']),['devi','neel','hello'])