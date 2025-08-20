import os
from core.book import Book

class Library:
    def __init__(self, books_dir="data/books"):
        self.books_dir = books_dir
        self.books = []
        self._load_books()

    def _load_books(self):
        self.books.clear()
        for filename in os.listdir(self.books_dir):
            if filename.endswith(".txt"):
                path = os.path.join(self.books_dir, filename)
                book = Book(title=filename[:-4], author="未知", path=path)
                self.books.append(book)

    def add_book(self, path, title=None, author="未知"):
        # 支持扩展格式
        book = Book(title or os.path.basename(path), author, path)
        self.books.append(book)
        # 可选择复制文件到 books_dir

    def get_books(self):
        return self.books