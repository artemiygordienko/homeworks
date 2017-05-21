# Задача №2. Закрепляем цикл while
# Спросить количество тарелок и количество моющего средства.
# Моющее средство расходуется из расчета 0.5 на одну тарелку.
# В цикле выводить сколько моющего средства осталось после мытья каждой тарелки.
# Вывести на экран сколько тарелок осталось, когда моющее средство закончилось или наоборот.
plates = int(input('Количество тарелок: '))
cleaner = float(input('Моющего средства: '))
while plates > 0 and cleaner >= 0.5:
    plates -= 1
    cleaner -= 0.5
    print('Осталось моющего средства', cleaner)

if plates > 0:
    print('Осталось тарелок', plates)
    print('Закончилось моющее средство')
elif cleaner >= 0.5:
    print('Осталось моющего средства', cleaner)
    print('Тарелки закончились')
else:
    print('Всего хватило')

