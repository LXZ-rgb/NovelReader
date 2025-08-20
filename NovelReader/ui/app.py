import tkinter as tk
from ui.booklist import BookListView
from ui.reader_view import ReaderView
from core.library import Library

class NovelReaderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("小说阅读器")
        self.library = Library()
        self.booklist_view = BookListView(self.root, self.library, self.open_book)
        self.booklist_view.pack(fill="both", expand=True)
        self.reader_view = None

    def open_book(self, book):
        if self.reader_view:
            self.reader_view.pack_forget()
        self.reader_view = ReaderView(self.root, book)
        self.reader_view.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()