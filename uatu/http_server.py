#!/usr/bin/env python
import socket


SOCK_ADDRESS = ('127.0.0.1', 9000)

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

        print(request_parse(request))

        if not request:
            break
        connection.sendall(header)
        connection.close()
