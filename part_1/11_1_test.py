import unittest
from sity_function import get_formatted_sity

class SityTestCase(unittest.TestCase):
    '''тесты для "name_function.py"'''

    def test_sity_country_sity(self):
        """Имена вида 'Антон Костин' работают правильно?"""
        formatted_sity = get_formatted_sity('киров', 'россия')
        self.assertEqual(formatted_sity, 'Киров, Россия')


unittest.main()
    