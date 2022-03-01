import os
from os.path import exists as file_exists

def exists(directory, filename):
    current_path = os.path.sep.join([directory, filename])
    if file_exists(current_path):
        return current_path
    return None