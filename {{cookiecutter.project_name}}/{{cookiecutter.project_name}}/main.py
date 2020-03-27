import falcon

from {{cookiecutter.project_name}} import config
from {{cookiecutter.project_name}}.api.common import Index
from {{cookiecutter.project_name}}.lib.errors import AppError
from {{cookiecutter.project_name}}.lib.log import setup_logger
from {{cookiecutter.project_name}}.middlewares import CORS, Filter, Translate


def register_routes(app):
    # index
    app.add_route('/', Index())
    # users self
    # add app error
    app.add_error_handler(AppError, AppError.handle)


def create_app(testing: bool = False):
    middlewares = (Filter(), CORS(), Translate())
    app = falcon.App(middleware=middlewares)
    # setup logger
    setup_logger(level=config.LOG_LEVEL)
    # register routes
    register_routes(app)
    return app
