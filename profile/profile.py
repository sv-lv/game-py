def profile(name, profile_info):
    if profile_info == 0:
        city = '__'
        status = '__'
        balance = '__'
    else:
        city = profile_info.city
        status = profile_info.status
        balance = profile_info.balance
    answer = 0
    while answer != 1:
        print('='*20)
        print('Имя пользователя:', name)
        print('Город: ', city)
        print("Статус: ", status)
        print("Баланс: ", balance)
        print('[1] - Выход')
        answer = int(input('Выбрать действие: '))
        print('='*20)