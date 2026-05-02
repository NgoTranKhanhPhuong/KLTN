def extract_features(tc, actual):

    features = []

    def add(f):
        if f not in features:
            features.append(f)

    for k, v in tc.items():

        if v is None:
            add("null_value")

        elif isinstance(v, str) and v == "":
            add("empty_string")

        elif isinstance(v, int):

            if v < 0:
                add("boundary_min")
            elif v > 10000:
                add("boundary_max")
            else:
                add("valid_numeric")

        elif isinstance(v, str):
            add("valid_string")

    status = actual.get("status_code")

    if status == 200:
        add("valid_response")
    elif status is None:
        add("timeout")
    else:
        add("error_response")

    return features