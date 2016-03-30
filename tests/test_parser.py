import unittest

from uatu import http_server


class TestParser(unittest.TestCase):
    def test_parser(self):
        request_headers = '''GET / HTTP/1.1
        Host: localhost:9000'''

        expected = http_server.request_parse(request_headers)
        found = {
            'PATH_INFO': '/',
            'REQUEST_METHOD': 'GET',
            'SERVER_NAME': 'localhost:9000',
            'SERVER_PORT': 9000
        }

        self.assertEquals(expected, found)

    def test_content_type_header(self):
        path = '/var/www/uatu/index.html'
        self.assertEquals(
            'Content-Type: text/html',
            http_server.content_type_header(path)
        )

    def test_path_info_is_valid(self):
        http_server.BASE_DIR = '/'
        self.assertTrue(http_server.path_info_is_valid('/home'))

    def test_is_image_valid(self):
        path = '/var/www/uatu/foto.html'
        self.assertEquals(
            'Content-Type: image/jpeg',
            http_server.content_type_header(path)
        )
