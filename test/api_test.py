import os
import sys
import json
import pytest
from unittest import TestCase

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from config import app

class TestIntegrations(TestCase):
    def setUp(self):
        self.twitter_acc = "Zemoga"
        self.app = app.test_client()

    def test_text(self):
        rv = self.app.get('test')
        print(rv)

        assert rv.status_code == 200

    def test_create(self):
        rv = self.app.post('/profile',
            data={
                "title": "title_test",
                "user_info": "user_info_test",
                "image":"https://logos-marcas.com/wp-content/uploads/2020/12/Batman-Logo.png",
                "description":"description_test",
                "twitter": self.twitter_acc
            }
        )

        json_data = rv.get_json()
        assert self.twitter_acc == json_data['twitter']

    def test_get(self):
        print("=================================")
        rv = self.app.get(f'/profile/{self.twitter_acc}')

        print(rv)
        json_data = rv.get_json()
        print(json_data)
        assert self.twitter_acc == json_data['twitter']

        rv = self.app.delete(f'/profile/{self.twitter_acc}')
        assert b'true' in rv.data
