# Задача №1.
# Реализовать генератор чисел Фибоначчи.
# Генератор принимает один обязательный аргумент - количество элементов последовательности.
# fibonacci(10) => 1 1 2 3 5 8 13 21 34 55
# https://vk.cc/38QYcS

def generator(n):
    a = 0
    b = 1
    c = 0

    yield 0

    while c < n:
        c += 1
        a, b = b + a, a

        yield a

for i in generator(10):
    print(i)