from cerberus import SchemaError, Validator

from {{cookiecutter.project_name}}.lib.errors import AppError, InvalidParameterError
from {{cookiecutter.project_name}}.lib.log import logger


ALLSCHEMA = {
    "User": {
        "username": {
            "type": "string",
            "regex": r"^[0-9a-zA-Z_]{4,30}$",
            "required": True
        },
        "password": {
            "type": "string",
            "minlength": 6,
            "maxlength": 64,
            "required": True
        }
    }
}


class FieldValidator:
    """FieldValidator: validate data according to schema
    Args:
        is_params: a Boolean, when is_params is true, validate req.params data
        null: a Boolean, When null is true, Doc is allowed to be empty

    Usage:
        @falcon.before(FieldValidator(ALLSCHEMA["User"], is_params=True, null=True).validate)
        def on_get(self, req, resp): ...
    """

    def __init__(self, schema, is_params=False, null=False):
        self.schema = schema
        self.is_params = is_params
        self.null = null

    def validate(self, req, resp, resource, params):
        v = Validator(self.schema)
        if self.is_params:
            doc = req.params
        else:
            doc = req.context.get("data", None)
        logger.debug("FieldValidator - data: %s" % repr(doc))

        if self.null is False:
            if not doc:
                raise InvalidParameterError("Invalid Request %s" % doc)
            if not isinstance(doc, dict):
                raise InvalidParameterError(
                    "Invalid doc %s not a dict." % doc)
        try:
            if not v.validate(doc):
                raise InvalidParameterError(v.errors)
        except SchemaError:
            raise AppError(description="FieldValidator Schema Error")
