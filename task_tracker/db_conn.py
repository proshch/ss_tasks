"""This is the module to connect database
and work with it"""


import MySQLdb


def is_available(task_id):
    """Return the status of task accessibility"""

    db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "tasks")
    cursor = db_tasks.cursor()
    sql = """SELECT is_solved FROM tasks
             WHERE task_id = {}""".format(task_id)
    cursor.execute(sql)
    status = cursor.fetchall()
    for row in status:
        status = row[0]
    db_tasks.close()

    return status

def get_tasks():
    """Return all available tasks"""

    db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "tasks")

    tasks = []
    # prepare a cursor object using cursor() method
    cursor = db_tasks.cursor()

    sql = """SELECT * FROM tasks
             WHERE is_solved = false"""

    # execute SQL query using execute() method
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        tasks.append(str(row))
    # disconnect from server
    db_tasks.close()
    return tasks

def update_result(task_id, result, client):
    """Update task as solved and
    write result into database

    Positional arguments:
    task_id -- id of the task
    result -- result of task
    client -- ip of client
    """
    db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "tasks")
    cursor = db_tasks.cursor()

    sql = """UPDATE tasks
             SET is_solved = 1
             WHERE task_id = {}""".format(task_id)
    cursor.execute(sql)

    res = """INSERT INTO results(task_id, result, author)
             VALUES(%s, %s, %s)"""
    cursor.execute(res, (task_id, result, client))
    db_tasks.commit()
    db_tasks.close()
