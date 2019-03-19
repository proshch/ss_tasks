"""This is the module to connect database
and work with it"""


import MySQLdb

class Jobs:
    """docstring for Jobs"""
    @staticmethod
    def get_task():
        """Return the status of task accessibility"""

        db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_tasks.cursor()
        
        sql = """SELECT * FROM Tasks
                 WHERE in_progress = false and done = false
                 ORDER BY RAND()
                 LIMIT 1"""
        
        cursor.execute(sql)

        task = cursor.fetchall()
        db_tasks.close()
        job = {"id": task[0][0],
                "title": task[0][1],
                "description": task[0][2],
                "new": task[0][3],
                "in_progress": task[0][4],
                "done": task[0][5]
        }
        return job

    @staticmethod
    def in_progress(job_id):
        """Update task as solved and
        write result into database

        Positional arguments:
        task_id -- id of the task
        result -- result of tasks
        client -- ip of client
        """
        db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_tasks.cursor()

        sql = """UPDATE Tasks
                SET in_progress = 1
                WHERE task_id = {}""".format(job_id)
        cursor.execute(sql)

        db_tasks.commit()
        db_tasks.close()

    @staticmethod
    def done(job_id):
        db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_tasks.cursor()

        sql = """UPDATE Tasks
                 SET done = 1
                 WHERE task_id = {}""".format(job_id)
        cursor.execute(sql)

        db_tasks.commit()
        db_tasks.close()
