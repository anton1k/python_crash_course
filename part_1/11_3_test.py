import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    '''тесты для "employee.py"'''

    def setUp(self):
        self.empl = Employee('Антон', 'Костин', 60000)

    def test_give_default_raise(self):
        '''Проверяет что работает без параметра'''
        self.empl.give_raise()
        self.assertEqual(self.empl.annual_salary, 65000)

    def test_give_custom_raise(self):
        '''Проверяет что работает с параметром'''
        self.empl.give_raise(10000)
        self.assertEqual(self.empl.annual_salary, 70000)



unittest.main()
    