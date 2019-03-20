"""This is the module to connect database
and work with it"""


import MySQLdb


class Jobs:
    """Class Jobs implements methods jobs 
    connection with database"""

    @staticmethod
    def get_job():
        """Return random available job from DB"""

        db_jobs = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_jobss.cursor()
        sql = """SELECT * FROM Jobs
                 WHERE status = 'new'
                 ORDER BY RAND()
                 LIMIT 1"""

        cursor.execute(sql)

        job = cursor.fetchall()
        db_jobs.close()
        job = {"job_id": task[0][0],
               "type": task[0][1],
               "status": task[0][2],
               "result": task[0][3],
               "ctime": task[0][4],
               "mtime": task[0][5],
               "config": task[0][6]
        }
        return job

    @staticmethod
    def in_progress(job_id):
        """Update statuse of job as in progress

        job_id -- id of the task"""
        db_jobs = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_jobs.cursor()

        jobs_sql = """UPDATE Jobs
                      SET status = 'in_progress'
                      WHERE job_id = %s"""

        cursor.execute(jobs_sql, (job_id))

        db_jobs.commit()
        db_jobs.close()

    @staticmethod
    def done(job_id):
        """Set statuse done - true, new and in 
        progress - false

        Positional argument:
        job_id -- id of solved job
        """

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
        """Set new - false, in_progress - false, client - NULL
        if job was not done successfully

        Positional argument:
        job_id -- id of failed job
        """
        db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_tasks.cursor()

        sql = """UPDATE Tasks
                 SET new = 0, in_progress = 0, client = NULL
                 WHERE task_id = {}""".format(job_id)
        cursor.execute(sql)

        db_tasks.commit()
        db_tasks.close()

    @staticmethod
    def update_result(job_id, result, client):
        """Update task as solved and
        write result into database

        Positional arguments:
        job_id -- id of the task
        result -- result of task
        client -- ip of client who solved job
        """
        db_tasks = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_tasks.cursor()

        res = """INSERT INTO Results(task_id, result, client)
                 VALUES(%s, %s, %s)"""

        cursor.execute(res, (job_id, result, client))

        db_tasks.commit()
        db_tasks.close()

