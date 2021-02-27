from flask import jsonify, render_template
from datetime import datetime


def ping():
    return jsonify(pong=True)


def health_check():
    now = datetime.now()
    return jsonify(alive=True, last_checked=now.utcnow())


def landing():
    return render_template("landing.html")
