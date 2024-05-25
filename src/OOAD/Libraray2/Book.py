class Book:
    def __init__(self, IBSN, title, author, publication, year):
        self.book_id = IBSN
        self.title = title
        self.author = author
        self.publication = publication
        self.year = year
        self.borrow_flag = 0
        self.borrow_time = None
        self.member_id = None
