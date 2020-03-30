#!/usr/bin/env python3
from wsgiref import simple_server

import click

from {{cookiecutter.project_name}}.main import create_app

BANNER = r"""
{{cookiecutter.project_name}}
"""


@click.group()
def manage():
    click.echo(BANNER)


@manage.command()
@click.option("--host", "host", default="127.0.0.1")
@click.option("--port", "port", default=5000)
@click.option("--testing", "testing", default=True)
def run(host, port, testing):
    """Runs the application on a local development server.
    """
    try:
        app = create_app(testing)
        click.echo("[TESTING] %s" % ("="*50))
        click.echo("[TESTING] API Server run on: http://%s:%s" %
                   (host, port))
        click.echo("[TESTING] %s" % ("="*50))
        httpd = simple_server.make_server(host, int(port), app)
        httpd.serve_forever()
    except KeyboardInterrupt:
        click.echo("\nBye👋")
        httpd.shutdown()


if __name__ == "__main__":
    manage()
