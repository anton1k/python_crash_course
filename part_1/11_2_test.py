import unittest
from sity_function_1 import get_formatted_sity

class SityTestCase(unittest.TestCase):
    '''тесты для "name_function.py"'''

    def test_sity_country_sity(self):
        """Город, страна типа 'Киров, Россия' работают правильно?"""

        formatted_sity = get_formatted_sity('киров', 'россия')
        self.assertEqual(formatted_sity, 'Киров, Россия')

    def test_sity_country_population_sity(self):
        """Город, страна - численость типа 'Киров, Россия - численность 6000000' работают правильно?"""

        formatted_sity = get_formatted_sity('киров', 'россия', 600000)
        self.assertEqual(formatted_sity, 'Киров, Россия - численность 600000')

unittest.main()
    