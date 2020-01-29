import os, sys
import requests

from flask_script import Manager
from evening import create_app


os.environ.setdefault("FLASK_ENV", "development")
os.environ.setdefault("FLASK_PORT", "5000")


config = os.environ.get("FLASK_ENV")
port = int(os.environ.get("FLASK_PORT"))

app = create_app(config=config)
manager = Manager(app)


@manager.command
def health_check():
    """
    Check application is running in production port.
    """
    try:
        r = requests.get("http://localhost:8000/health-check")
        if r.status_code == 200:
            print("Up at Port 8000")
            sys.exit(0)
        else:
            print("Down")
            sys.exit(-1)
    except:
        print("Down")
        sys.exit(-1)


if __name__ == "__main__":
    manager.run()

