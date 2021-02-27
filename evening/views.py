from flask import jsonify
from datetime import datetime

from . import __version__


def ping():
    return jsonify(pong=True)


def health_check():
    now = datetime.now()
    return jsonify(alive=True, last_checked=now.utcnow())


def landing():
    return jsonify(
        name="Evening API",
        version=__version__,
        description="Evening is an Eve boilerplate project for rapid api deployment via `.yaml` file configurations.",
    )
