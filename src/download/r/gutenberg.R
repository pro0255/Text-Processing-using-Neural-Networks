library(gutenbergr)
library(jsonlite)
library(dplyr)


# https://cran.r-project.org/web/packages/gutenbergr/vignettes/intro.html


# In many analyses, you may want to filter just for English works, avoid duplicates, and include only books that have text that can be downloaded. 
# The gutenberg_works() function does this pre-filtering:


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

nrow(prepared_dataframe) #should be 40737



ids = prepared_dataframe[, c('gutenberg_id')]
authors = prepared_dataframe[, c('author.y')]

# Freq of author
prepared_dataframe %>% count(gutenberg_author_id)
prepared_dataframe %>% count(author.y, sort=TRUE)





#Sort by gutenberg id



#Filter dataframe - UNKNOWN authors, NA etc.


#Omited docs without author
prepared_dataframe =  prepared_dataframe[!is.na(prepared_dataframe$gutenberg_author_id), ]


prepared_dataframe = prepared_dataframe[order(prepared_dataframe$gutenberg_id), ]


ids_to_filter = c(116, 216, 49)


prepared_dataframe = prepared_dataframe[!prepared_dataframe$gutenberg_author_id %in% ids_to_filter, ] 


my_summary_authors <- prepared_dataframe %>%
  dplyr::count(gutenberg_author_id, author.y, sort = TRUE) 



save_doc <- function(downloaded_document_frame, current_row, directory_to_save) {
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
  for(current_id in dataframe$gutenberg_id) {
    current_row = dataframe[dataframe$gutenberg_id == current_id, ]
    print(current_id)
    print('Downloading')    
    downloaded_doc = gutenberg_download(current_id, mirror = 'http://www.gutenberg.org/dirs/')
    print('Downloaded')
    save_doc(downloaded_doc, current_row, directory_to_save)
  }
  print("Finished")
}

selected = prepared_dataframe[prepared_dataframe$gutenberg_id > 46926, ]

download_frame(selected, 'C:\\Users\\Vojta\\Desktop\\diploma\\gutenberg_downloaded\\data')


write.csv(my_summary_authors, 'C:\\Users\\Vojta\\Desktop\\diploma\\gutenberg_downloaded\\authors\\authors.csv',  row.names = FALSE)


