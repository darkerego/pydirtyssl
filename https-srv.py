#!/usr/bin/python env
# Quick&Dirty HTTPS Server

import BaseHTTPServer, SimpleHTTPServer
import ssl
import os

os.system("openssl req \
    -new \
    -newkey rsa:4096 \
    -days 365 \
    -nodes \
    -x509 \
    -subj '/C=US/ST=Denial/L=Somewhere/O=Dis/CN=www.yourhacked.bro' \
    -keyout /tmp/server.key \
    -out /tmp/server.crt")

os.system("cat server.crt server.key > /tmp/server.pem")




httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/tmp/server.pem', server_side=True)
print("Serving on 0.0.0.0:4443")
httpd.serve_forever()