
from datetime import datetime
from urllib.parse import unquote

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
    if 'fields' in request.args:
        fields = [
            f.strip()
            for f in request.args['fields'].split(',')
            if f.strip() in settings.ECHE_KEYS
        ]
    else:
        fields = settings.ECHE_KEYS

    if 'processed' in request.args:
        processed = [
            p.strip()
            for p in request.args['processed'].split(',')
            if p.strip() in [*settings.PROCESSED_FIELDS, 'all']
        ]

        if 'all' not in processed:
            processed = [f'{settings.PROCESSED_KEY}.{p}' for p in processed]
        else:
            processed = settings.PROCESSED_KEYS
    else:
        processed = []

    if 'verified' in request.args:
        verified = [
            v.strip()
            for v in request.args['verified'].split(',')
            if v.strip() in [*settings.VERIFIED_FIELDS, 'all']
        ]

        if 'all' not in verified:
            verified = [f'{settings.VERIFIED_KEY}.{v}' for v in verified]
        else:
            verified = settings.VERIFIED_KEYS
    else:
        verified = []

    filter = None
    if key is not None:
        if key not in settings.KNOWN_KEYS:
            raise ApiError(404, 'Resource not found')

        if key in settings.DATE_FIELDS and value is not None:
            try:
                dt = datetime.fromisoformat(value)
            except Exception:
                raise ApiError(400, 'Bad request', detail='Invalid date format. ISO format expected.')
            else:
                value = dt.strftime('%Y-%m-%d %H:%M:%S')

        if value:
            value = unquote(value)

        filter = (key, value)

    try:
        body = api.as_json(
            fields=[*fields, *processed, *verified],
            filter=filter,
            nested=True,
        )
    except Exception:
        app.logger.exception('Error while fetching API data')
        raise ApiError(500, 'Server error')

    return Response(body, mimetype='application/json')
