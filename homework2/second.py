# Задача №2.
# Написать функцию, которая принимает координаты точки (x, y) и возвращает номер четверти, которой эта точка принадлежит.

def coordinates():
    x = int(input('Координата Х: '))
    y = int(input('Координата Y: '))
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    elif x == 0 or y == 0:
        return False


coordinates()
