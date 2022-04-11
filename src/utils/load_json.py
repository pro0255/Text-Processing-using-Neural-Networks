import codecs
import json
from re import L


def load_json(path):
    with codecs.open(path, "r", encoding="utf-8", errors="ignore") as stream:
        try:
            content = stream.read()
            return json.loads(content)
        except Exception as e:
            try:
                content = postprocess(stream)
                return json.loads(content)
            except:
                print(f"Oops error when loading json {e}")
                return None


def postprocess(stream):
    content = stream.read()
    content = correct_single_quote_JSON(content)
    content = content.replace("[None]", '["None"]')
    return content


def correct_single_quote_JSON(s):
    rstr = ""
    escaped = False

    for c in s:

        if c == "'" and not escaped:
            c = '"'  # replace single with double quote

        elif c == "'" and escaped:
            rstr = rstr[:-1]  # remove escape character before single quotes

        elif c == '"':
            c = "\\" + c  # escape existing double quotes

        escaped = c == "\\"  # check for an escape character
        rstr += c  # append the correct json

    return rstr
