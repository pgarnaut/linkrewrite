'''
    Created on Jun 22, 2013

    @author:  pgarnaut
'''

from django.test import TestCase
from django.test.client import Client
from permalink.linkrewrite.models import Link

class SimpleTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def verify_http_success(self, resp, expected_status=200):
        self.assertEqual(resp.status_code, expected_status, 'HTTP %d error: %s' % (resp.status_code, resp.content))
    
    def test_create_link(self):
        """
        """
        client = Client()

        resp = client.post(
            '/link/', 
            data={'foobar': 'got this stuff'},
        )
        self.verify_http_success(resp, expected_status=200)
