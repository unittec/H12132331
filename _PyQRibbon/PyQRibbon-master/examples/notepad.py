# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/4/10 16:39
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QToolButton, QPushButton, QAction, QSizePolicy, QLabel, \
    QMenu, QHBoxLayout, QTextEdit, QDockWidget

from PyQRibbon import QRibbonWindow


class Notepad(QRibbonWindow):
    def __init__(self):
        super(Notepad, self).__init__()
        self.resize(800, 600)

        # 设置标题
        self.title = "记事本"

        # 左侧添加按钮
        # saveBtn = QPushButton(QIcon('images/save.png'), '')
        # self.addLeftWidget(saveBtn)
        # saveBtn.setMouseTracking(True)

        # 右侧添加按钮
        # self.addRightWidget(QPushButton(QIcon("./images/smile.png"), ''))

        # 文件按钮点击事件
        fileButton = self.addFileButton("文件")
        fileButton.clicked.connect(lambda: print('file clicked'))

        # 添加标签
        tab = self.addTab("开始")
        widget = QWidget(tab)
        widget.setObjectName("groupWidget")
        gridLayout = QGridLayout(widget)
        gridLayout.setContentsMargins(3, 3, 3, 3)
        gridLayout.setSpacing(0)
        pasteToolBtn = QToolButton(widget)
        pasteToolBtn.setObjectName("pasteToolBtn")
        pasteToolBtn.setAutoRaise(True)
        pasteToolBtn.clicked.connect(lambda: print("clicked"))
        pasteToolBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        pasteToolBtn.setPopupMode(QToolButton.MenuButtonPopup)
        pasteToolBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 设置菜单
        menu = QMenu(pasteToolBtn)
        menu.addAction(QAction("粘贴", menu))
        menu.addAction(QAction("粘贴为纯文本", menu))
        pasteToolBtn.setMenu(menu)
        pasteToolBtn.setIcon(QIcon('./images/paste.png'))
        pasteToolBtn.setText('粘贴')
        pasteToolBtn.setDefaultAction(QAction(QIcon("./images/paste.png"), "test"))

        gridLayout.addWidget(pasteToolBtn, 0, 0, 3, 1)
        cutBtn = QPushButton(QIcon("./images/cut.png"), "剪切", widget)
        cutBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        gridLayout.addWidget(cutBtn, 0, 1, 1, 1)
        copyBtn = QPushButton(QIcon("./images/copy.png"), "复制", widget)
        copyBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        gridLayout.addWidget(copyBtn, 1, 1, 1, 1)
        brushBtn = QPushButton(QIcon("./images/format.png"), "格式刷", widget)
        brushBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        gridLayout.addWidget(brushBtn, 2, 1, 1, 1)
        # 添加分组
        tab.addGroup("剪贴板", widget, corner=True, cornerCallback=lambda: print('clicked'))
        # 添加分组
        widget = QLabel('在这里添加一个控件...')
        tab.addGroup("文件", widget)
        widget = QLabel('在这里添加一个控件...')
        tab.addGroup("文件", widget)


        # 添加第二个标签
        tab = self.addTab('插入')
        tab.addGroup('设计', QLabel("在这里添加一个控件..."))

        # 添加第三个标签
        tab = self.addTab('帮助')
        tab.addGroup(widget=QLabel(" 标签 "), line=True)
        tab.addGroup(widget=QPushButton(" 按钮 "), line=False)


        dock_widget = QDockWidget("可停靠窗口", self)
        #设置停靠窗口可以最小化
        dock_widget.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetVerticalTitleBar)


        dock_widget2 = QDockWidget("可停靠窗口2", self)
        text_edit = QTextEdit()
        dock_widget.setWidget(text_edit)
        dock_widget2.setWidget(text_edit)
        # self.setStyleSheet("background-color: black;")
        self.addDockWidget(Qt.RightDockWidgetArea, dock_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, dock_widget2)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)   # 这里是为了适配高分屏
    app = QApplication([])
    form = Notepad()
    form.show()

    # 设置样式
    app.setStyleSheet(open('./notepad.qss').read())

    # from pyqss import Qss
    #
    # qss = Qss(form)
    # qss.show()

    app.exec_()
