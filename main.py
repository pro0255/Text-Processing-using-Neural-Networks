from src.data_preparing.build_dataset.gutenberg_builder import gutenberg_builder

builder = gutenberg_builder()

build_sentences = [2, 7, 15]


for bs in build_sentences:
    builder.build_dataset(bs, 5)