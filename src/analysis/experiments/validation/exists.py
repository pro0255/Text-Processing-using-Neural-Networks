import os
import typing
from os.path import exists as file_exists


def exists(directory: str, filename: str) -> typing.Union[None, str]:
    current_path = os.path.sep.join([directory, filename])
    if file_exists(current_path):
        return current_path
    return None
