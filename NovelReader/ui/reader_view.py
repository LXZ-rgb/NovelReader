import tkinter as tk
from core.reader import Reader

class ReaderView(tk.Frame):
    def __init__(self, master, book):
        super().__init__(master)
        self.reader = Reader(book)
        self.text = tk.Text(self, wrap="word", font=("Arial", 14))
        self.text.pack(fill="both", expand=True)
        self.controls = tk.Frame(self)
        self.controls.pack(fill="x")
        tk.Button(self.controls, text="上一页", command=self.prev_page).pack(side="left")
        tk.Button(self.controls, text="下一页", command=self.next_page).pack(side="left")
        self.update_view()

    def update_view(self):
        self.text.delete(1.0, tk.END)
        content = self.reader.get_current_page_content()
        self.text.insert(tk.END, content)

    def next_page(self):
        self.reader.next_page()
        self.update_view()

    def prev_page(self):
        self.reader.prev_page()
        self.update_view()