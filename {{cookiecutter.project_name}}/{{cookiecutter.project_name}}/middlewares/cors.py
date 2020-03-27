import falcon
from falcon.http_status import HTTPStatus

from {{cookiecutter.project_name}} import config as cnf


class CORS:
    """Handle CORS
    """

    def __init__(self, testing=False):
        self._testing = testing

    def process_request(self, req, resp):
        if self._testing:
            # Allow origin all when debugging
            resp.set_header('Access-Control-Allow-Origin', '*')
        else:
            origin = req.get_header('ORIGIN', "")
            if origin and origin.startswith("http://%s" % cnf.DOMAIN):
                resp.set_header('Access-Control-Allow-Origin', origin)
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 24 * 3600)

        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_200, body='\n')
