import sys

from task_manager import tasks, storage


def action_show_menu():
    print('''
Ежедневник. Выберите действие:

1. Вывести список задач.
2. Добавить задачу.
3. Отредактировать задачу.
4. Завершить задачу.
5. Начать задачу сначала.
6. Удалить задачу.
m. Показать меню.
q. Выход.''')


def action_exit():
    sys.exit(0)


def main():
    action_show_menu()

    actions = {
        '1': tasks.output,
        '2': tasks.add,
        '3': tasks.edit,
        '4': tasks.end,
        '5': tasks.restart,
        '6': tasks.over,
        'm': action_show_menu,
        'q': action_exit
    }

    while True:
        id_action = input('Выберите задачу: ')
        action = actions.get(id_action)

        if action:
            action()
        else:
            print('Введены неверные данные')
