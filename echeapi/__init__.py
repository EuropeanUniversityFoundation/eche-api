
import logging
import os

from jinja_markdown import MarkdownExtension

from flask import Flask
from flask_caching import Cache

from echeapi import settings
from echeapi.interface.views import discover

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

cache = Cache(config={
    'CACHE_KEY_PREFIX': __name__,
    **settings.CACHE_CONFIG,
})
cache.init_app(app)

discover()
