import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''тесты для "name_function.py"'''

    def test_first_last_name(self):
        """Имена вида 'Антон Костин' работают правильно?"""
        formatted_name = get_formatted_name('антон', 'костин')
        self.assertEqual(formatted_name, 'Антон Костин')

    def test_first_middle_last_name(self):
        """Имена вида 'Антон Тошик Костин' работают правильно?"""
        formatted_name = get_formatted_name('антон', 'костин', 'тошик')
        self.assertEqual(formatted_name, 'Антон Тошик Костин')

unittest.main()
    