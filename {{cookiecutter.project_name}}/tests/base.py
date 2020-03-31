from falcon import testing

from {{cookiecutter.project_name}}.main import create_app


class TestCaseBase(testing.TestCase):
    def setUp(self):
        super(TestCaseBase, self).setUp()
        self.app = create_app(testing=True)
