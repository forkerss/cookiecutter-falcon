# cookiecutter-falcon 🦅
Fast building `Falcon` rest api(with sqlite using ORM) project template.

It includes the following: Docker, Docker-compose, Gunicorn, Pipenv, Nginx and a simple command manager.

**middlewares**

    - CORS: handle CORS
    - Filter: filter some requests
    - Translate:  parsing the request body when `Content-Type` is `application/json`

**errors**: common errors

**FieldValidator**: using `cerberus` to verify field data

## Usage

```bash
git clone git@github.com:Buzz2d0/cookiecutter-falcon.git
cookiecutter cookiecutter-falcon
```

## thx

- https://github.com/ziwon/falcon-rest-api
