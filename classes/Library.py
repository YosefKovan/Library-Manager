from classes.Logger import Logger
from classes.SystemAdmin import SystemAdmin


class Library:
    """
    Library
    """

    max_borrow_days = 14

    def __init__(self):
        self.books = {}
        self.users = {}

    # ========================================
    def register_user(self, user):
        self.users[user.user_id] = user
        Logger.action_type("INFO", "User Added")


    # ========================================
    def validate_book_and_user(self, user_id, isbn):
        if not user_id or not user_id in self.users:
            return False, "User does not exist!!!"

        if not isbn or not isbn in self.books:
            return False,  "Book does not exist it must be added before performing a borrow!!!"

        return True, "Book and user in system"

    # ========================================
    def add_book(self, book):
        self.books[book.isbn] = book
        Logger.action_type("INFO", "Book Added")

    # ========================================
    def perform_borrow(self, user_id, isbn):

        try:
            result = self.validate_book_and_user(user_id, isbn)
            if not result[0]:
                raise Exception(f"Error : {result[1]}")

            if not self.books[isbn].is_available:
                raise Exception("the book is currently not available!!!")

            book = self.books[isbn]
            user = self.users[user_id]

            book.is_available = False
            user.borrow_book(book)
            Logger.action_type("INFO", "Book borrowed, User Name: " + user.name + ", " + "Book borrowed: " + book.title)
            SystemAdmin.update_transactions_count(1)

        except Exception as error:
            Logger.action_type("ERROR", error)

    #========================================
    def perform_return(self, user_id, isbn):
        try:
            result = self.validate_book_and_user(user_id, isbn)
            if not result[0]:
                raise Exception(f"Error : {result[1]}")

            if self.books[isbn].is_available:
               raise Exception("The book is currently available. cannot return book!")

            user = self.users[user_id]
            book = self.books[isbn]

            user.return_book(book)
            book.is_available = True
            Logger.action_type("INFO", "Book returned: " + "User Name: " + user.name + ", " + "Book returned: " + book.title)
            SystemAdmin.update_transactions_count(1)

        except Exception as error:
            Logger.action_type("ERROR", error)




