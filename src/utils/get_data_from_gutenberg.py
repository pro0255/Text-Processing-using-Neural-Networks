import typing


def get_data_from_gutenberg(data: typing.Dict[str, ], key: str):
    try:
        return data[key][0]
    except:
        return data[0][key][0]
