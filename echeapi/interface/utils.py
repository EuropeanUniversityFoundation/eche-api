
import os

from flask import render_template

from echeapi import settings

DEFAULT_CONTEXT = {
    'data_filename': os.path.basename(settings.DATA_FILENAME),
}


def render_to_string(template_name, context=None):
    return render_template(template_name, **{
        **DEFAULT_CONTEXT,
        **(context or {}),
    })
