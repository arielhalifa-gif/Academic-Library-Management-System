from modules.Books import Book
from modules.user import User
from modules.library import Library
from utils.sistemAdmin import SystemAdmin

if __name__ == "__main__":
    b1 = Book("Harry Potter", "J.k Rolling", 215468)
    b2 = Book("etsem abariaj", "collin uber", 65498)
    b3 = Book("tsofen da vinci", "grisham", 654132)

    user1 = User("654321", "moshe")
    user2 = User("615489", "yosi")

    library = Library()
    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)

    library.register_user(user1)
    library.register_user(user2)

    library.perform_borrow("654321", 215468)
    library.perform_borrow("654321", 215468)
    SystemAdmin.report_stats()