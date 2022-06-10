
from flask import Flask
from jinja_markdown import MarkdownExtension

from echeapi import settings

app = Flask(
    import_name=__name__,
    static_folder='interface/static',
    template_folder='interface/templates',
)
app.jinja_env.add_extension(MarkdownExtension)
app.secret_key = settings.app_secret_key

import echeapi.interface.views
