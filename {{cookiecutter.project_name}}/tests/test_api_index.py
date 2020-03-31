import unittest

from tests.base import TestCaseBase


class TestApiIndex(TestCaseBase):
    def test_index(self):
        """index
        """
        resp = self.simulate_get('/')
        self.assertEqual(
            resp.json, {'server': "Falcon REST API Template"})


if __name__ == "__main__":
    unittest.main()
