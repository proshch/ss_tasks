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
        cursor = db_jobs.cursor()
        sql = """SELECT * FROM Jobs
                 WHERE status = 'new'
                 ORDER BY ctime DESC"""

        cursor.execute(sql)

        job = cursor.fetchone()
        db_jobs.close()
        job = {"job_id": job[0],
               "type": job[1],
               "status": 'in_progress',
               "result": job[3],
               "ctime": str(job[4]),
               "mtime": str(job[5]),
               "config": job[6]
        }
        return job

    @staticmethod
    def in_progress(job_id):
        """Update statuse of job as in progress

        job_id -- id of the task"""
        db_jobs = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_jobs.cursor()

        jobs_sql = """UPDATE Jobs
                      SET status = 'in_progress', mtime = now()
                      WHERE job_id = %s"""

        cursor.execute(jobs_sql, (job_id, ))

        db_jobs.commit()
        db_jobs.close()

    @staticmethod
    def update_result(job_id, status, result):
        """Update task as solved and
        write result into database

        Positional arguments:
        job_id -- id of the task
        status -- status
        result -- result of task
        """
        db_jobs = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_jobs.cursor()

        res = """UPDATE Jobs
                 SET status = %s, result = %s, mtime = now()
                 WHERE job_id = %s"""

        cursor.execute(res, (status, result, job_id))

        db_jobs.commit()
        db_jobs.close()

    @staticmethod
    def failed(job_id, fail):
        """Set statuse done - true, new and in
        progress - false

        Positional argument:
        job_id -- id of solved job
        """

        db_jobs = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_jobs.cursor()

        sql = """UPDATE Jobs
                 SET status = 'failed', result = %s, mtime = now()
                 WHERE job_id = %s"""

        cursor.execute(sql, (fail, job_id))

        db_jobs.commit()
        db_jobs.close()
