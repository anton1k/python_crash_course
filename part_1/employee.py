class Employee():
    """Класс представляет работника"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, annual_plus = 5000):
        '''Увеличивает годовой доход'''
        self.annual_salary += annual_plus


meclass = Employee('Антон', 'Костин', 60000)

