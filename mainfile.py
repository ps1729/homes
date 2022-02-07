import socket
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import socketserver
import sys
import testHandler

class style1(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        text="<html> <body> Hello </body> </html>"
        self.wfile.write(bytes(text,"utf-8"))

args = sys.argv
print(args)
if ('-h' in args):
    host=args[args.index('-h')+1]
else:
    host='0.0.0.0'

host_name = socket.gethostname()
print(host_name)
ip = socket.gethostbyname(host_name)
print(ip)
if ('-p' in args):
    port=int(args[args.index('-p')+1])
else:
    port=8080

print ("http://"+host+":"+str(port)+'/')
# can use SimpleHTTPRequestHandler for default function
with HTTPServer((host, port), testHandler.testHandler) as server:
 server.serve_forever(
    )
 server.server_close()

 print("Exiting")