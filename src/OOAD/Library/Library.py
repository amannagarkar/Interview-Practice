from src.OOAD.Library.Books import Books


class Library:
    def __init__(self):
        self.library = dict()
        self.active_book = None
        self.book_id = 0

    def display_books(self):
        return self.library

    def add_book(self, title, content, author):
        new_book = Books(self.book_id, title, content, author)
        self.book_id += 1
        self.library[self.book_id] = new_book
        return "Book successfully added"

    def remove_book(self, delete_book_id):
        try:
            del self.library[delete_book_id]
        except KeyError:
            print(f"Book id {delete_book_id} not in library")
        else:
            print(f"Book {delete_book_id} successfully removed")

    def display_library_items(self):
        print('{:<10} {:<10} {:<10}'.format('ID', 'Title', 'Author'))
        for key, value in self.library.items():
            print('{:<10}{:<10} {:<10}'.format(value.id, value.title, value.author))

    def set_active_book(self, active_book_id):
        try:
            self.library[active_book_id]
        except KeyError:
            print(f"Book id {active_book_id} not in library")
        else:
            self.active_book = active_book_id
            print(f"Book {active_book_id} loaded")

    def display_active_page(self):
        if self.active_book is not None:
            return self.library[self.active_book].display_active_page()
        else:
            print("No active book selected")

    def turn_active_page(self):
        if self.active_book is not None:
            return self.library[self.active_book].turn_page()
        else:
            print("No active book selected")

