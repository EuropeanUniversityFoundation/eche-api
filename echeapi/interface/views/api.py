
from flask import request, Response

from echeapi import app, settings
from echeapi.utils import api


@app.route("/api/", methods=['GET'])
@app.route("/api/<string:key>/", methods=['GET'])
@app.route("/api/<string:key>/<string:value>/", methods=['GET'])
def api_(key=None, value=None):
    fields = []
    args = request.args
    if 'fields' in args:
        request_fields = args.get("fields").split(',')
        fields = [f for f in request_fields if f in settings.known_keys]

    if key in settings.known_keys:
        body = api.list(filter=(key, value), fields=fields)
    else:
        body = api.list(fields=fields)

    return Response(body, mimetype='application/json')
