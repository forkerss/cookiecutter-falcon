FROM python:{{cookiecutter.python_version}}
RUN mkdir /app
ADD . /app/

RUN pip install -i {{cookiecutter.pypi_src}} --no-cache-dir -r /app/requirements.txt

WORKDIR /app