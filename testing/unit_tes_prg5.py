import unittest
from Test_Programs.program4 import Employee
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee=Employee('Neel',50000)
    def test_email(self):
        self.assertEqual(self.employee.email, 'neel@hcl.com')
    def test_apply_raise(self):
        self.employee.apply_raise(10)
        self.assertEqual(self.employee.salary,55000)

