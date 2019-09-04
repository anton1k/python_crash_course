class User():
    def __init__(self, first_name, last_name, age, profehinal):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profehinal = profehinal

    def describe_user(self):
        return 'Имя - {0}, Фамилия - {1}, возраст - {2}, профессия - {3}'.format(self.first_name.title(), self.last_name.title(), str(self.age), self.profehinal)

    def greet_user(self):
        print('Привет ' + self.first_name.title())

user = User('Иван', 'Петров', 32, 'врач')
print(user.describe_user())
user.greet_user()

user1 = User('вася', 'иванов', 44, 'повар')
print(user1.describe_user())
user1.greet_user()