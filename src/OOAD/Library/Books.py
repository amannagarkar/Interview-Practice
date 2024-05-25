class Books:
    def __init__(self, book_id: int, title: str, content: list[[list]], author: str):
        self.id = book_id
        self.title = title
        self.content = content
        self.author = author
        self.active_page_number = 0

    def display_active_page(self):
        return self.content[self.active_page_number]

    def turn_page(self):
        self.active_page_number += 1
        return self.display_active_page()
