import json
import unittest

from nose.tools import assert_equal


"""
from truecallerapp.main import create_app


class TestTruecallerapp(unittest.TestCase):

    def setUp(self):
        app = create_app("truecallerapp.settings.DevConfig", 'dev')
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_add(self):
        '''An example test.'''
        assert_equal(1 + 1, 2)


def json_response(response, code=200):
    '''Checks that the status code is OK and returns the json as a dict.'''
    assert_equal(response.status_code, code)
    return json.loads(response.data)

if __name__ == '__main__':
    unittest.main()
"""