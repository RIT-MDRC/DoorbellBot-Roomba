from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from routes import REQUESTS, other

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        path = self.path.split('/')[1]

        if path in REQUESTS:
            resp, msg = REQUESTS[path]()
        else:
            resp, msg = other()

        self.send_response(resp)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(msg, "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
