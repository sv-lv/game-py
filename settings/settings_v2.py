#from profile.profile import profile
#from settings.game_settings import game_settings
from settings.class_prof_set import Prof_settings

def settings1():
    print('=' * 20)
    print('[1] - Настройки игры')
    print('[2] - Профиль')
    answer = int(input('Что изменить: '))
    if answer == 1:
        pass
    if answer == 2:
        city = input('Введите город: ')
        status = input('Введите статус: ')
        balance = input('Введите баланс: ')
        profile1 = Prof_settings(city, status, balance)
        return profile1