"""This is the module to connect database
and work with it"""


import MySQLdb


def update_result(job_id, result, client):
    """Update task as solved and
    write result into database
    Positional arguments:
    task_id -- id of the task
    result -- result of task
    """
    db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
    cursor = db_tasks.cursor()

    res = """INSERT INTO Results(task_id, result, client)
             VALUES(%s, %s, %s)"""

    cursor.execute(res, (job_id, result, client))

    db_tasks.commit()
    db_tasks.close()

