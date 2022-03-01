import json


def get_from_instance_params(instance):
    func = getattr(instance, "get_params", None)
    if callable(func):
        return func(instance)
    else:
        return None


def get_extra(predictor):
    predictor_params = get_from_instance_params(predictor)

    j_p = json.dumps(dict(predictor_params))

    return j_p
