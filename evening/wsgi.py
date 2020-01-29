import os
from evening import create_app

config = os.environ.get("FLASK_ENV", "production")

app = create_app(config=config)

