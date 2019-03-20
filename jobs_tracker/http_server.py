from http.server import HTTPServer, BaseHTTPRequestHandler
from db_conn import Jobs
import json
from status_code import success_status


PORT = 8000
server_address = ('', PORT)


class Handler(BaseHTTPRequestHandler):
    """Handler for the GET and POST requests """

    def do_GET(self):
        """Handle GET request for getting available job"""
        try:
            select_job = Jobs.get_job()
            job = json.dumps(select_job)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Send the html message
            self.wfile.write(job.encode())
        except IndexError:
            self.wfile.write(b'No available tasks')
            self.send_response(404)
        return

    def do_POST(self):
        """Method to processing POST request
        Add done job to results table or send response 400
        if no result for job
        """

        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length).decode())   
        job_id = message["job_id"]
        code = message["code"]
        try:
            result = message["result"]
            Jobs.update_result(job_id, result)
            self.send_response(code)
        except KeyError:
            self.send_response(code)
        self.end_headers()


if __name__ == '__main__':
    try:
        with HTTPServer(server_address, Handler) as httpd:
            # Create a web server and define the handler to manage the
            # incoming request
            print("serving at port", PORT)
            httpd.serve_forever()
            httpd.socket.close()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        httpd.socket.close()

