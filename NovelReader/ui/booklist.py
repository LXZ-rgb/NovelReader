import tkinter as tk

class BookListView(tk.Frame):
    def __init__(self, master, library, open_book_callback):
        super().__init__(master)
        self.library = library
        self.open_book_callback = open_book_callback
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill="both", expand=True)
        self.refresh()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for book in self.library.get_books():
            self.listbox.insert(tk.END, f"{book.title} - {book.author}")

    def on_select(self, event):
        if self.listbox.curselection():
            idx = self.listbox.curselection()[0]
            book = self.library.get_books()[idx]
            self.open_book_callback(book)