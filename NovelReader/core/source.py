import os

class BookSource:
    def list_books(self):
        raise NotImplementedError

    def download_book(self, book_id):
        raise NotImplementedError

# 本地源举例
class LocalSource(BookSource):
    def __init__(self, books_dir):
        self.books_dir = books_dir

    def list_books(self):
        import os
        return [f for f in os.listdir(self.books_dir) if f.endswith('.txt')]

    def download_book(self, book_id):
        path = os.path.join(self.books_dir, book_id + '.txt')
        if os.path.exists(path):
            return path
        return None