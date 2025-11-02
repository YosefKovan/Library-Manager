from classes.Library import Library
from classes.User import User
from classes.Book import Book

if __name__ == "__main__":
   library = Library()

   user1 = User("1", "Yossi")
   user2 = User("2", "David")

   library.register_user(user1)
   library.register_user(user2)

   book1 = Book("Home", "Yossi", "1")
   book2 = Book("Return", "Dossi", "2")

   library.add_book(book1)
   library.add_book(book2)

   library.perform_borrow(user1.user_id, book1.isbn)
   library.perform_borrow(user1.user_id, book1.isbn)
   library.perform_return(user1.user_id, book1.isbn)
   library.perform_borrow(user1.user_id, book1.isbn)

