import http.client
import json
import logging
import time
from status_code import success_status
from solve import solve_job


PORT = 8000
conn = http.client.HTTPConnection("localhost", PORT)

client = 'client 2'
try:
    while True:
        try:
            conn.request("GET", "")
            response_get = conn.getresponse()
            job = response_get.read().decode()
            job = json.loads(job)
            result = solve_job(job)

            if result['Success']:
                code = success_status(job["type"])
                params = json.dumps({"job_id": job["job_id"], "status": 'done',
                                     "client": client, "result": result['Success'],
                                     "code": code})
                headers = {"Content-type": "application/x-www-form-urlencoded",
                           "Accept": "text/plain"}
                conn.request("POST", "", params, headers)
                response = conn.getresponse()
                conn.close()
            else:
                params = json.dumps({"job_id": job["job_id"], "status": 'failed', 
                                     "client": client, "result": result['Failed'],
                                     "code": 400})
                headers = {"Content-type": "application/x-www-form-urlencoded",
                           "Accept": "text/plain"}
                conn.request("POST", "", params, headers)
                response = conn.getresponse()
                conn.close()

        except http.client.RemoteDisconnected:
            print('Remote Disconnected!')
        except http.client.BadStatusLine:
            conn.close()
            print('No available tasks!')

        time.sleep(10)
except KeyboardInterrupt:
    print('Client stop working!')
