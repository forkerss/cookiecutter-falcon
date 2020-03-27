import unittest

from falcon import MEDIA_JSON, testing

from {{cookiecutter.project_name}}.main import create_app
from tests.base import MyTestCase


class TestApiIndex(MyTestCase):
    def test_index(self):
        """index
        """
        resp = self.simulate_get('/')
        self.assertEqual(
            resp.json, {'server': "Falcon REST API Template"})


if __name__ == "__main__":
    unittest.main()
