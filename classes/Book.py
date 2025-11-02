
class Book:
    """
    book class
    """
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def get_details(self):
        return f"Book details : Title : {self.title}, Author : {self.author}, ISBN : {self.isbn}, Available : {self.is_available}"


