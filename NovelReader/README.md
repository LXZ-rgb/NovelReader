# NovelReader

一个可扩展的小说阅读器，支持本地txt小说导入与阅读，易于扩展为支持epub/网络小说源。

## 项目结构
- core：数据结构与阅读核心逻辑
- ui：界面（Tkinter，可扩展PyQt/Web前端）
- utils：配置
- data/books：小说文件存放

## 运行
1. `pip install tk`
2. 将txt小说文件放入 `data/books/`
3. `python main.py`

## 扩展
- 支持epub、在线源（通过core/source.py扩展）
- UI可替换为更高级前端