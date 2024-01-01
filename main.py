import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QSplitter

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建四个停靠窗口
        dock1 = QDockWidget("Left 1", self)
        dock2 = QDockWidget("Left 2", self)
        dock3 = QDockWidget("Right Top", self)
        dock4 = QDockWidget("Right Bottom", self)
        dock4_2 = QDockWidget("Right Bottom 2", self)


        # 创建文本编辑框
        text_edit1 = QTextEdit(dock1)
        text_edit2 = QTextEdit(dock2)
        text_edit3 = QTextEdit(dock3)
        text_edit4 = QTextEdit(dock4)
        text_edit4_2 = QTextEdit(dock4_2)

        # 将文本编辑框放入停靠窗口
        dock1.setWidget(text_edit1)
        dock2.setWidget(text_edit2)
        dock3.setWidget(text_edit3)
        dock4.setWidget(text_edit4)
        dock4_2.setWidget(text_edit4_2)

        # 将左1停靠窗口放在左侧，占据1/4宽度
        self.addDockWidget(1, dock1)

        # 将左2停靠窗口放在左1停靠窗口的右侧，占据1/4宽度
        self.addDockWidget(2, dock2)

        # 使用 Splitter 放置左1和左2停靠窗口，占据1/2宽度
        splitter_left = QSplitter(self)
        splitter_left.addWidget(dock1)
        splitter_left.addWidget(dock2)
        self.setCentralWidget(splitter_left)

        # 将右上停靠窗口放在左1和左2停靠窗口的右侧
        self.addDockWidget(2, dock3)

        # 将右下停靠窗口放在左1和左2停靠窗口的右侧
        self.addDockWidget(2, dock4)
        # 将4_2放在与右下停靠窗口同一位置，通过标签切换显示
        self.tabifyDockWidget(dock4, dock4_2)

        # 设置主窗口属性
        self.setWindowTitle("Four Dock Example")
        self.setGeometry(100, 100, 800, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())
    # OKde
