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

print(make_album('КиШ', 'Король и шут'))
print(make_album('Ария', 'Осколки льда'))
print(make_album('ДДТ', 'Осень', 14))









    


