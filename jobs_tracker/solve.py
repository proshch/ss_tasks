"""Module for checking job_id and exucution it"""


from logic import Solve
from db_conn import Jobs
import json


def solve_job(job):
    """Execute job and update status to done if job successfully
    executed
    :param job: job
    """
    result = None
    config = json.loads(job["config"])
    if job["type"] == 1:
        try:
            result = Solve.count_unique_words(config['path'])
            print(result)
            Jobs.done(job["job_id"])
        except FileNotFoundError:
            fail = 'Can`t find file with words'
            Jobs.failed(job["job_id"], fail)
    elif job["type"] == 2:
        try:
            result = Solve.make_dir(config['path'])
            print(result)
            Jobs.done(job["job_id"])
        except FileExistsError:
            fail = 'Directory already exist'
            print(fail)
            Jobs.failed(job["job_id"], fail)
    elif job["type"] == 3:
        try:
            result = Solve.remove_dir(config['path'])
            print(result)
            Jobs.done(job["job_id"])
        except FileNotFoundError:
            fail = 'Directory Not Found'
            Jobs.failed(job["job_id"], fail)
    elif job["type"] == 4:
        try:
            result = Solve.dump_command(config['command'])
            print(result)
            Jobs.done(job["job_id"])
        except PermissionError:
            fail = 'You don`t have permission to run this command'
            Jobs.failed(job["job_id"], fail)
    elif job["type"] == 5:
        try:
            result = Solve.generate_random_job(config['count'])
            print(result)
            Jobs.done(job["job_id"])
        except:
            fail = 'You don`t have permission to run this command'
            Jobs.failed(job["job_id"], fail)
    return result

