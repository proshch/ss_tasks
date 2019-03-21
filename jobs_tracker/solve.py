"""Module for checking job if job was executed successfully or failed"""


from logic import Solve
import json


def solve_job(job):
    """Execute job and check if job was executed successfully or failed
    :param job: job
    :return: result of job execution
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
        if output:
            result['Success'] = output
        else:
            result['Failed'] = 'Directory already exists'
    elif job["type"] == 3:
        output = Solve.remove_dir(config['path'])
        if output:
            result['Success'] = output
        else:
            result['Failed'] = 'No such directory'
    elif job["type"] == 4:
        output = Solve.dump_command(config['command'])
        if output[0]:
            result['Success'] = 'Command was dumped successfully'
            print(output[0].decode())
        else:
            result['Failed'] = output[1].decode()
    elif job["type"] == 5:
        try:
            result['Success'] = Solve.generate_random_job(config['count'])
        except FileNotFoundError:
            result['Failed'] = 'Can`t find file with words'
        except FileExistsError:
            result['Failed'] = 'Directory already exists'
        except Exception as e:
            result['Failed'] = e
    return result

