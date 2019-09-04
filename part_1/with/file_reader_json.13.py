import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.

filname = 'username.json'

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    try:
        with open(filname) as target:
            username = json.load(target)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input('Как вас зовут?: ')
    with open(filname, 'w') as target:
        json.dump(username, target)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print('С возвращением ' + username)
    else:
        username = get_new_username()
        print('Мы будем помнить тебя, когда ты вернешься ' + username)

greet_user()
