## DEPRECATED FILE. Please use download_gutenberg_with_config.R!


ID_KEY = "Id"
VALUE_KEY = "Value"

MIRROR_KEY = "MIRROR"
DATA_DIR_KEY = "DATA_DIRECTORY"
AUTHORS_DIR_KEY = "AUTHORS_DIRECTORY"


current_directory = getwd()
path_to_config = paste(current_directory, "/../../config/r_config.csv", sep="")

load_config <- function(path) {
  config = read.csv(path_to_config, header=TRUE, sep=';')
  return(config) 
}

config = load_config(path_to_config)


from_config_mirror_target_data_target_authors <- function(config) {

  
  mirror = config[config[ID_KEY] == MIRROR_KEY, c(VALUE_KEY)]
  target_data_directory = config[config[ID_KEY] == DATA_DIR_KEY, c(VALUE_KEY)]
  target_author_directory = config[config[ID_KEY] == AUTHORS_DIR_KEY, c(VALUE_KEY)]
  
  return(c(mirror, target_data_directory, target_author_directory))
  
}

values = from_config_mirror_target_data_target_authors(config)

mirror = values[0]
target_data_directory = values[1]
target_author_directory = values[2]



