from profile.profile import profile
from settings.game_settings import game_settings


def settings(name):
    print('=' * 20)
    print('[1] - Настройки игры')
    print('[2] - Профиль')
    answer = int(input('Что изменить: '))
    if answer == 1:
        hard = int(input('Установите уровень сложности от 0 до 5: '))
        language = int(input('Установите уровень сложности от 0 до 5: '))
        sound = int(input('Установите уровень сложности от 0 до 5: '))
        game_settings(hard, language, sound)
    if answer == 2:
        name = input('Введите имя: ')
        city = input('Введите город: ')
        status = input('Введите статус: ')
        balance = input('Пополнить баланс: ')
        profile(name, city, status, balance)