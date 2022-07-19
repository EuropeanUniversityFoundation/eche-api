
import json

from echeapi import settings


def process(json_data):
    input = json.loads(json_data)
    output = []

    for item in input:
        tmp = {}

        for key, value in item.items():
            tmp[key] = value

        if list(set(item.keys()) & set(settings.PROCESSED_KEYS)) is not []:
            tmp[settings.PROCESSED_KEY] = {}

            for key, value in item.items():
                if key in settings.PROCESSED_KEYS:
                    field = key.split('.')[-1]
                    tmp[settings.PROCESSED_KEY][field] = tmp.pop(key)

        if list(set(item.keys()) & set(settings.VERIFIED_KEYS)) is not []:
            tmp[settings.VERIFIED_KEY] = {}

            for key, value in item.items():
                if key in settings.VERIFIED_KEYS:
                    field = key.split('.')[-1]
                    tmp[settings.VERIFIED_KEY][field] = tmp.pop(key)

        output.append(tmp)

    json_data = json.dumps(output)

    return json_data
