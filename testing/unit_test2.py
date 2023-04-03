import unittest
class TestMath(unittest.TestCase):
    def setUp(self):
        self.x = 2
        self.y = 3
    def tearDown(self):
        del self.x
        del self.y
    def test_addition(self):
        result = self.x + self.y
        self.assertEqual(result,5)
