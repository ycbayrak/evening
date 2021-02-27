from eve import Eve
from eve_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from . import __version__
from . import hooks

from .config import config_map
from .views import ping, health_check, landing

SWAGGER_URL = "/docs"  # URL for exposing Swagger UI (without trailing '/')
API_URL = "/api-docs"  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={"app_name": "Evening API Swagger", "version": __version__},
)


def create_app(config="development", api_version=__version__):
    config_path = config_map[config]

    app = Eve(settings=config_path)
    app.config["VERSION"] = api_version

    app.config["SWAGGER_INFO"] = {
        "title": "Evening API",
        "version": __version__,
        "description": "Evening is a Eve boilerplate project for rapid api deployment via yaml file configurations.",
    }
    app.register_blueprint(swagger)

    app.add_url_rule("/", "landing", landing)
    app.add_url_rule("/ping", "ping", ping)
    app.add_url_rule("/health-check", "health-check", health_check)

    app.before_first_request_funcs.append(hooks.before_request_handler)
    # app.after_request += hooks.after_request_handler

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
