def prepare_dataset_from_tokenizer(dataset, tokenizer):
    return dataset.map(tokenizer.ty_py_func).map(tokenizer.to_model_input)
