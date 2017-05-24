# Задача №2.
# Написать функцию, которая принимает координаты точки (x, y) и возвращает номер четверти, которой эта точка принадлежит.

def coordinates(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return False


a=coordinates(int(input('Координата Х: ')), int(input('Координата Y: ')))
print(a)
