def create_statistics_from(dataset, metric_instance):
    for record in dataset:
        metric_instance.process_row(record)
    metric_instance.save()
    return metric_instance
