from src.config.config import FILENAME_DESCRIPTION
from src.analysis.experiments.exists import exists
import pandas as pd

def parse_description(directory):
    path = exists(directory, FILENAME_DESCRIPTION)
    
    if path is None:
        return None
        
    content = pd.read_csv(path, sep=';')
    return content