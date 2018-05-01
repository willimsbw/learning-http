#!/usr/bin/env python3
#
# Udacity provided all code. Most notes by Bryan Williams.
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

# The classes we need from https.server module
from http.server import HTTPServer, BaseHTTPRequestHandler

# Our handler class, which is a BaseHTTPRequestHandler child (it inherits
# everything from its parent, BaseHTTPRequestHandler)
class HelloHandler(BaseHTTPRequestHandler):
    # The only method in this handler. do_GET means it handles HTTP GET
    #requests. When the server gets a GET request, it will use this function
    # to handle it. Inside this method are methods to send status, headers,
    # and a response body (the necessary components of a response to a GET
    # request.) Note that they're called in order
    def do_GET(self):
        # First, send a 200 OK response. The client already knows what 200
        # means, so there is no need to write "200 OK". The send_response
        # method from BaseHTTPRequestHandler is what we use for this
        self.send_response(200)

        # Then send headers. We use BaseHTTPRequestHandler's send_headers
        # method for this. end_headers is what supplies our blank line.
        # The first arg in send_header is the label, and the second arg is that
        # label's corresponding value.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Now, write the response body. send.wfile is a class from
        # BaseHTTPRequestHandler which we'll use to send the response. wfile
        # stands for writable file. Python makes an analogy between network
        # connections and open files - it expects that network connections are
        # things you can read and write data to. Some file objedcts are
        # read-only, some write-only, and some read-write; like a word doc.
        #
        # self.wfile represents the connection from teh server to the client,
        # and it is write-only (hence writable file). Any binary data written
        # to it with its write method (used here) gets sent ot the client as
        # part of the resposne. In this case, we're writing to client the arg
        # in write's ()'s.
        #
        # The .encode() is there to encode the string we're sending into
        # bytes, because HTTP could be transferring any kind of data, not just
        # a string, and so it expects to receive a binary object. There is
        # also a decode() method for turning bytes back into strings.
        self.wfile.write("Hello, HTTP!\n".encode())


# This code will run when we actually run this file (the first bit is just a
# class declaration).
#
# The HTTPServer constructor needs to know what address and port to listen on
# (in this case, uses the tuple server_address). It's also being passed
# HelloHandler, the class we defined earlier, which the server will use as its
# request handler.
#
# At the end, we call serve_forever on the HTTPServer we just declared
# (httpd), which tells it to open for business (start handling HTTP requests
# sent to it) until closed manually.
if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
