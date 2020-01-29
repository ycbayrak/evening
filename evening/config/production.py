import yaml
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RESOURCE_DIR = os.path.join(BASE_DIR, "resources")
RESOURCE_FILES = [
    {"name": file, "config": open(os.path.join(RESOURCE_DIR, file)).read()}
    for file in os.listdir(RESOURCE_DIR)
]

URL_PREFIX = os.environ.get("URL_PREFIX", None)
API_VERSION = os.environ.get("API_VERSION", None)


# Running on local machine. Let's just use the local mongod instance.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.

MONGO_HOST = "mongo"
MONGO_PORT = 27017
# MONGO_USERNAME = "user"
# MONGO_PASSWORD = "user"
MONGO_DBNAME = "evening-production"


# Swagger UI Settings
SWAGGER_INFO = {
    "title": "Evening API",
    "version": "1.0",
    "description": "API description",
    "termsOfService": "Terms of Service",
    "license": {
        "name": "BSD",
        "url": "https://github.com/nicolaiarocci/eve-swagger/blob/master/LICENSE",
    },
}


DOMAIN = {
    f["name"].split(".")[0]: yaml.safe_load(f["config"])
    for f in RESOURCE_FILES
    if not f["name"].startswith("_")
}

