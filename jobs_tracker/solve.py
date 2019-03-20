"""Module for checking job_id and exucution it"""


from logic import Solve
from db_conn import Jobs
import json


def solve_job(job):
    """Execute job and update status to done if job successfully
    executed
    :param job: job
    """

    config = json.loads(job["config"])
    if job["type"] == 1:
        try:
            result = Solve.count_unique_words(config)
            print(result)
            Jobs.done(job["job_id"])
        except FileNotFoundError:
            print('Can`t find file with words')
    elif job["job_id"] == 2:
        try:
            result = Solve.make_dir(config)
            print(result)
            Jobs.done(job["job_id"])
        except PermissionError:
            print('You don`t have permissions')
        except FileExistsError:
            print('Directory already exist')
    elif job["id"] == 3:
        try:
            result = Solve.remove_dir(config)
            print(result)
            Jobs.done(job["job_id"])
        except PermissionError:
            print('You don`t have permission to remove this directory')
        except FileNotFoundError:
            print('Directory Not Found')
    elif job["id"] == 4:
        try:
            result = Solve.dump_command(config)
            print(result)
            Jobs.done(job["job_id"])
        except PermissionError:
            print('You don`t have permission to run this command')
    elif job["job_id"] == 5:
        try:
            result = Solve.generate_random_job(config)
            print(result)
            Jobs.done(job["job_id"])
        except PermissionError:
            print('You don`t have permission to run this command')
    return result

