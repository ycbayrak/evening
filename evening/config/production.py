import os
import yaml

RESOURCE_DIR = os.environ.get("RESOURCE_DIRECTORY")
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

DOMAIN = {
    f["name"].split(".")[0]: yaml.safe_load(f["config"])
    for f in RESOURCE_FILES
    if not f["name"].startswith(".")
}
