import sqlite3
import os.path as Path

SQL_SHOW_ALL = '''
SELECT id, name, task_text, status, start_date, end_date
FROM task_man
'''

SQL_SELECT_TASK_BY_ID = '''
SELECT name, task_text, status, start_date, end_date
FROM task_man
WHERE id = ?
'''

SQL_INSERT_NEW_TASK = '''
INSERT INTO task_man (name, task_text)
VALUES (?, ?)
'''

SQL_EDIT_NAME = '''
UPDATE task_man
SET name = ?
WHERE id = ?
'''

SQL_EDIT_TASK_TEXT = '''
UPDATE task_man
SET task_text = ?
WHERE id = ?
'''

SQL_CHANGE_STATUS = '''
UPDATE task_man
SET status = ?, start_date = CURRENT_TIMESTAMP, end_date = ''
WHERE id = ?
'''

SQL_CLOSE_TASK = '''
UPDATE task_man
SET status = 'close', end_date = CURRENT_TIMESTAMP
WHERE id = ?
'''


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn


def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'schema.sql')

        with open(script_file_path) as f:
            conn.executescript(f.read())


def show_all_tasks():
    with connect('task_man.sqlite') as conn:
        cursor = conn.execute(SQL_SHOW_ALL)
        return cursor.fetchall()


def find_task_by_id(task_id):
    with connect('task_man.sqlite') as conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_ID, (task_id,))
        return cursor.fetchall()


def new_task(name, task_text):
    with connect('task_man.sqlite') as conn:
        initialize(conn)
        cursor = conn.execute(SQL_INSERT_NEW_TASK, (name, task_text))
        return cursor.fetchone()


def edit_name(name, task_id):
    with connect('task_man.sqlite') as conn:
        initialize(conn)
        conn.execute(SQL_EDIT_NAME, (name, task_id))


def edit_text(task_id, task_text):
    with connect('task_man.sqlite') as conn:
        initialize(conn)
        conn.execute(SQL_EDIT_TASK_TEXT, (task_text, task_id))
        return


def change_status(task_id, status):
    with connect('task_man.sqlite') as conn:
        initialize(conn)
        conn.execute(SQL_CHANGE_STATUS, (status, task_id))
        return


def end(task_id):
    with connect('task_man.sqlite') as conn:
        initialize(conn)
        conn.execute(SQL_CLOSE_TASK, (task_id,))
        return
