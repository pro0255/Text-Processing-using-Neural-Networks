

current_directory = getwd()

path_to_config = paste(current_directory, "/../../config/r_config.csv", sep="")

path_to_config
config = read.csv(path_to_config, header=TRUE, sep=';')
config

ID_KEY = "Id"
VALUE_KEY = "Value"

MIRROR_KEY = "MIRROR"
DATA_DIR_KEY = "DATA_DIRECTORY"
AUTHORS_DIR_KEY = "AUTHORS_DIRECTORY"

mirror = config[config[ID_KEY] == MIRROR_KEY, c(VALUE_KEY)]
target_data_directory = config[config[ID_KEY] == DATA_DIR_KEY, c(VALUE_KEY)]
target_author_directory = config[config[ID_KEY] == AUTHORS_DIR_KEY, c(VALUE_KEY)]

print(mirror)
print(target_data_directory)
print(target_author_directory)

