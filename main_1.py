from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQRibbon import QRibbonWindow

from MyDockWidget import MyDockWidget


class MyWindow(QRibbonWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self._icon_path = r"icon/"

        self.resize(800, 600)

        self._dock_tree_view = MyDockWidget("左1", self)
        self._dock_setting_view = MyDockWidget("左2", self)
        self._dock_chart_view = MyDockWidget("右上", self)
        self._dock_msg_view = MyDockWidget("Messages", self)    # 消息窗口
        self._dock_log_view = MyDockWidget("Log", self)  # 日志窗口
        self._dock_progress_view = MyDockWidget("Progress", self)    # 进度窗口


        self.__init_ui()


    def __init_ui(self):
        # 设置标题
        self.setWindowTitle("MyWindow")

        # 文件按钮点击事件
        fileButton = self.addFileButton("文件")
        fileButton.clicked.connect(lambda: print('file clicked'))
        # 重新设置文件背景色和鼠标悬停背景色
        fileButton.setMouseTracking(True)

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
        pasteToolBtn.setIcon(QIcon(f"{self._icon_path}/paste.png"))
        pasteToolBtn.setText('粘贴')
        pasteToolBtn.setDefaultAction(QAction(QIcon(f"{self._icon_path}/paste.png"), "test"))

        gridLayout.addWidget(pasteToolBtn, 0, 0, 3, 1)
        cutBtn = QPushButton(QIcon(f"{self._icon_path}/cut.png"), "剪切", widget)
        cutBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        gridLayout.addWidget(cutBtn, 0, 1, 1, 1)
        copyBtn = QPushButton(QIcon(f"{self._icon_path}/copy.png"), "复制", widget)
        copyBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        gridLayout.addWidget(copyBtn, 1, 1, 1, 1)
        brushBtn = QPushButton(QIcon(f"{self._icon_path}/format.png"), "格式刷", widget)
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

        # 设置窗口布局
        self._layout_setting()
        self._init_tree_view(self._dock_tree_view, {"key1": "value1", "key2": "value2", "key3": {"key4": "value4"}})
        self._init_tree_view(self._dock_tree_view, {"123": {
                "key4": "value4",
                "key5": {'key6': 'value6', 'key7': 'value7'},
            }
        }
                             )

    def _init_tree_view(self, dock_widget: QDockWidget, tree_dict: dict):
        """根据字典创建树形控件"""
        tree_widget = QTreeWidget(dock_widget)
        # 设置缩进
        tree_widget.setIndentation(10) # 设置缩进 单位是像素
        tree_widget.setHeaderHidden(True)  # 隐藏表头
        # 内部函数，递归添加子项
        def add_tree_items(data, parent_item):
            for key, value in data.items():
                item = QTreeWidgetItem(parent_item, [str(key)])
                item.setIcon(0, QIcon('comsol_icons/material_32.png'))
                if isinstance(value, dict):
                    # 如果值是字典，递归添加子项
                    add_tree_items(value, item)

        # 调用内部函数开始递归添加子项
        add_tree_items(tree_dict, tree_widget)

        # 将树形控件设置为停靠窗口的主窗口
        dock_widget.setWidget(tree_widget)



    # 布局设置
    def _layout_setting(self):
        """布局设置"""
        # 添加窗口
        self.addDockWidget(Qt.LeftDockWidgetArea, self._dock_tree_view)
        self.addDockWidget(Qt.RightDockWidgetArea, self._dock_setting_view)
        self.addDockWidget(Qt.RightDockWidgetArea, self._dock_chart_view)
        self.addDockWidget(Qt.RightDockWidgetArea, self._dock_msg_view)

        # 使用 Splitter 放置左1和左2停靠窗口
        splitter_left = QSplitter(self)
        splitter_left.addWidget(self._dock_tree_view)
        splitter_left.addWidget(self._dock_setting_view)
        # 设置分隔条的宽度
        splitter_left.setHandleWidth(4)
        self.setCentralWidget(splitter_left)

        # 将图标窗口放在左1和左2窗口的右侧
        self.addDockWidget(2, self._dock_chart_view)

        # 将消息窗口放在左1和左2窗口的右侧
        self.addDockWidget(2, self._dock_msg_view)
        self.addDockWidget(2, self._dock_progress_view)
        # 添加标签页
        self.tabifyDockWidget(self._dock_msg_view, self._dock_log_view)
        self.tabifyDockWidget(self._dock_msg_view, self._dock_progress_view)




if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)   # 这里是为了适配高分屏
    app = QApplication([])
    form = MyWindow()
    form.show()

    # 设置样式 这里加载了一个外部样式文件 生效范围是整个应用程序
    app.setStyleSheet(open('./window.qss', encoding='utf-8').read())
    #
    # from pyqss import Qss
    # qss = Qss(form)
    # qss.show()

    app.exec_()