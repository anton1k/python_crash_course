def make_album(name, title, track = ''):
   res = {}
   if track:
      res = {
         'name': name,
         'title': title,
         'track': track,
         }
   else:
      res = {
         'name': name,
         'title': title,
         }
   return res

while True:
   name = input('Введите исполнителя: ')
   title = input('Введите названия альбома: ')

   if name and title:
      print(make_album(name, title))
      break









    


