filname = 'programming.txt'

with open(filname, 'a') as target: # ключ "а" говорит что нужно дописать в файл
    target.write('Я также люблю находить смысл в больших наборах данных \n')
    target.write('Я люблю создавать приложения, которые могут работать в браузере \n')