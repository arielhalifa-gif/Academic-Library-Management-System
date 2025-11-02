from utils.sistemAdmin import SystemAdmin
from utils.loger import Logger
from modules.user import User

class Library:
    max_borrow_days = 14
    def __init__(self):
        self.books = {}
        self.users = {}


    def register_user(self, user):
        self.users[user.user_id] = user


    def add_book(self, book):
        self.books[book.isbn] = book


    def perform_borrow(self, user_id, isbn):
        if user_id in self.users:
            user = self.users[user_id]
            if isbn in self.books:
                book = self.books[isbn]
                if book.is_available:
                    User.borrow_book(user, book)
                    book.is_available = False
                else:
                    try:
                        raise NameError
                    except:
                        print("the book is not available")
            else:# the book is not in the list
                try:
                    raise NameError
                except:
                    print("the book is not exist")
        else:
            try:
                raise NameError
            except:
                print("the user is not exist")
        Logger.log_action("BORROW", f"{user_id, isbn}")
        SystemAdmin.update_transactions_count()



    def perform_return(self, user_id: str, isbn: str) -> None:
        if user_id in self.users:
            if isbn in self.books:
                book = self.books["isbn"]
                if not book.is_available:
                    User.return_book(book)
                    book.is_available = True
                else:
                    try:
                        raise NameError
                    except:
                        print("something went wrong")
            else:# the book is not in the list
                try:
                    raise NameError
                except:
                    print("the book is not exist")
        else:
            try:
                raise NameError
            except:
                print("the user is not exist")
        Logger.log_action("RETURN", f"{user_id, isbn}")
        SystemAdmin.update_transactions_count()