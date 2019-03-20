import http.client
import json
import logging
import time
from status_code import success_status
from solve import solve_job
from db_conn import Jobs


PORT = 8000
conn = http.client.HTTPConnection("localhost", PORT)
conn.request("GET", "")

try:
    response_get = conn.getresponse()
    job = response_get.read().decode()
    job = json.loads(job)
    Jobs.in_progress(job["job_id"])
    result = solve_job(job)
    print(result)
    if result:
        code = success_status(job["type"])
        params = json.dumps({"job_id": job["job_id"], "result": result, "code": code})
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        conn.request("POST", "", params, headers)
        response = conn.getresponse()
        conn.close()
    else:
        params = json.dumps({"job_id": job["job_id"], "code": 400})
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        conn.request("POST", "", params, headers)
        response = conn.getresponse()
        conn.close()
except http.client.RemoteDisconnected:
    print('Remote Disconnected!')
except http.client.BadStatusLine:
    print('No available tasks!')


