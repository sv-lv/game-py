from password import check_password
from profile.profile import profile
from all_games.games_list import games
from settings.settings_v2 import settings1


def menu(name):
    answer = 0
    profile_info = 0
    while answer != 4:
        print('[1] - профиль')
        print('[2] - библиотека игр')
        print('[3] - настройки')
        print('[4] - выход')
        answer = int(input('Что хотите сделать?'))
        if answer == 1:
            profile(name, profile_info)
        if answer == 2:
            games()
        if answer == 3:
            profile_info = settings1()

def main():
    print('Добро пожаловать в Games!')
    print('Пожалуйста, пройдите регистрацию')
    name = input('Введите имя:')
    password = input('Введите пароль:')
    if check_password(password):
        print('Вы успешно зарегистрировались')
        print('='*20)
        menu(name)
    else:
        print('Пароль не соответствует условиям безопасности')

main()