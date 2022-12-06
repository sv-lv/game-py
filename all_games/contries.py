def repeat_countries():
    """Функция выводится, если игра окончена"""
    print('=' * 20)
    print('Начать заново?')
    print('[1] - начать')
    print('[2] - вернуться в меню игр')
    answer = int(input("Выберите действие: "))
    if answer == 1:
        countries()

def countries():
    print('=' * 20)
    print('Столица Монголии:')
    print('[1] – Сухэбатор')
    print('[2] – Улан-Батор')
    print('[3] – Эрдэнэт')
    answer_mong = int(input('Введите правильный ответ: '))
    if answer_mong != 2:
        print('Вы проиграли :((')
        repeat_countries()
    else:
        print('Отлично! Следующий вопрос: Столица Австрии –')
        print('[1] – Грац')
        print('[2] – Инсбрук')
        print('[3] – Вена')
        answer_austria = int(input('Введите правильный ответ: '))
        if answer_austria != 3:
            print('Вы проиграли :((')
            repeat_countries()
        else:
            print('Очень хорошо! Следующий вопрос: Столица Мексики –')
            print('[1] – Чиуауа')
            print('[2] – Мехико')
            print('[3] – Канкун')
            answer_mexico = int(input('Введите правильный ответ: '))
            if answer_mexico != 2:
                print('Вы проиграли :((')
                repeat_countries()
            else:
                print('Замечательно! Столица Японии –')
                print('[1] – Токио')
                print('[2] – Сохо')
                print('[3] – Киото')
                answer_japan = int(input('Введите правильный ответ: '))
                if answer_japan != 1:
                    print('Вы проиграли :((')
                    repeat_countries()
                else:
                    print('Просто великолепно! Столица Бразилии –')
                    print('[1] – Бразилиа')
                    print('[2] – Сан-Паулу')
                    print('[3] – Рио-де-Жанейро')
                    answer_brasilia = int(input('Введите правильный ответ: '))
                    if answer_brasilia != 1:
                        print('Вы проиграли :((')
                        repeat_countries()
                    else:
                        print('Спасибо за игру!')
                        print('=' * 27)
                        repeat_countries()