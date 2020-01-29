import os

from eve import Eve
from eve_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from . import __version__
from . import hooks

from .config import config_map, TEMPLATE_DIR
from .views import ping, health_check, landing


SWAGGER_URL = "/docs"  # URL for exposing Swagger UI (without trailing '/')
API_URL = "/api-docs"  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={"app_name": "Evening API Swagger"},  # Swagger UI config overrides
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)


def create_app(config="development", api_version="2019.1"):
    config_path = config_map[config]

    app = Eve(settings=config_path, template_folder=TEMPLATE_DIR)
    app.config["VERSION"] = api_version

    # Swagger Extension
    app.register_blueprint(swagger)

    app.add_url_rule("/", "landing", landing)
    app.add_url_rule("/ping", "ping", ping)
    app.add_url_rule("/health-check", "health-check", health_check)

    app.before_first_request_funcs.append(hooks.before_request_handler)
    # app.after_request += hooks.after_request_handler

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app

