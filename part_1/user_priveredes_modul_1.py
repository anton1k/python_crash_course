class Privileges():
    def __init__(self):
        self.privileges = ['удалить', 'банить', 'добавить']

    def r_privileges(self):
        print('Разрешено: ' + ', '.join(self.privileges))
