
from datetime import datetime

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
    fields = [
        f.strip()
        for f in request.args.get('fields', '').split(',')
        if f.strip() in settings.DATA_FIELDS
    ]

    filter = None
    if key is not None:
        if key not in settings.DATA_FIELDS:
            raise ApiError(404, 'Resource not found')

        if key in settings.DATE_FIELDS and value is not None:
            try:
                dt = datetime.fromisoformat(value)
            except Exception:
                raise ApiError(400, 'Bad request', detail='Invalid date format. ISO format expected.')
            else:
                value = dt.strftime('%Y-%m-%d %H:%M:%S')

        filter = (key, value)

    try:
        body = api.as_json(fields=fields, filter=filter)
    except Exception:
        app.logger.exception('Error while fetching API data')
        raise ApiError(500, 'Server error')

    return Response(body, mimetype='application/json')
