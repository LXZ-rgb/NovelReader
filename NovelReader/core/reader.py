class Reader:
    def __init__(self, book):
        self.book = book
        self.current_chapter = 0
        self.current_page = 0
        self.page_size = 800  # 每页字数，可配置

    def get_current_page_content(self):
        chapter = self.book.chapters[self.current_chapter]
        start = self.current_page * self.page_size
        end = start + self.page_size
        return chapter['content'][start:end]

    def next_page(self):
        chapter = self.book.chapters[self.current_chapter]
        if (self.current_page + 1) * self.page_size < len(chapter['content']):
            self.current_page += 1
        else:
            self.next_chapter()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        else:
            self.prev_chapter()

    def next_chapter(self):
        if self.current_chapter < len(self.book.chapters) - 1:
            self.current_chapter += 1
            self.current_page = 0

    def prev_chapter(self):
        if self.current_chapter > 0:
            self.current_chapter -= 1
            self.current_page = 0

    def save_progress(self):
        # 可扩展为写入配置文件
        pass

    def load_progress(self):
        pass