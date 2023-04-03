import unittest
from Test_Programs import fact
class Test_fact(unittest.TestCase):
    # def test_case1(self):
    #     self.assertEqual(fact.fact(0),"number must be greater than zero")
    # def test_case2(self):
    #     self.assertEqual(fact.fact(-2),"only positive numbers should enter")
    def test_case1(self):
        self.assertEqual(fact.findfact(5),120)