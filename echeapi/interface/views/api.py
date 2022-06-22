
from flask import jsonify, request, Response

from echeapi import app, settings
from echeapi.utils import api


class ApiError(Exception):
    def __init__(self, status, title, **kwargs):
        self.status = status
        self.title = title
        self.detail = kwargs.get('detail', '')
        self.type = kwargs.get('type', '')
        self.instance = kwargs.get('instance', '')


@app.errorhandler(ApiError)
def api_error(error):
    response = jsonify(
        type=error.type,
        title=error.title,
        status=error.status,
        detail=error.detail,
        instance=error.instance,
    )
    response.mimetype = 'application/problem+json'
    return response, error.status


@app.route("/api/", methods=['GET'])
@app.route("/api/<string:key>/", methods=['GET'])
@app.route("/api/<string:key>/<string:value>/", methods=['GET'])
def eche_list(key=None, value=None):
    args = request.args

    fields = []
    if 'fields' in args:
        request_fields = args.get("fields").split(',')
        fields = [f for f in request_fields if f in settings.DATA_FIELDS]

    filter = None
    if key is not None:
        if key in settings.DATA_FIELDS:
            filter = (key, value)
        else:
            raise ApiError(404, 'Resource not found')

    try:
        body = api.list(fields=fields, filter=filter)
    except Exception:
        app.logger.exception('Error while fetching API data')
        raise ApiError(500, 'Server error')

    return Response(body, mimetype='application/json')
