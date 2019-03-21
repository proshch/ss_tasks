"""Module for checking job_id and exucution it"""


from logic import Solve
from db_conn import Jobs
import json


def solve_job(job):
    """Execute job and update status to done if job successfully
    executed
    :param job: job
    """


    result = {'Success': None, 'Failed': None}
    config = json.loads(job["config"])
    if job["type"] == 1:
        try:
            result['Success'] = Solve.count_unique_words(config['path'])
        except FileNotFoundError:
            result['Failed'] = 'Can`t find file with words'
    elif job["type"] == 2:
        output = Solve.make_dir(config['path'])
        if output[0]:
            result['Success'] = output[0].decode()
        else:
            result['Failed'] = output[1].decode()
            if result['Failed'] == 'None' or result['Failed'] == '':
                result['Failed'] = 'Directory already exists'
    elif job["type"] == 3:
        output = Solve.remove_dir(config['path'])
        if output[0]:
            result['Success'] = output[0].decode()
        else:
            result['Failed'] = output[1].decode()
            if result['Failed'] == 'None' or result['Failed'] =='':
                result['Failed'] = 'Such file not exists'
    elif job["type"] == 4:
        output = Solve.dump_command(config['command'])
        if output[0]:
            result['Success'] = output[0].decode()
        else:
            result['Failed'] = output[1].decode()
    elif job["type"] == 5:
        try:
            result['Success'] = Solve.generate_random_job(config['count'])
        except:
            result['Failed'] = 'You don`t have permission to run this command'
    return result

