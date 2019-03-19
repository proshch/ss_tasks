from http.server import HTTPServer, BaseHTTPRequestHandler
from db_conn import Jobs
import json
from io import BytesIO
from status_code import success_status

PORT = 8000
server_address = ('', PORT)


class Handler(BaseHTTPRequestHandler):
    """Handler for the GET and POST requests """

    def do_GET(self):
        try:
            job = Jobs.get_task()
            code = success_status(job['id'])
            job = json.dumps(job)
            self.send_response(code)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Send the html message
            self.wfile.write(job.encode())
        except IndexError:
            self.send_response(404)
        return

    def do_POST(self):
        """Method to processing POST request"""

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        job_id = body
        code = success_status(job_id)
        self.send_response(code)
        self.end_headers()
        response = BytesIO()
        response.write(body)

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
