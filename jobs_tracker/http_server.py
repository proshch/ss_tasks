from http.server import HTTPServer, BaseHTTPRequestHandler
from db_conn import Jobs
import json
import logging
from status_code import success_status

FORMAT = '%(asctime)-15s %(filename)s %(message)s'
logging.basicConfig(
                    level=logging.DEBUG,
                    format=FORMAT,
                    filename='http.log',
                    filemode='a')

logger = logging.getLogger('httpserver')

PORT = 8000
server_address = ('', PORT)


class Handler(BaseHTTPRequestHandler):
    """Handler for the GET and POST requests """

    def do_GET(self):
        """Handle GET request for getting available job"""
        try:
            select_job = Jobs.get_job()
            Jobs.in_progress(select_job["job_id"])
            job = json.dumps(select_job)
            self.send_response(200)
            logger.info(f'GET - 200 OK: job_id: {select_job["job_id"]} {select_job["status"]}')
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Send the html message
            self.wfile.write(job.encode())
        except TypeError:
            self.send_response(404)
            logger.error(f'GET - 404 NOT FOUND - No available jobs')
        return

    def do_POST(self):
        """Method to processing POST request
        Add done job to results table or send response 400
        if no result for job
        """

        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length).decode())
        job_id = message["job_id"]
        status = message["status"]
        code = message["code"]
        try:
            result = message["result"]
            Jobs.update_result(job_id, status, result)
            self.send_response(code)
            logger.info(f'POST - {code}: job_id: {job_id} {status}')
        except KeyError:
            self.send_response(code)
            logger.error(f'POST - {code}: job_id: {job_id} {status}')
        self.end_headers()


if __name__ == '__main__':
    try:
        with HTTPServer(server_address, Handler) as httpd:
            # Create a web server and define the handler to manage the
            # incoming request
            logger.info(f"serving at port {PORT}")
            httpd.serve_forever()
            httpd.socket.close()
    except KeyboardInterrupt:
        logger.info('^C received, shutting down the web server')
        httpd.socket.close()

