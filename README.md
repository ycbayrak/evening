# Evening

Evening is a Eve boilerplate project for rapid api deployment via `.yaml` file configurations.

Good evening!

## Getting Started

- `pipenv install`

- `python manage.py runserver`

## Guide

### How to create resource?

Create a file in `evening/resources` folder, and name it like `<resource-name>.yaml`, then your resource is ready. You can check available parameters on `/docs/resource-config.rst`

## Deployment

### Docker

`docker build -t evening-api .`

`docker run -p 8000:8000 evening-api:latest`

Or, with `docker-compose`

`docker-compose up`
