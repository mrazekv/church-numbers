import re
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json

import urllib
PORT_NUMBER = 8080

try:
    zalm_cache = json.load(open("zalm_cache.json", "r"))
except:
    zalm_cache = []
    

# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)


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

                
        elif self.path == "/get_zalm":
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(display_global.get_zalm().encode())
            
        elif self.path == "/get_status":
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            self.wfile.write(json.dumps(display_global.get_status(), indent=4).encode())
        
        elif self.path == "/get_zalm_cache":
            global zalm_cache
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            
            js = json.dumps(zalm_cache)
            self.wfile.write(js.encode())
            
        elif self.path.startswith("/remove_zalm_cache_"):
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            data = self.path.split("_")
            if len(data) != 4:
                self.wfile.write("FAIL bad datalen".encode())
                return
            try:
                zalm_cache.remove(data[-1])
                json.dump(zalm_cache, open("zalm_cache.json", "w"))
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
    
    def do_POST(self):
        global display_global
        global zalm_cache
        
        if self.path == "/set_zalm":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            post_data =  urllib.parse.unquote_plus(post_data.decode())
            post_data = re.sub(r"\s+", " ", post_data)
            # decode post_data           
            
            if post_data not in zalm_cache:
                zalm_cache.append(post_data)
                json.dump(zalm_cache, open("zalm_cache.json", "w"))
            
            display_global.set_zalm(post_data)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode())
            return
        elif self.path == "/remove_zalm_cache":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = urllib.parse.unquote_plus(post_data.decode())
            if post_data in zalm_cache:
                zalm_cache.remove(post_data)
                json.dump(zalm_cache, open("zalm_cache.json", "w"))
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode())
        
        else:
            self.send_error(404, 'Post file Not Found: %s' % self.path)
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
        print("Web stopping")
        self.server.shutdown()
        self.server.socket.close()
        print("Web stopped")
        # tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    try:
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print('Started httpserver on port ', PORT_NUMBER)

        # Wait forever for incoming htto requests
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
