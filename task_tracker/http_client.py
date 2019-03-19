"""This module is for create http client"""


import http.client, urllib.parse
import argparse, requests
import logging
import logging.config
from db_conn import update_result, is_available
from jobs import *


logging.config.fileConfig('log.conf')
# create logger
logger = logging.getLogger('clientLogger')

PORT = 8000
conn = http.client.HTTPConnection("localhost", PORT)
conn.request("GET", "")
r1 = conn.getresponse()
task_list = r1.read().decode().split('\r\n')
client = task_list[-1]

parser = argparse.ArgumentParser(description='Choose task TODO: ')
parser.add_argument('-task', action='store', type=int,
                    help='Choose number of task ')
parser.add_argument('-file', action='store', default='task1.txt',
                    help='Enter file name (task1.txt -default)')
parser.add_argument('-dir', action='store', default='/home/oleksandr/test_dir',
                    help='Enter dir path (/home/oleksandr/test_dir -default)')
parser.add_argument('--show', action='store_true', help='Show available jobs')

args = parser.parse_args()

if args.show:
    for task in task_list[:-1]:
        print(task)

task_id = args.task
logger.info(f'client - {client} choosed job {task_id}')
if task_id != None and is_available(task_id) != 1:
    if task_id == 1:
        try:
            result = job1(args.file)
            update_result(task_id, result, client)
            status_code = 200
            print(result)
            logger.info(f'Job was done successfully: \nResult{result}')
        except FileNotFoundError:
            status_code = 404
            logger.error(f'No such file!{args.file}')
            print(f'No such file!{args.file}')
    elif task_id == 2:
        try:
            result = job2(args.dir)
            update_result(task_id, result, client)
            status_code = 201
            print(result)
            logger.info(f'Job was done successfully: \nResult{result}')
        except FileExistsError:
            status_code = 400
            print(f'{args.dir} directory already exist, try to create another!')
            logger.error(f'{args.dir} directory already exist, try to create another!')
    elif task_id == 3:
        try:
            result = job3(args.dir)
            update_result(task_id, result, client)
            status_code = 200
            print(result)
            logger.info(f'Job was done successfully: \nResult{result}')
        except FileNotFoundError:
            status_code = 404
            print(f'No such directory: {args.dir}')
            logger.error(f'No such directory: {args.dir}')
    elif task_id == 4:
        try:
            result = job4()
            update_result(task_id, result, client)
            status_code = 200
            print(result)
            logger.info(f'Job was done successfully: \nResult{result}')
        except:
            status_code = 400
            print('Smth was wrong')
            logger.error('Smth was wrong')
    elif task_id == 5:
        try:
            result = job5()
            update_result(task_id, result, client)
            status_code = 200
            print(result)
            logger.info(f'Job was done successfully: \nResult{result}')
        except:
            status_code = 400
            print('Smth was wrong!')
            logger.error('Smth was wrong!')
    else:
        print('No any available tasks with such id')
        logger.info('No any available tasks with such id')
    params = urllib.parse.urlencode({'status': status_code})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn.request("POST", "", params, headers)

    response = conn.getresponse()
else:
    print('You didn`t choose any task or task is unavailable')
    logger.error('Client didn`t choose any task or task is unavailable')
    params = urllib.parse.urlencode({'status': 400})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn.request("POST", "", params, headers)

    response = conn.getresponse()
conn.close()
