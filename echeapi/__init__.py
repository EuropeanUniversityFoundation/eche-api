
import os
import logging

from flask import Flask
from jinja_markdown import MarkdownExtension

from echeapi import settings

file_handler = logging.FileHandler(os.path.join(settings.LOG_DIR, 'app.log'))
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(logging.Formatter(settings.LOG_FORMAT))

app = Flask(
    import_name=__name__,
    static_folder='interface/static',
    template_folder='interface/templates',
)
app.jinja_env.add_extension(MarkdownExtension)
app.secret_key = settings.SECRET_KEY
app.logger.addHandler(file_handler)

from echeapi.interface.views import api, errors, pages
