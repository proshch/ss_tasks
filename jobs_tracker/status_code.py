"""Module for set statuse codes"""

def success_status(job_id):
    """Set success statuse code for different jobs

    Positional argument:
    job_id -- id of job
    """

    if job_id == 1:
        code = 200
    elif job_id == 2:
        code = 201
    elif job_id == 3:
        code = 202
    elif job_id == 4:
        code = 200
    else:
        code = 200
    return code
