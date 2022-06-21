
from flask import render_template

from echeapi import app


@app.errorhandler(404)
def page_not_found(message):
    return render_template(
        'errors/404.html',
        message=message,
    ), 404


@app.errorhandler(500)
def server_error(message):
    return render_template(
        'errors/500.html',
        message=message,
    ), 500
