import json
from datetime import datetime

import falcon

import {{cookiecutter.project_name}}.config as cnf
from {{cookiecutter.project_name}}.lib import errors

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict


class Index:
    def on_get(self, req, resp):
        if req.path == "/":
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({"server": "%s" % cnf.BRAND_NAME})
        else:
            raise errors.NotSupportedError(method="GET", url=req.path)


class BaseResource:
    def on_error(self, resp, error):
        resp.status = error["status"]
        meta = OrderedDict()
        meta["code"] = error["code"]
        meta["message"] = error["message"]

        resp.body = BaseResource.to_json({"meta": meta})

    def on_success(self, resp, data=None):
        resp.status = falcon.HTTP_200
        meta = OrderedDict()
        meta["code"] = 200
        meta["message"] = "OK"

        resp.body = BaseResource.to_json({"meta": meta, "data": data})

    def on_get(self, req, resp, *args, **kwargs):
        raise errors.NotSupportedError(method="GET", url=req.path)

    def on_post(self, req, resp, *args, **kwargs):
        raise errors.NotSupportedError(method="POST", url=req.path)

    def on_put(self, req, resp, *args, **kwargs):
        raise errors.NotSupportedError(method="PUT", url=req.path)

    def on_delete(self, req, resp, *args, **kwargs):
        raise errors.NotSupportedError(method="DELETE", url=req.path)

    @staticmethod
    def to_json(body: dict):
        return json.dumps(body)
