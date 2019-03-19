from logic import Solve
from db_conn import Jobs


def solve_job(job):
    """
    Do job and update status to done
    :param job: job
    """
    if job["id"] == 1:
        try:
            result = Solve.count_unique_words()
            print(result)
            Jobs.done(job["id"])
        except FileNotFoundError:
            print('Can`t find file with words')
    elif job["id"] == 2:
        try:
            result = Solve.make_dir()
            print(result)
            Jobs.done(job["id"])
        except PermissionError:
            print('You don`t have permissions')
        except FileExistsError:
            print('Directory already exist')
    elif job["id"] == 3:
        try:
            result = Solve.remove_dir()
            print(result)
            Jobs.done(job["id"])
        except PermissionError:
            print('You don`t have permission to remove this directory')
        except FileNotFoundError:
            print('Directory Not Found')
    elif job["id"] == 4:
        try:
            result = Solve.dump_command()
            print(result)
            Jobs.done(job["id"])
        except PermissionError:
            print('You don`t have permission to run this command')
    elif job["id"] == 5:
        try:
            result = Solve.generate_random_job()
            print(result)
            Jobs.done(job["id"])
        except PermissionError:
            print('You don`t have permission to run this command')       
    return result

