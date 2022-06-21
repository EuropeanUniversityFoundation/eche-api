
from flask import render_template

from echeapi import app


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        'errors/404.html',
        error=error,
    ), error.code


@app.errorhandler(500)
def server_error(error):
    return render_template(
        'errors/500.html',
        error=error,
    ), error.code
