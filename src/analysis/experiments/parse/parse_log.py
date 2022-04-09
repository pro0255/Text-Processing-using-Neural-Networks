from src.analysis.experiments.validation.exists import exists
from src.config.config import FILENAME_LOGS
import pandas as pd


def parse_log(directory):
    path = exists(directory, FILENAME_LOGS)

    if path is None:
        return None

    content = pd.read_csv(path, sep=";")

    keys = []
    dic = {}
    for index in range(content.shape[1]):
        key = content.columns[index]
        keys.append(key)
        if "Unnamed" not in key:
            dic[key] = [content.iloc[:, index].values]

    res = pd.DataFrame.from_dict(dic, orient="index").reset_index()
    res.columns = ["id", "value"]

    return res
