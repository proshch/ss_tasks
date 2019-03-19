import http.client
import json
import sys
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
    Jobs.in_progress(job["id"], job["client"])
    try:
        result = solve_job(job)
        code = success_status(job["id"])
        params=json.dumps({"job_id": job["id"], "result": result, "client": job["client"], "code": code})
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        conn.request("POST", "", params, headers)
        response = conn.getresponse()
        conn.close()
    except:
        Jobs.reset_job_status(job["id"])
        params=json.dumps({"job_id": job["id"], "client": job["client"], "code": 400, "info": 'Result of job not found!'})
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        conn.request("POST", "", params, headers)
        response = conn.getresponse()
        conn.close()
except http.client.RemoteDisconnected:
    print('Remote Disconnected!')
except http.client.BadStatusLine:
    print('No available tasks!')

