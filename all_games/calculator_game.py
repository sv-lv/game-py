def calculator_f():
    print('=' * 20)
    print('Калькулятор ➕')
    print('[1] – сложение')
    print('[2] – вычитание')
    print('[3] – деление')
    print('[4] – умножение')
    print('[5] – выход')
    answer = int(input('Выберите действие: '))
    if answer == 1:
        plus()
    if answer == 2:
        minus()
    if answer == 3:
        division()
    if answer == 4:
        multiplication()

def return_to_calculator():
    print('=' * 20)
    print('Начать заново?')
    print('[1] - начать')
    print('[2] - вернуться в меню игр')
    answer = int(input("Выберите действие: "))
    if answer == 1:
        calculator_f()

def plus():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    result = a+b
    print('Ответ: ', result)
    return_to_calculator()

def minus():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    result = a - b
    print('Ответ: ', result)
    return_to_calculator()

def division():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    result = a/b
    print('Ответ: ', result)
    return_to_calculator()

def multiplication():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    result = a * b
    print('Ответ: ', result)
    return_to_calculator()