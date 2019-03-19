"""Module for implementing jobs"""


from collections import Counter
from random import randint
import os
import re
import MySQLdb


def count_unique_words(file_name):
    """Count all unique words in file

    Positional argument:
    file_name -- name of file
    """

    with open(file_name, 'r') as text_file:
        words = []
        for line in text_file:
            words += re.findall(r"[\w']+", line)
            count = Counter(words)
    return count

def make_dir(path="/home/oleksandr/testdir"):
    """Make directory for path

    Positional argument:
    path -- path to dir what you want to create
    """

    os.mkdir(path, 777)
    res = 'Path '+path+' is created'
    return res

def remove_dir(path="/home/oleksandr/testdir"):
    """Remove directory for path

    Positional argument:
    path -- path to dir what you want to delete
    """

    os.rmdir(path)
    res = 'Directory '+path+' was deleted!'
    return res

def dump_command():
    """Dump result of shell command"""

    result = os.popen('ps').read()
    return result

def generate_job():
    """Generate random jobs"""

    db_conn = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "tasks")

    cursor = db_conn.cursor()

    for count in range(1, 4):
        rand = randint(1, 1000)
        task_title = f'Task{rand}'
        task_desc = f'Task Description{rand}'
        is_solved = 0
        sql = """INSERT INTO tasks(task_title, description, is_solved)
                 VALUES(%s, %s, %s)"""
        cursor.execute(sql, (task_title, task_desc, is_solved))
    db_conn.commit()
    db_conn.close()
    return 'Tasks was created'
