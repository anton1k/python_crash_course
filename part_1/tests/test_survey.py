import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""

    def test_store_single_response(self):
        """Проверяет, что один ответ сохранен правильно."""
        question = 'На каком языке вы впервые научились говорить?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Русский')

        self.assertIn('Русский', my_survey.responses)

    def test_store_three_responses(self):
        """Проверяет, что три ответа были сохранены правильно."""
        question = 'На каком языке вы впервые научились говорить?'
        my_survey = AnonymousSurvey(question)
        responses = ['Русский', 'Английский', 'Неметский']

        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()