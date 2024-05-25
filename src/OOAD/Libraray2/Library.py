import datetime

from src.OOAD.Libraray2.Book import Book
from src.OOAD.Libraray2.Member import Member


class Borrow:
    def __init__(self):
        self.borrow_days = 30
        self.borrow_limit = 3
        self.fine = 4


class Library:
    def __init__(self):
        self.borrow = Borrow()
        self.member_dict = {}
        self.lib = {}
        self.book_id = 0
        self.member_id = 0

    def add_book(self, book_title, book_author, book_publication, book_year):
        new_book = Book(self.book_id, book_title, book_author, book_publication, book_year)
        self.lib[self.book_id] = new_book
        self.book_id += 1
        return "Book added"

    def search_book(self, search_book_id):
        if search_book_id in self.lib:
            return self.lib[search_book_id]
        return f"{search_book_id} not in Library."

    def remove_book(self, remove_book_id):
        if remove_book_id in self.lib:
            book = self.lib.pop(remove_book_id)
        return f"{book.book_id} - {book.title} removed from Library."

    def display_collection(self):
        print('{:>10}{:>10}{:>10}'.format("ID", "Title", "Author"))
        for i in self.lib:
            print('{:>10}{:>10}{:>10}'.format(i.id, i.title, i.author))

    def add_member(self, member_name):
        member = Member(self.member_id, member_name)
        self.member_dict[self.member_id] = member
        self.member_id += 1
        return f"{member_name} added."

    def show_members(self):
        print('{:>10}{:>10}{:>10}'.format("ID", "Member", "Books"))
        for i in self.member_dict:
            print('{:>10}{:>10}{:>10}'.format(i.member_id, i.member_name, i.borrow_list))

    def borrow_book(self, member_id, borrow_book_id):
        if borrow_book_id in self.lib:
            book = self.lib[borrow_book_id]
            if book.borrow_flag == 0:
                book.borrow_flag = 1
                book.borrow_time = datetime.now()
                book.member_id = member_id
                self.lib[borrow_book_id] = book
            else:
                return f"Book unavailable. Please check on {self.check_due_date(borrow_book_id)}"
        else:
            return "Invalid book id."

    def check_due_date(self, book_id):
        book = self.lib[book_id]
        due_date = book.borrow_time + datetime.timedelta(days = self.borrow.borrow_days)
        return due_date

    def calculate_fine(self, book_id):
        if datetime.now() > self.check_due_date(book_id):
            return (self.check_due_date(book_id) - datetime.now()).days * self.borrow.fine
