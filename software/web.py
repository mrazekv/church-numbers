import os
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from glob import glob
import os
import time
PORT_NUMBER = 8080


# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        global display_global
        # Send the html message
        self.send_response(200)

        if self.path == "/":
            self.path = "/index.html"

        if self.path in ["/bootstrap.min.css", "/bootstrap.min.js", "/favicon.ico", "/index.html", "/jquery-3.3.1.min.js", "/popper.min.js"]:

            if self.path.endswith(".css"):
                self.send_header("Content-type", "text/css")

            elif self.path.endswith(".js"):
                self.send_header("Content-type", "text/javascript")
            elif self.path.endswith(".ico"):
                self.send_header("Content-type", "image/x-icon")
            else:
                self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open("files" + self.path, "rb") as f:
                self.wfile.write(f.read())

        elif self.path.startswith("/display_"):
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # self.wfile.write(self.path)

            data = self.path.split("_")
            if len(data) != 2 or len(data[1]) != 5:
                self.wfile.write("FAIL bad datalen".encode())
                return

            try:
                display_global.set_number(data[1])
                self.wfile.write("OK".encode())
            except Exception as e:
                self.wfile.write(f"FAIL {e}".encode())

        elif self.path.startswith("/get"):
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            try:
                self.wfile.write(display_global.get_number().encode())
            except Exception as e:
                self.wfile.write(f"FAIL {e}".encode())
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

        return


class webThread(threading.Thread):
    def __init__(self, display):
        threading.Thread.__init__(self)
        self.display = display
        global display_global
        display_global = display

    def run(self):

        self.server = HTTPServer(('', PORT_NUMBER), myHandler)
        print('Started httpserver on port ', PORT_NUMBER)

        # Wait forever for incoming htto requests
        try:
            self.server.serve_forever()
        except:
            pass

    def stop(self):
        print("Tornado stopping")
        self.server.socket.close()
        print("Tornado stopped")
        # tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    try:
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print('Started httpserver on port ', PORT_NUMBER)

        # Wait forever for incoming htto requests
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
