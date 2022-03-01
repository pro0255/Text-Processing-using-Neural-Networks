from src.analysis.experiments.parse_confusion_matrix import parse_confusion_matrix
from src.analysis.experiments.parse_metrics import parse_metrics
from src.analysis.experiments.parse_description import parse_description
from src.analysis.experiments.parse_summarization import parse_summarization
from src.analysis.experiments.merge_content import merge_content
 

def create_record(directory):
    try:
        confusion_matrix = parse_confusion_matrix(directory)
        metrics = parse_metrics(directory)
        description = parse_description(directory)
        summarization = parse_summarization(directory)
        record = merge_content(confusion_matrix, metrics, description, summarization, directory)
        return record
    except Exception as e:
        print(f"Exception in {directory}")
        print(f"Exception {e}")
        return None