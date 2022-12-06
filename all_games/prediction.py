import random
from all_games.exit import exit_

def repeat_prediction():
    print('=' * 20)
    print('Начать заново?')
    print('[1] - начать')
    print('[2] - вернуться в меню игр')
    answer = int(input("Выберите действие: "))
    if answer == 1:
        prediction()

def prediction():
    prediction = ['Конечно, нет', 'Конечно, да', 'Возможно, не сегодня?',
                  'Определенно не стоит!', 'Не стоит сомневаться',
                  'Вам стоит обсудить это с лучшим другом', 'Не медлите!',
                  'Вы уже знаете ответ', 'Время покажет...', ]
    print(f'Простое гадание "Да или нет" с вариациями ответов.')
    print(f'Можно использовать в любых случаях, когда не требуется')
    print(f'философских отступлений, но нужно просто узнать ответ на вопрос.')
    question = input('Задайте Ваш вопрос: ')
    if question:
        random_prediction = random.randint(0, 8)
        print(prediction[random_prediction])
        repeat_prediction()