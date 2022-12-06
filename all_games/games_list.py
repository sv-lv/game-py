from all_games.calculator_game import calculator_f
from all_games.rus_rullete import rus_rulette
from all_games.fish import fish
from all_games.contries import countries
from all_games.prediction import prediction
from all_games.train import train
from all_games.exit import exit_


def games():
    '''Функция выводит меню игр'''
    print('=' * 20)
    print('[1] - Калькулятор ➕')
    print('[2] - Русская рулетка 🔫')
    print('[3] - Рыбки 🎏')
    print('[4] - Страны 🇦🇹')
    print('[5] - Гадание 🔮')
    print('[6] - Поезд ушел? 🚉')
    print('[7] - Выход 🚪')
    answer = int(input('Выберите игру: '))
    if answer == 1:
        calculator_f()
    if answer == 2:
        rus_rulette()
    if answer == 3:
        fish()
    if answer == 4:
        countries()
    if answer == 5:
        prediction()
    if answer == 6:
        train()
    if answer == 7:
        exit_()