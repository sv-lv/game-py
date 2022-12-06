class Prof_settings():
    def __init__(self, city, status, balance):
        '''настройки профиля'''
        self.city = city
        self.status = status
        self.balance = balance

    def prof_settings(self):
        print('=' * 20)
        print('Настройки игры')
        print('Город: ', self.city)
        print("Статус: ", self.status)
        print("Баланс: ", self.balance)