"""Module to implement http client"""


import http.client
import json
import logging
import time
from status_code import success_status
from solve import solve_job


FORMAT = '%(asctime)-15s %(filename)s %(message)s'
logging.basicConfig(
                    level=logging.DEBUG,
                    format=FORMAT,
                    filename='http.log',
                    filemode='a')

logger = logging.getLogger('HttpClient')

PORT = 8000
conn = http.client.HTTPConnection("localhost", PORT)
logger.info('Client start working!\n')

try:
    while True:
        try:
            conn.request("GET", "")
            response_get = conn.getresponse()
            job = response_get.read().decode()
            job = json.loads(job)
            result = solve_job(job)
            logger.info(f'GET - {response_get.status} {response_get.reason}: job_id: {job["job_id"]}')
            if result['Success']:
                code = success_status(job["type"])
                params = json.dumps({"job_id": job["job_id"], "status": 'done',
                                    "result": result['Success'], "code": code})
                headers = {"Content-type": "application/x-www-form-urlencoded",
                           "Accept": "text/plain"}
                conn.request("POST", "", params, headers)
                response = conn.getresponse()
                conn.close()
                logger.info(f'POST - {response.status} {response.reason}: job_id: {job["job_id"]} {result["Success"]}')
            else:
                params = json.dumps({"job_id": job["job_id"], "status": 'failed', 
                                     "result": result['Failed'], "code": 400})
                headers = {"Content-type": "application/x-www-form-urlencoded",
                           "Accept": "text/plain"}
                conn.request("POST", "", params, headers)
                response = conn.getresponse()
                conn.close()
                logger.error(f'POST - {response.status} {response.reason}: job_id: {job["job_id"]} {result["Failed"]}\n')
        except http.client.RemoteDisconnected:
            logger.error('Remote Disconnected!')
        except http.client.BadStatusLine:
            conn.close()
        time.sleep(5)
except KeyboardInterrupt:
    logger.info('Client stopped working!\n')
