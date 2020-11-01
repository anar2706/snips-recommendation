from app import create_app
from flask import current_app

import logging
logging.basicConfig(level=logging.ERROR)
import os
import json
import unittest

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

 
 

class BasicsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('test.json')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Whelp' in response.get_data(as_text=True))

    def test_api_resposne(self):
        response = self.client.post('/nlu',data=json.dumps({"sentence":"How is weather in Singapur"}),
        content_type='application/json',)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        logging.debug(data['slots'][0]['rawValue'])
        self.assertEqual(data['slots'][0]['rawValue'],'Singapur')

 
if __name__ == "__main__":
    unittest.main()