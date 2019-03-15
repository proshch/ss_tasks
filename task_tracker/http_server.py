"""This module is to create a very basic webserver serving"""


from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import logging
import logging.config
from db_conn import get_tasks

logging.config.fileConfig('log.conf')
# create logger
logger = logging.getLogger('serverLogger')

PORT = 8000
server_address = ('', PORT)

class Handler(BaseHTTPRequestHandler):
    """Handler for the GET and POST requests """
    def do_GET(self):
        """Method to processing GET request """
        try:
            tasks = get_tasks()
            message = '\r\n'.join(tasks)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(message.encode())
            ip_ad = '\r\n'+self.client_address[0]
            self.wfile.write(ip_ad.encode())
            logger.info(f'GET REQUEST: client - {ip_ad} status code = 200')
        except NameError:
            self.send_response(400)
            ip_ad = '\r\n'+self.client_address[0]
            logger.error(f'GET REQUEST: client - {ip_ad} status code = 400')
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        return

    def do_POST(self):
        """Method to processing POST request"""

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        status = body.decode()
        self.send_response(int(status[-3:]))
        self.end_headers()
        response = BytesIO()
        response.write(body)
        ip_ad = self.client_address[0]
        logger.info(f'POST REQUEST client - {ip_ad} {status}')

if __name__ == '__main__':
    try:
        with HTTPServer(server_address, Handler) as httpd:
            #Create a web server and define the handler to manage the
            #incoming request
            print("serving at port", PORT)
            httpd.serve_forever()
            httpd.socket.close()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        httpd.socket.close()
