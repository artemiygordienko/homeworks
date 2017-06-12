# Задача №2
# Реализовать генератор случайных паролей указанной длины.
# В пароле можно использовать любые символы в верхнем и нижнем регистре.
# Например: password_generator(16), вернет случайный пароль длиной 16 символов.
# Пригодится стандартный модуль random


import random
from string import digits, ascii_letters


def pass_generator(n):
    valid_values = list(digits + ascii_letters)
    radix = len(valid_values)

    yield "".join([str(valid_values[random.randrange(radix)]) for i in range(n)])

for i in pass_generator(10):
    print(i)