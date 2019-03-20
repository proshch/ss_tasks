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
                 ORDER BY RAND()
                 LIMIT 1"""

        cursor.execute(sql)

        job = cursor.fetchall()
        db_jobs.close()
        job = {"job_id": job[0][0],
               "type": job[0][1],
               "status": job[0][2],
               "result": job[0][3],
               "ctime": str(job[0][4]),
               "mtime": str(job[0][5]),
               "config": job[0][6]
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

        cursor.execute(jobs_sql, (job_id, ))

        db_jobs.commit()
        db_jobs.close()

    @staticmethod
    def done(job_id):
        """Set statuse done - true, new and in 
        progress - false

        Positional argument:
        job_id -- id of solved job
        """

        db_jobs = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_jobs.cursor()

        sql = """UPDATE Jobs
                 SET status = 'done'
                 WHERE job_id = %s"""

        cursor.execute(sql, (job_id, ))

        db_jobs.commit()
        db_jobs.close()

    @staticmethod
    def update_result(job_id, result):
        """Update task as solved and
        write result into database

        Positional arguments:
        job_id -- id of the task
        result -- result of task
        """
        db_jobs = MySQLdb.connect("localhost", "oleksandr", "K@tchi1899", "jobs_tracker")
        cursor = db_jobs.cursor()

        res = """UPDATE Jobs
                 SET result = %s
                 WHERE job_id = %s"""

        cursor.execute(res, (result, job_id))

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
                 SET status = 'failed', result = %s
                 WHERE job_id = %s"""

        cursor.execute(sql, (fail, job_id))

        db_jobs.commit()
        db_jobs.close()
