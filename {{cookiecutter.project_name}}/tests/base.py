from falcon import MEDIA_JSON, testing
from {{cookiecutter.project_name}}.main import create_app


class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()
        self.app = create_app(testing=True)
