import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

config_map = {
    "development": os.path.join(BASE_DIR, "config", "development.py"),
    "test": os.path.join(BASE_DIR, "config", "development.py"),
    "production": os.path.join(BASE_DIR, "config", "production.py"),
}
