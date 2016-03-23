#!/usr/bin/env python
import os
import socket
import os
import urllib2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOCK_ADDRESS = ('127.0.0.1', 9000)


def check_path_info(path_info):
    if not path_info:
        path_info = '/index.html'
    return os.path.join(BASE_DIR, path_info[1:])


def request_parse(text):
    lines = text.splitlines()
    request_method = lines[0].rstrip('\r\n').split()
    server_name = lines[1].rstrip('\r\n').split()

    return {
        'REQUEST_METHOD': request_method[0],
        'PATH_INFO': request_method[1],
        'SERVER_NAME': server_name[1],
        'SERVER_PORT': 9000
    }


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(SOCK_ADDRESS)

    sock.listen(1)

    header = '''HTTP/1.0 200 OK
        Content-Type: text/html

        <h1>Example</h1>'''

    while 1:
        connection, address = sock.accept()
        request = connection.recv(1024)

        environ = request_parse(request)
        print(check_path_info(environ['PATH_INFO']))

        if not request:
            break
        connection.sendall(header)
        connection.close()

def request_file(self):
    try:
        if os.path.isfile(self):
            if self.endswith('.html'):
                return 'text/html'
            if self.endswith('.jpg'):
                return 'image/jpeg'
        else:
            return False
    except urllib2.HTTPError, err:
        if err.code == 404:
            print 'Arquivo nao encontrado!'