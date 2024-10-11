class Book:
  def __init__(self,title,author):
    self.title = title
    self.author = author
    self.__is_checked_out = False

  def is_checked_out(self):
    return self.__is_checked_out

  def check_out(self):
    self.__is_checked_out = True
  def return_book(self):
    self.__is_checked_out = False

class Library:
  def __init__(self):
    self.__books = []
  
  def add_book(self,book):
    self.__books.append(book)
  
  def check_out_book(self,title):
    for book in self.__books:
      if title == book.title and not book.is_checked_out():
        book.check_out()
  
  def return_book(self,title):
    for book in self.__books:
      if title == book.title and book.is_checked_out():
        book.return_book()   

  def list_available_books(self):
    for book in self.__books:
      if not book.is_checked_out():
        print(f"{book.title} by {book.author}")