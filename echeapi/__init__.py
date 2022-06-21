
import os
import logging

from flask import Flask
from jinja_markdown import MarkdownExtension

from echeapi import settings

file_handler = logging.FileHandler(os.path.join(settings.log_dir, 'app.log'))
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(logging.Formatter(settings.log_format))

app = Flask(
    import_name=__name__,
    static_folder='interface/static',
    template_folder='interface/templates',
)
app.jinja_env.add_extension(MarkdownExtension)
app.secret_key = settings.app_secret_key
app.logger.addHandler(file_handler)

import echeapi.interface.views
