from {{cookiecutter.project_name}} import config as cnf
from {{cookiecutter.project_name}}.lib import errors


class Filter:
    """Filter
    """

    def process_request(self, req, resp):
        # allow methods
        if not req.method in cnf.ALLOW_METHODS:
            raise errors.NotSupportedError(method=req.method, url=req.url)
