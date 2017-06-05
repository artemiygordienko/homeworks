from task_manager import storage

TASK_STATUS_OPEN = 'open'
TASK_STATUS_REOPEN = 'reopen'
TASK_STATUS_CLOSE = 'close'


def output():
    tasks = storage.show_all_tasks()
    for task in tasks:
        print("""
Задача №{task[id]}: {task[name]}
Описание: {task[task_text]}
Начало: {task[start_date]}
Статус: {task[status]}
Конец: {task[end_date]}
""".format(task=task))


def add():
    while True:
        name = input('Введите название задачи: ')
        task_text = input('Введите описание задачи: ')
        if name:
            storage.new_task(name, task_text)
            break
        else:
            print('Вы не ввели название задачи!')
    print('Задача добавлена.')


def edit():
    while True:
        task_id = input('Введите номер задачи: ')
        if not task_id:
            print('Вы не ввели номер задачи!')
        task = storage.find_task_by_id(task_id)
        if not task:
            print('Задача с таким номером не найдена!')

        new_name = input('Введите новое название задачи: ')
        new_text = input('Введите новое описание задачи: ')
        if new_name:
            storage.edit_name(task_id, new_name)
            break
        if new_desc:
            storage.edit_task_text(task_id, new_text)
            print('Задача отредактирована.')
            break


def end():
    while True:
        task_id = input('Введите название завершенной задачи: ')
        if task_id:
            task = storage.find_task_by_id(task_id)
            if not task:
                print('Задача с таким названием не найдена!')
            else:
                storage.end(task_id)
                break
        else:
            print('Вы не ввели название задачи!')
    print('Задача закрыта.')


def restart():
    while True:
        task_id = input('Введите номер задачи для пересоздания: ')
        if not task_id:
            print('Вы не ввели номер задачи!')
        task = storage.find_task_by_id(task_id)
        if not task:
            print('Задача с таким номером не найдена!')
        elif task['status'] in [TASK_STATUS_OPEN, TASK_STATUS_REOPEN]:
            print('Задача уже открыта.')
            break
        else:
            storage.change_task_status(task_id, TASK_STATUS_REOPEN)
            print('Задача пересоздана.')
            break


def over():
    print('удаление задачи')
