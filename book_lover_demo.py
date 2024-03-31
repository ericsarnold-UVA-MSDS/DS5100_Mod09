import pandas as pd
from booklovers.booklover import BookLover

newby = BookLover("Eric S. Arnold", "esa5ch@virginia.edu", "Comedy")
newby.add_book("Indiana Jones", 4)
newby.add_book("Kill Bill", 2)

newby.num_books_read()
newby.fav_books()