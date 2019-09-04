from survey import AnonymousSurvey

# Определение вопроса с созданием экземпляра AnonymousSurvey.
question = 'На каком языке вы впервые научились говорить?'
my_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответов.
print('Нажмите "q" для выхода')

while True:
    reverse = input('Язык: ')
    if reverse == 'q':
        break
    my_survey.store_response(reverse)

# Вывод результатов опроса.
print('Спасибо всем, кто принял участие в опросе!')
my_survey.show_result()