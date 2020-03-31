import json

from falcon import MEDIA_JSON

from {{cookiecutter.project_name}}.lib import errors
from {{cookiecutter.project_name}}.lib.log import logger


class Translate:
    """Translate 
        - application/json
    """

    def process_request(self, req, resp):
        logger.debug("Translate - method: %s, content_type: %s",
                     repr(req.method), repr(req.content_type))

        if req.content_type is None or \
                not req.content_type.startswith(MEDIA_JSON):
            req.context["data"] = None
            return

        raw_json = req.bounded_stream.read()
        if not raw_json:
            raise errors.InvalidParameterError(
                "A valid JSON document is required")
        try:
            req.context["data"] = json.loads(raw_json.decode("utf-8"))
        except UnicodeDecodeError:
            raise errors.InvalidParameterError(
                "Cannot be decoded by utf-8")
        except ValueError:
            raise errors.InvalidParameterError(
                "No JSON object could be decoded or Malformed JSON")
