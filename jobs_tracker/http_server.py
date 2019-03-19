from http.server import HTTPServer, BaseHTTPRequestHandler
from db_conn import Jobs
import json
import logging
from io import BytesIO
from status_code import success_status
from save_results import update_result


PORT = 8000
server_address = ('', PORT)


class Handler(BaseHTTPRequestHandler):
    """Handler for the GET and POST requests """

    def do_GET(self):
        try:
            ip_ad = self.client_address[0]
            select_job = Jobs.get_task(ip_ad)
            code = success_status(select_job['id'])
            job = json.dumps(select_job)
            self.send_response(code)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Send the html message
            self.wfile.write(job.encode())
            logger.info(f"GET request from {ip_ad} | job - {select_job['id']} | status_code: {code}")
        except IndexError as e:
            self.wfile.write(b'No available tasks')
            logger.error(f"GET request from {ip_ad} status_code: 404 - {e}\nNo available tasks")
            self.send_response(404)
        return

    def do_POST(self):
        """Method to processing POST request"""

        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length).decode())   
        job_id = message["job_id"]
        code = message["code"]
        client = message["client"]   
        try:
            result = message["result"]
            update_result(job_id, result, client)
            self.send_response(code)
            logger.info(f"POST request from {client} | job - {job_id} | status_code: {code} | Result:\n{result}\n")
        except KeyError:
            logger.error(f"POST request from {client} | job - {job_id} | status_code: {code} | No result for this job\n")
            self.send_response(code)
        self.end_headers()

if __name__ == '__main__':
    try:
        with HTTPServer(server_address, Handler) as httpd:
            # Create a web server and define the handler to manage the
            # incoming request
            logger = logging.getLogger('HTTPServer')
            logger.setLevel(logging.DEBUG)
            fh = logging.FileHandler('HTTPServer.log')
            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            print("serving at port", PORT)
            httpd.serve_forever()
            logger.info('Starting httpd...\n')
            httpd.socket.close()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        httpd.socket.close()
        logger.info('Stopping httpd...\n')
