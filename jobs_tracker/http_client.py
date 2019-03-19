import http.client
import json
import urllib.parse
from solve import solve_job
from db_conn import Jobs


PORT = 8000
conn = http.client.HTTPConnection("localhost", PORT)
conn.request("GET", "")
try:
    response_get = conn.getresponse()
    job = response_get.read().decode()
    job = json.loads(job)
    Jobs.in_progress(job["id"])
    solve_job(job)

    params = urllib.parse.urlencode({'job_id': job["id"]})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    conn.close()
except http.client.RemoteDisconnected:
    print('No available tasks!')



