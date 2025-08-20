import os

class Book:
    def __init__(self, title, author, path, book_id=None):
        self.title = title
        self.author = author
        self.path = path
        self.book_id = book_id or self.generate_id()
        self.chapters = []
        self._load_content()

    def generate_id(self):
        return f"{self.title}_{self.author}".replace(" ", "_")

    def _load_content(self):
        # 简单以txt为例，章节拆分可扩展
        if self.path.endswith('.txt'):
            with open(self.path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.chapters = self._split_chapters(content)
        # 可扩展支持 epub、网络小说等
        # elif self.path.endswith('.epub'):
        #     pass
    
    def _sort_chapters(self,chapter):
        self.chapter = []
        

    def _split_chapters(self, content):
        # 按“第XX章”拆分，可自定义规则
        import re
        chapters = re.split(r'(第[\d一二三四五六七八九十百千]+章.*?)\n', content)
        #获取chapters中的部分字符串
        #调用函数
        result = []
        for i in range(1, len(chapters), 2):
            result.append({
                'title': chapters[i].strip(),
                'content': chapters[i+1].strip()
            })
        return result if result else [{'title': '正文', 'content': content}]