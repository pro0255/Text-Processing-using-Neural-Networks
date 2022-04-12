pac = c("gutenbergr", "jsonlite", "dplyr", "docstring")


ROOT = "C:/Users/Vojta/Desktop/diploma"
wd = gsub(" ", "", paste(ROOT, "/src/download/r", ""))

print(wd)

setwd(wd)
lib_subdir = "lib"
current_directory = getwd()

lib_directory = gsub(" ", "", paste(current_directory, "/", lib_subdir, ""))

print(lib_directory)

ifelse(!dir.exists(file.path(lib_directory)), dir.create(file.path(lib_directory)), FALSE)

.libPaths(c(.libPaths(), lib_directory))


install.packages(pac, lib=lib_directory, repos = "http://cran.us.r-project.org")

library(gutenbergr)
library(jsonlite)
library(dplyr)
library(docstring)

### Import || Download libraries

ID_KEY = "Id"
VALUE_KEY = "Value"

MIRROR_KEY = "MIRROR"
DIRECTORY_REAL_KEY = "DIRECTORY_REAL"
DIRECTORY_TEST_KEY = "DIRECTORY_TEST"
DATA_DIRECTORY_KEY = "DATA_DIRECTORY"
AUTHORS_DIRECTORY_KEY = "AUTHORS_DIRECTORY"
AUTHORS_FILENAME_KEY = "AUTHORS_FILENAME"
AUTHORS_DIR_KEY = "AUTHORS_DIRECTORY"
IS_TEST_KEY = "IS_TEST"
FROM_KEY = "FROM"
TO_KEY = "TO"

CONFIG_KEYS = c(
  MIRROR_KEY, 
  DIRECTORY_REAL_KEY,
  DIRECTORY_TEST_KEY,
  DATA_DIRECTORY_KEY,
  AUTHORS_DIRECTORY_KEY,
  AUTHORS_FILENAME_KEY,
  AUTHORS_DIR_KEY,
  IS_TEST_KEY,
  FROM_KEY,
  TO_KEY
)

### Loading config

path_to_config = paste(current_directory, "/../../config/r_config.csv", sep="")

load_config <- function(path) {
  #' Loads a config
  #'
  #' Loads config from specified path
  #'
  #' @param path string input which describes path where config is situated
  config = read.csv(path_to_config, header=TRUE, sep=';')
  return(config) 
}


config = load_config(path_to_config)


get_value_from_config <- function(config, key) {
  return(config[config[ID_KEY] == key, c(VALUE_KEY)])
}


MIRROR_VALUE = get_value_from_config(config, MIRROR_KEY)
DIRECTORY_REAL_VALUE = get_value_from_config(config, DIRECTORY_REAL_KEY)
DIRECTORY_TEST_VALUE = get_value_from_config(config, DIRECTORY_TEST_KEY)
DATA_DIRECTORY_VALUE = get_value_from_config(config, DATA_DIRECTORY_KEY)
AUTHORS_DIRECTORY_VALUE = get_value_from_config(config, AUTHORS_DIRECTORY_KEY)
AUTHORS_FILENAME_VALUE = get_value_from_config(config, AUTHORS_FILENAME_KEY)
AUTHORS_DIR_VALUE = get_value_from_config(config, AUTHORS_DIR_KEY)
IS_TEST_VALUE = get_value_from_config(config, IS_TEST_KEY)
FROM_VALUE = get_value_from_config(config, FROM_KEY)
TO_VALUE = get_value_from_config(config, TO_KEY)


create_directories <- function(directory_real, directory_test, is_test, authors_dir, data_dir, authors_filename) {
  
  #' Create directories
  #'
  #' According to input creates desired paths
  #'
  #' @param directory_real real directory where will be downloaded data from gutenberg project
  #' @param directory_test teste directory where will be downloaded data from gutenberg project
  #' @param is_test boolean information which acts signpost
  #' @param authors_dir subdirectory name where should be authors csv downloaded
  #' @param data_dir subdirectory name where should be data downloaded
  #' @param authors_filename name of file which will be used for authors csv
  
  print(is_test)
  directory = if(is_test == "True") directory_test else directory_real
  path_authors = paste(directory, "\\", authors_dir, "")
  path_data = paste(directory, "\\", data_dir, "")
  authors_filename = paste(path_authors, "\\", authors_filename, "")
  return(c(path_authors, path_data, authors_filename, directory)) 
}

path_values = create_directories(DIRECTORY_REAL_VALUE, DIRECTORY_TEST_VALUE, IS_TEST_VALUE, AUTHORS_DIRECTORY_VALUE, DATA_DIRECTORY_VALUE, AUTHORS_FILENAME_VALUE)

path_authors = gsub(" ", "", path_values[1])
path_data = gsub(" ", "", path_values[2])
authors_filename = gsub(" ", "", path_values[3])
parent_directory = gsub(" ", "", path_values[4])

print(paste("Current mirror", MIRROR_VALUE, ""))
print(paste("Parent directory", parent_directory, ""))
print(paste("Current target data directory", path_data, ""))
print(paste("Current authors filename", path_authors, ""))
print(paste("Authors filename", authors_filename, ""))
print(paste("Is test", IS_TEST_VALUE, ""))
print(paste("From id", FROM_VALUE, ""))
print(paste("To id", TO_VALUE, ""))


id_from = if(FROM_VALUE == 'None') 0 else FROM_VALUE
id_to = if(TO_VALUE == 'None') nrow(prepared_dataframe) else TO_VALUE

print(paste("Downloading from", id_from, "to", id_to, " "))



### Check if exists directory else create

ifelse(!dir.exists(file.path(parent_directory)), dir.create(file.path(parent_directory)), FALSE)

ifelse(!dir.exists(file.path(path_data)), dir.create(file.path(path_data)), FALSE)

ifelse(!dir.exists(file.path(path_authors)), dir.create(file.path(path_authors)), FALSE)


### Downloading from Gutenberg Project



gutenberg_metadata %>%
  count(language, sort = TRUE)


# The meta-data currently in the package was last updated on 05 May 2016.

gutenberg_metadata %>%
  filter(language == "en")


works_metadata = gutenberg_works()
subjects_metadata = gutenberg_subjects
authors_metadata = gutenberg_authors



prepared_dataframe = merge(works_metadata, subjects_metadata, by='gutenberg_id', all.x = TRUE)
prepared_dataframe = merge(prepared_dataframe, authors_metadata, by='gutenberg_author_id', all.x = TRUE)


nrow(prepared_dataframe)
nrow(prepared_dataframe[!duplicated(prepared_dataframe), ]) 


prepared_dataframe = distinct(prepared_dataframe, gutenberg_id, .keep_all= TRUE)

print(paste("Number of english books", nrow(prepared_dataframe), ""))



ids = prepared_dataframe[, c('gutenberg_id')]
authors = prepared_dataframe[, c('author.y')]

# Freq of author
prepared_dataframe %>% count(gutenberg_author_id)
prepared_dataframe %>% count(author.y, sort=TRUE)



#Filter dataframe - UNKNOWN authors, NA etc.
#Omited docs without author
prepared_dataframe =  prepared_dataframe[!is.na(prepared_dataframe$gutenberg_author_id), ]


prepared_dataframe = prepared_dataframe[order(prepared_dataframe$gutenberg_id), ]


#Some ids of authors are in category unknown, various. These ones was filtered.
ids_to_filter = c(116, 216, 49)


prepared_dataframe = prepared_dataframe[!prepared_dataframe$gutenberg_author_id %in% ids_to_filter, ] 
my_summary_authors <- prepared_dataframe %>%
  dplyr::count(gutenberg_author_id, author.y, sort = TRUE) 


print(paste("Number of english books with specified author", nrow(prepared_dataframe), ""))

save_doc <- function(downloaded_document_frame, current_row, directory_to_save) {
  
  #' Save document with gutenberg properties
  #'
  #' It is process function which takes out specific properties from record of gutenberg. After that is constructed json file named 
  #' with id of book.
  #'
  #' @param downloaded_document_frame downloaded text of current gutenberg book
  #' @param current_row current record with specific properties
  #' @param directory_to_save string which describes directory where should be json saved
  
  # Prepare properties
  
  current_id = current_row$gutenberg_id
  save_name = paste("\\", current_id, '.json', sep="")
  path_to_save = paste(directory_to_save, save_name, sep="")
  processed_text = c(downloaded_document_frame$text, sep='')
  
  #Create dataframe
  
  dataframe_to_save <- data.frame(
    Title = I(list(c(current_row$title))),
    Author = I(list(c(current_row$author.x))),
    Subject = I(list(c(current_row$subject))),
    Alias = I(list(c(current_row$alias))),
    Birthdate = I(list(c(current_row$birthdate))),
    Deathdate = I(list(c(current_row$deathdate))),
    Aliases = I(list(c(current_row$aliases))),
    Text = I(list(toString(processed_text))),
    Id = I(list(c(current_row$gutenberg_id))),
    AuthorId = I(list(c(current_row$gutenberg_author_id)))
  )
  
  #Save to json
  
  json <- toJSON(dataframe_to_save)
  write(json, path_to_save)
  print("Saved")
}



download_frame <- function(dataframe, directory_to_save) {
  
  #' Download frame
  #'
  #' It is function which iterates over input dataframe and one after one tries to download gutenberg books. This books can be picked before.
  #' In my diploma work i filtered it with conditions:
  #' - English text
  #' - Known author
  #'
  #' @param dataframe dataframe object with books which should be downloaded
  #' @param directory_to_save string which describes directory where should be saved books
  
  # Prepare properties
  
  
  print(paste("Downloading to directory", directory_to_save, " "))
  for(current_id in dataframe$gutenberg_id) {
    current_row = dataframe[dataframe$gutenberg_id == current_id, ]
    print(current_id)
    print('Downloading')    
    downloaded_doc = gutenberg_download(current_id, mirror = MIRROR_VALUE)
    print('Downloaded\n')
    save_doc(downloaded_doc, current_row, directory_to_save)
  }
  print("Finished downloading")
}

#selected = prepared_dataframe[prepared_dataframe$gutenberg_id == 1, ]


#Selection of books which should be downloaded. Prepared dataframe is already filtered. Id from and id to are properties from config file.

selected = prepared_dataframe[id_from:id_to, ]


#Call of implemented function which iterates over all books and tries to download them.

download_frame(selected, path_data)


#After all books are downloaded, then authors csv for whom was books downloaded are saved in specified directory according to config.

print(paste("Saving authors csv to", authors_filename, " "))
write.csv(my_summary_authors, authors_filename, row.names = FALSE)



