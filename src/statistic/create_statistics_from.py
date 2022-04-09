def create_statistics_from(dataset, metric_instance):
    for record in dataset:
        metric_instance.process_row(record)
    metric_instance.save()
    return metric_instance



def create_statistics_from_with_example(dataset, metric_instance):
    saved_record = None
    for record in dataset:
        if saved_record is None:
            text, label = record
            text = bytes.decode(text.numpy())
            saved_record = text
        metric_instance.process_row(record)
    metric_instance.save()
    return (metric_instance, saved_record)

