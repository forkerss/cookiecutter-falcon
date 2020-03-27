import json

import falcon

try:
    from collections import OrderedDict
except:
    OrderedDict = dict


ERR_INVALID_PARAMETER = {
    "status": falcon.HTTP_400,
    "code": 400,
    "title": "Invalid Parameter"
}
ERR_AUTH_REQUIRED = {
    "status": falcon.HTTP_401,
    "code": 401,
    "title": "Authentication Required"
}
ERR_NOT_SUPPORTED = {
    "status": falcon.HTTP_404,
    "code": 404,
    "title": "Not Supported"
}
ERR_UNKNOWN = {
    "status": falcon.HTTP_500,
    "code": 500,
    "title": "Unknown Error"
}


class AppError(Exception):
    def __init__(self, error=ERR_UNKNOWN, description=None):
        self.error = error
        self.error["description"] = description

    @property
    def code(self):
        return self.error["code"]

    @property
    def title(self):
        return self.error["title"]

    @property
    def status(self):
        return self.error["status"]

    @property
    def description(self):
        return self.error["description"]

    @staticmethod
    def handle(exception, req, resp, error=None):
        resp.status = exception.status
        meta = OrderedDict()
        meta["code"] = exception.code
        meta["message"] = exception.title
        if exception.description:
            meta["description"] = exception.description
        resp.body = json.dumps({"meta": meta})


class InvalidParameterError(AppError):
    def __init__(self, description=None):
        super().__init__(ERR_INVALID_PARAMETER)
        self.error["description"] = description


class AuthenticationRequiredError(AppError):
    def __init__(self, description=None):
        super().__init__(ERR_AUTH_REQUIRED)
        self.error["description"] = description


class NotSupportedError(AppError):
    def __init__(self, method=None, url=None):
        super().__init__(ERR_NOT_SUPPORTED)
        if method and url:
            self.error["description"] = "method: %s, url: %s" % (method, url)
