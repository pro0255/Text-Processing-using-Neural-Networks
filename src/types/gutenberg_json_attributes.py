from enum import Enum


class GutenbergJsonAttributes(Enum):
    """Fields which are used in json gutenberg. They are constructed in .R script.
    """
    Title = "Title"
    Author = "Author"
    Subject = "Subject"
    Alias = "Alias"
    Birthdate = "Birthdate"
    Deathdate = "Deathdate"
    Aliases = "Aliases"
    Text = "Text"
    Id = "Id"
    AuthorId = "AuthorId"
