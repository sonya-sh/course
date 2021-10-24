import json
import os.path


def register(login, passwd):
    tmp = True
    with open('data.json', 'r') as file:
        users_data = json.load(file)
    for k in users_data.keys():
        if k == login:
            tmp = False
    if tmp:
        users_data[login] = passwd
        with open('data.json', 'w') as file:
            json.dump(users_data, file)
    return tmp


def login_function(login, passwd):
    registered = False
    with open('data.json', 'r') as file:
        users_data = json.load(file)
    for x, y in users_data.items():
        if x == login and y == passwd:
            registered = True
    return registered


data = {}
if os.path.exists('data.json'):
    print('Файл существует')
else:
    with open('data.json', 'w') as file:
        json.dump(data, file)
choice = int(input('1 - регистрация, 2 - вход'))
login = input('Введите логин: ')
passwd = input('Введите пароль: ')
if choice == 1:
    if register(login, passwd):
        print('Пользователь добавлен')
    else:
        print('Пользователь уже существует')
else:
    if login_function(login, passwd):
        print('Успешный вход')
    else:
        print('Логин или пароль неверные')
