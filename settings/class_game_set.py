class Game_settings():
    def __init__(self, hard, language, sound):
        '''настройки профиля'''
        self.hard = hard
        self.language = language
        self.sound = sound

    def game_settings(self):
        print('=' * 20)
        print('Профиль')
        print("Сложность: ", self.hard)
        print("Язык: ", self.language)
        print("Громкость: ", self.sound)


profile_g = Game_settings(hard=int(input("Введите сложность: ")), language=input("Введите язык: "),
                          sound=int(input("Введите громкость звуков (от 1 до 5): ")))
profile_g.profile_settings()