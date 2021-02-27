# Evening

Evening is an Eve boilerplate project for rapid api deployment via `.yaml` file configurations.

## Getting Started

Install required python packages;

```shell
pipenv install
```

Activate your Pipenv;

```
pipenv shell
```

Run development server;

```
python manage.py runserver
```

## Guide

### How to create resource?

First, create new `.yaml` called `book.yaml` in `resources/` directory;

```shell
touch resources/book.yaml
```

Then edit file with the content below;

```yaml
url: book
sorting: true
resource_methods:
  - GET
  - POST
  - DELETE
item_methods:
  - GET
  - PATCH
  - DELETE
schema:
  name:
    type: string
  categoryId:
    type: objectid
    required: true
  type:
    type: string
    allowed:
      - bestseller
      - low-price
      - high-price
  age:
    type: number
    max: 10
```

All set, now run development server with;

```shell
python manage.py runserver
```

Navigate to the Swagger UI;

```
http://127.0.0.1:5000/docs
```

You will see your book endpoints accordingly. You can check all configurations on `/docs/resource-config.rst` file.

## Deployment

### Docker

Build image with;

```shell
docker build -t evening-api .
```

Run container with port binding;

```shell
docker run -p 8000:8000 evening-api
```

### Docker Compose

Evening preconfigured with MongoDB instance specified in `docker-compose.yml` file.

Simply run;

```shell
docker-compose up
```
