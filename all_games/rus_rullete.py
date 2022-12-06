import random
from all_games.exit import exit_


def repeat_rus_rulette():
    print('=' * 20)
    print('Начать заново?')
    print('[1] - начать')
    print('[2] - вернуться в меню игр')
    answer = int(input("Выберите действие: "))
    if answer == 1:
        rus_rulette()

def rus_rulette():
    print('=' * 20)
    print('[1] - начать')
    print('[2] - отказаться')
    choice_rr = int(input('Выберите действие: '))
    if choice_rr == 1:
        random_shot = random.randint(0, 1)
        if random_shot == 1:
            print('Вы проиграли.')
            repeat_rus_rulette()
        if random_shot == 0:
            print('Вы выиграли.')
            repeat_rus_rulette()
    else:
        exit_()