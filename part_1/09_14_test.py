from random import randint
# x = randint(1, 6)
class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
         return randint(1, self.sides)

die = Die()
die10 = Die(10)
die20 = Die(20)

for i in range(1, 11):
    print('Обычный куб. ' + 'Бросок №' + str(i) + ' Выпало: ' + str(die.roll_die()) )

for i in range(1, 11):
    print('Куб 10. ' + 'Бросок №' + str(i) + ' Выпало: ' + str(die.roll_die()))

for i in range(1, 11):
    print('Куб 20. ' + 'Бросок №' + str(i) + ' Выпало: ' + str(die.roll_die()))