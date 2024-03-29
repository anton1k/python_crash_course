class User():
    def __init__(self, first_name, last_name, age, profehinal):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profehinal = profehinal
        self.login_attempts = 0

    def describe_user(self):
        return 'Имя - {0}, Фамилия - {1}, возраст - {2}, профессия - {3}'.format(self.first_name.title(), self.last_name.title(), str(self.age), self.profehinal)

    def greet_user(self):
        print('Привет ' + self.first_name.title())

    def increment_login_attempts(self):
        print('Значения обнулились увеличилось на 1')
        self.login_attempts += 1

    def reset_login_attempts(self):
        print('Значения обнулились')
        self.login_attempts = 0
