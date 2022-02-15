import pandas as pd
from src.statistic.types.metric_type import translate_instance_to_type

class MetricWrapper:
    def __init__(self, statistic_description, metric_instances = [], path_to_save = None):
        self.path_to_save = path_to_save
        self.metric_instances = metric_instances
        self.statistic_description = statistic_description
    
    def update_state(self, text, label):
        #TODO: Can derive from this class and update __init__ and update_states
        for instance in self.metric_instances:
            instance.update_state(text, label)
    
    def process_row(self, record):
        text, label = record
        text = bytes.decode(text.numpy())
        label = label.numpy()
        self.update_state(text, label)
    
    def save(self):
        if self.path_to_save is not None:
            print(f'Saving to {self.path_to_save}')
            with pd.ExcelWriter(self.path_to_save, engine='xlsxwriter') as writer:
                self.statistic_description.get_dataframe().to_excel(writer, sheet_name=translate_instance_to_type(self.statistic_description))        
                for metric_instance in self.metric_instances:
                    metric_instance.get_dataframe().to_excel(writer, sheet_name=translate_instance_to_type(metric_instance))            
        else:
            print('Saving path is not specified!')
            
    def __str__(self):
        string = ''
        for instance in self.metric_instances:
            string += type(instance).__name__
            string += instance.get_dataframe().to_string()
            string += '\n'
        return string