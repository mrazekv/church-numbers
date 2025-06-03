import os
import re
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import json
import urllib
from display import displayApp

PORT_NUMBER = 8080

# Singleton AppData
class AppData:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AppData, cls).__new__(cls, *args, **kwargs)
            print("AppData new")
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            print("AppData init")
            self.data = {}
            
    def setDisplay(self, display : displayApp):
        self.display = display
        
    def fillZalmCache(self):
        try:
            self.zalm_cache = json.load(open("zalm_cache.json", "r"))
        except Exception as e:
            print(f"Error loading zalm_cache: {e}")
            self.zalm_cache = []
        
    def removeZalmCache(self, zalm):        
        self.zalm_cache.remove(zalm)
        json.dump(self.zalm_cache, open("zalm_cache.json", "w"))
        
    def appendZalmCache(self, zalm):
        if zalm not in self.zalm_cache:
            self.zalm_cache.append(zalm)
            json.dump(self.zalm_cache, open("zalm_cache.json", "w"))
            return True
        return False
    
    def get_wifi_signal(self):
        try:
            
            with open("/proc/net/wireless", "r") as f:
                return f.read()
                for line in f:
                    if "wlan0" in line:
                        return line
        except Exception as e:
            return str(e)
        
    def get_uptime(self):
        try:
            # call uptime command and return stdout
            res = subprocess.run(["uptime"], stdout=subprocess.PIPE)
            return res.stdout.decode("utf-8")
            
        except Exception as e:
            return str(e)
        
    def get_date_time(self):
        try:
            # call date command and return stdout
            res = subprocess.run(["date"], stdout=subprocess.PIPE)
            return res.stdout.decode("utf-8")
        except Exception as e:
            return str(e)  
        
    

# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)


    # Handler for the GET requests
    def do_GET(self):
        appData = AppData()
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
                appData.display.set_number(data[1])
                self.wfile.write("OK".encode())
            except Exception as e:
                self.wfile.write(f"FAIL {e}".encode())

                
        elif self.path == "/get_zalm":
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(appData.display.get_zalm().encode())
            
        elif self.path == "/reload_config":
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            try:
                appData.display.reload_config()
                self.wfile.write("OK".encode())
            except Exception as e:
                self.wfile.write(f"FAIL {e}".encode())
            
        elif self.path == "/get_status":
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            self.wfile.write(json.dumps(appData.display.get_status(), indent=4).encode())
        
        elif self.path == "/get_zalm_cache":
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            
            js = json.dumps(appData.zalm_cache, indent=2)
            self.wfile.write(js.encode())
            
        elif self.path.startswith("/remove_zalm_cache_"):
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            data = self.path.split("_")
            if len(data) != 4:
                self.wfile.write("FAIL bad datalen".encode())
                return
            try:
                appData.remove_zalm_cache(data[-1])
                self.wfile.write("OK".encode())
            except Exception as e:
                self.wfile.write(f"FAIL {e}".encode())
                
        elif self.path.startswith("/status"):
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            try:
                # return html status page with json status of display, strenght of wifi signal, uptime and date time. Formatted as pre tag
                ret = f"""
                <html>  
                <head>
                <meta http-equiv="refresh" content="5">
                </head>
                <body>
<pre><b>Status:</b> {json.dumps(appData.display.get_status(), indent=4)}
                
<b>System status:</b>
{appData.get_wifi_signal()}
<b>Uptime:</b> {appData.get_uptime()}
<b>Date:</b> {appData.get_date_time()}

                </pre>
                </body>
                </html>
                """
                self.wfile.write(ret.encode())
                
            except Exception as e:
                self.wfile.write(f"FAIL {e}".encode())

        elif self.path.startswith("/get"):
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            try:
                self.wfile.write(appData.display.get_number().encode())
            except Exception as e:
                self.wfile.write(f"FAIL {e}".encode())
                
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

        return
    
    def do_POST(self):
        appData = AppData()
        
        if self.path == "/set_zalm":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            post_data =  urllib.parse.unquote_plus(post_data.decode())
            post_data = re.sub(r"\s+", " ", post_data)
            # decode post_data          

            appData.appendZalmCache(post_data)            
                        
            appData.display.set_zalm(post_data)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode())
            return
        elif self.path == "/remove_zalm_cache":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = urllib.parse.unquote_plus(post_data.decode())
            appData.removeZalmCache(post_data)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode())
            
        elif self.path == "/set_status":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = urllib.parse.unquote_plus(post_data.decode())
            post_data = json.loads(post_data)
            appData.display.set_status(post_data)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode())
        
        else:
            self.send_error(404, 'Post file Not Found: %s' % self.path)
            return



class webThread(threading.Thread):
    def __init__(self, display : displayApp, port : int = PORT_NUMBER):
        threading.Thread.__init__(self)
        self.display = display
        self.appdata = AppData()
        self.appdata.setDisplay(display)
        self.appdata.fillZalmCache()
        self.port = port

    def run(self):

        self.server = HTTPServer(('', self.port), myHandler)
        print('Started httpserver on port ', self.port)

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


if __name__ == "__main__":
    try:
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print('Started httpserver on port ', PORT_NUMBER)
        
        # Wait forever for incoming htto requests
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
