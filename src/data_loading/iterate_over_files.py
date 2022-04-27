import typing

from tqdm import tqdm

from src.data_loading.load_files import load_files
from src.utils.load_json import load_json


def iterate_over_files(
    files_path: typing.List[str],
    process_func
):
    """Iterates over files and call method process_func

    Args:
        files_path (typing.List[str]): path where files are situated
        process_func (_type_): function which is called in loop
    """
    print(f"Loading files from {files_path}")
    counter = 0
    for path_to_file in tqdm(load_files(files_path)):
        path = bytes.decode(path_to_file.numpy())
        data = load_json(path)

        if counter % 10000 == 0:
            print(counter)

        counter += 1

        if data is None:
            continue

        process_func(data)
