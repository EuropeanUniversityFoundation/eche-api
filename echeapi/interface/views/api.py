
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
    if '_fields' in request.args:
        fields = [
            f.strip()
            for f in request.args['_fields'].split(',')
            if f.strip() in settings.DEFAULT_API_KEYS
        ]
    else:
        fields = settings.DEFAULT_API_KEYS

    if '_verified' in request.args:
        verified = [
            v.strip()
            for v in request.args['_verified'].split(',')
            if v.strip() in [*settings.VERIFIED_BASE_KEYS, 'all']
        ]
        if 'all' in verified:
            verified = settings.VERIFIED_BASE_KEYS
        verified = [f'{settings.VERIFIED_KEY_PREFIX}.{v}' for v in verified]
    else:
        verified = []

    # For compatibility with in-path parameters.
    params = {**request.args}
    if key is not None:
        if key not in settings.ALL_API_KEYS:
            raise ApiError(404, 'Resource not found')
        params[key] = value

    filter = {}
    for _key, _value in params.items():
        if _key.startswith('_'):
            continue

        if _key not in settings.ALL_API_KEYS:
            raise ApiError(400, f'Invalid parameter: {_key}')

        if _value is None or not _value.strip():
            filter[_key] = None
            continue

        _value = unquote(_value)

        if _key in settings.DATE_FIELDS:
            try:
                dt = datetime.fromisoformat(_value)
            except Exception:
                raise ApiError(400, 'Bad request', detail='Invalid date format. ISO format expected.')
            else:
                _value = dt.strftime('%Y-%m-%d %H:%M:%S')

        elif _key == 'hasVerifiedData':
            if str(_value).lower() in ['true', '1']:
                _value = True
            elif str(_value).lower() in ['false', '0']:
                _value = False
            else:
                raise ApiError(400, 'Bad request', detail='Invalid format. Boolean expected.')

        filter[_key] = _value

    try:
        body = api.as_json(
            fields=[*fields, *verified],
            filter=filter,
            nested=True,
        ).encode()
    except Exception:
        app.logger.exception('Error while fetching API data')
        raise ApiError(500, 'Server error')

    return Response(body, mimetype='application/json')
