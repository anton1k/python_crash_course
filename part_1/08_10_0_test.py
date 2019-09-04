names = ['Добрыня', 'Петя', 'Вася']
def make_great(names):

   for i in range(len(names)):
      names[i] += '-Great'

   magicians(names)


def magicians(names):

   for name in names:
      print('Фокусника зовут - ' + name)


make_great(names)







    


