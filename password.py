ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet = ALPHABET.upper()
numbers = '1234567890'

def check_password(password: str) -> bool:
    '''Функция проверяет надежность пароля'''
    big_words = 0
    small_words = 0
    check_number = 0
    if len(password) > 8:
        for i in password:
            if i in ALPHABET:
                big_words += 1
            if i in alphabet:
                small_words += 1
            if i in numbers:
                check_number += 1
        if big_words > 0 and small_words > 0 and check_number > 0:
            flag = True
        else:
            flag = False
    else:
        flag = False
    return flag