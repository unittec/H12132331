from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class MyDockWidget(QDockWidget):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)

        # 创建一个文本编辑框作为停靠窗口的内容
        text_edit = QTextEdit(self)
        self.setWidget(text_edit)
        # 设置停靠窗口的特性，禁止浮动和独立，不显示标题栏
        self.setWidget(QWidget(self))
        self.setTitleBarWidget(QWidget(self))
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)

        # # 初始化添加一个文本编辑框
        self._text_edit = QTextEdit(self)
        self.setWidget(self._text_edit)
