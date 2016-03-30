#!/usr/bin/env python
import mimetypes
import os
import socket


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOCK_ADDRESS = ('127.0.0.1', 9000)


def get_404():
    return '''HTTP/1.0 404 Not Found
        Content-Type: text/html

        Not Found'''


def request_parse(text):
    lines = [l.rstrip('\r\n') for l in text.splitlines()]
    request_method = lines[0].split()
    server_name = lines[1].split()

    return {
        'REQUEST_METHOD': request_method[0],
        'PATH_INFO': request_method[1],
        'SERVER_NAME': server_name[1],
        'SERVER_PORT': SOCK_ADDRESS[1],
    }


def content_type_header(path_info):
    """
    Return the content type header.
    """
    if path_info == '/':
        path_info = '/index.html'

    filename = path_info.split('/')[-1]
    mimetype = mimetypes.guess_type(filename)

    return 'Content-Type: {0}'.format(mimetype[0])


def path_info_is_valid(path):
    full_path = os.path.join(BASE_DIR, path[1:])
    if os.path.isdir(full_path) or os.path.isfile(full_path):
        return True
    return False


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(SOCK_ADDRESS)

    sock.listen(1)

    response_pattern = '''HTTP/1.0 200 OK
        {content_type}

        {content_body}
        '''

    while 1:
        connection, address = sock.accept()
        request = connection.recv(1024)

        environ = request_parse(request)

        if not request:
            connection.close()
            break

        if path_info_is_valid(environ['PATH_INFO']):
            f = open(environ['PATH_INFO'].split('/')[-1])
            response = response_pattern.format(
                content_type=content_type_header(environ['PATH_INFO']),
                content_body=f.read()
            )
            print(response);
            f.close()
        else:
            response = get_404()

        connection.sendall(response)
        connection.close()
