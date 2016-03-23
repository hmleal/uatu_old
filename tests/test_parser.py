import unittest

from uatu.http_server import request_parse
from uatu.http_server import request_file


class TestParser(unittest.TestCase):
    def test_parser(self):
        request_headers = '''GET / HTTP/1.1
        Host: localhost:9000'''

        expected = request_parse(request_headers)
        found = {
            'PATH_INFO': '/',
            'REQUEST_METHOD': 'GET',
            'SERVER_NAME': 'localhost:9000',
            'SERVER_PORT': 9000
        }

        self.assertEquals(expected, found)

    def test_file_exists(self):
        self.assertEquals(request_file('/var/www/uatu/uatu/index.html'), 'text/html')