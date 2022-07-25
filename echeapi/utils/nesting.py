
def process(input):
    output = []

    for item in input:
        tmp = {}
        for key, value in item.items():
            if '.' not in key:
                tmp[key] = value
            else:
                _prefix, _key = key.split('.', 1)
                tmp.setdefault(_prefix, {})[_key] = value
        output.append(tmp)

    return output
