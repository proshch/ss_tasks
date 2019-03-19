"""This is the module to connect database
and work with it"""


import MySQLdb


class Jobs:
    """docstring for Jobs"""
    @staticmethod
    def get_task(ip_ad):
        """Return random available taask from DB"""

        db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_tasks.cursor()
        sql = """SELECT * FROM Tasks
                 WHERE in_progress = false and done = false
                 OR (in_progress = true and client = %s and done = false)
                 ORDER BY RAND()
                 LIMIT 1"""

        cursor.execute(sql, (ip_ad, ))

        task = cursor.fetchall()
        db_tasks.close()
        job = {"id": task[0][0],
                "title": task[0][1],
                "description": task[0][2],
                "new": task[0][3],
                "in_progress": task[0][4],
                "done": task[0][5],
                "client": ip_ad
        }
        return job

    @staticmethod
    def in_progress(job_id, client_name):
        """Update task as solved and
        write result into database

        Positional arguments:
        task_id -- id of the task
        result -- result of tasks
        client -- client
        """
        db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_tasks.cursor()

        tasks_sql = """UPDATE Tasks
                       SET in_progress = 1, new = 0, client = %s
                       WHERE task_id = %s"""

        cursor.execute(tasks_sql, (client_name, job_id))

        db_tasks.commit()
        db_tasks.close()

    @staticmethod
    def done(job_id):
        db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_tasks.cursor()

        sql = """UPDATE Tasks
                 SET done = 1, new = 0, in_progress = 0
                 WHERE task_id = {}""".format(job_id)
        cursor.execute(sql)

        db_tasks.commit()
        db_tasks.close()

    @staticmethod
    def reset_job_status(job_id):
        db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_tasks.cursor()

        sql = """UPDATE Tasks
                 SET new = 0, in_progress = 0, client = NULL
                 WHERE task_id = {}""".format(job_id)
        cursor.execute(sql)

        db_tasks.commit()
        db_tasks.close()

