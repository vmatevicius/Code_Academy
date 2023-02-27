# Create a Book class that has two attributes:

# title
# author

# and two methods:

# A method named .get_title() that returns: "Title: " + the instance title.
# A method named .get_author() that returns: "Author: " + the instance author.

# and instantiate this class by creating 3 new books:

# Pride and Prejudice - Jane Austen (PP)
# Hamlet - William Shakespeare (H)
# War and Peace - Leo Tolstoy (WP)
# The name of the new instances should be PP, H, and WP, respectively. For instance, if I instantiated the following book using this Book class:

import logging

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Book():
    
    def __init__(self, title: str, author: str):
        logging.info(f"Recieved values when creating a book ojbect. title: {title}, author: {author}")
        try:
            self.title = title
            self.author = author
        except Exception as e:
            logging.error(f"Error recieved when setting book obj. values. {e}")
            
    @classmethod
    def get_book(cls):
        title = input("Enter title: ")
        author =  input("Enter author: ")
        return cls(title, author)
    
    def __str__(self) -> str:
        try:
            return f"Title: {self.title}, Author: {self.author}"
        except Exception as e:
            logging.error(f"Error recieved when calling __str__. {e}")
    def get_title(self) -> str:
        try:
            return f"Title: {self.title}"
        except Exception as e:
            logging.error(f"Error recieved when calling get_title. {e}")
    def get_author(self) -> str:
        try:
            return f"Author: {self.author}"
        except Exception as e:
            logging.error(f"Error recieved when calling get_author. {e}")
            
            
PP = Book("Pride and Prejudice", "Jane Austen")
H = Book.get_book()
print(H)
print(PP)