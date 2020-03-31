import os

BRAND_NAME = "Falcon REST API Template"
DOMAIN = os.getenv("DOMAIN", default="{{cookiecutter.domain}}")
SECRET_KEY = os.getenv("SECRET_KEY", default="this is a secret_key")
ALLOW_METHODS = ("GET", "POST", "PUT", "DELETE", "OPTIONS")
# log
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
# session
SESSION_EXPIRE_DAYS = 7
