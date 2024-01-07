import cv2
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQRibbon import QRibbonWindow

from MyDockWidget import MyDockWidget


class MyWindow(QRibbonWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self._icon_path = r"icon/"
        self._comsol_icon_path = r"comsol_icons/"

        self._default_icon = f"{self._comsol_icon_path}/animate.png"

        self.resize(1000, 600)

        self._dock_tree_view = MyDockWidget("左1", self)
        self._dock_setting_view = MyDockWidget("左2", self)
        self._dock_chart_view = MyDockWidget("右上", self)
        self._dock_msg_view = MyDockWidget("Messages", self)  # 消息窗口
        self._dock_log_view = MyDockWidget("Log", self)  # 日志窗口
        self._dock_progress_view = MyDockWidget("Progress", self)  # 进度窗口

        self._dock_title_fixed_height = 35  # 标题栏固定高度
        # 标题栏字体
        self._dock_font = QFont("Microsoft YaHei", 18, QFont.NoFontMerging, False)
        # 字体水平向上对齐
        self._dock_font.setLetterSpacing(QFont.AbsoluteSpacing, 0)

        # 窗口边框样式表
        self._dock_style_sheet_normal = "QFrame { border: 1px solid  #e5e5e8;}"
        self._dock_style_sheet_focus = "QFrame { border: 1px solid  #9dd1f9;}"
        self._tree_dock_style_sheet_normal = "QFrame { border: 1px solid  #e5e5e8;; margin-left: 3px;}"
        self._tree_dock_style_sheet_focus = "QFrame { border: 1px solid  #9dd1f9;; margin-left: 3px;}"

        self.__init_ui()

    def __init_ui(self):
        # 设置标题
        self.setWindowTitle("MyWindow")

        # 文件按钮点击事件
        fileButton = self.addFileButton("文件")
        # 设置样式表 正常状态下的背景色为红色，鼠标悬停时的背景色为绿色 点击时的背景色为蓝色 边框为0
        fileButton.setStyleSheet(
            "QPushButton { background-color: #368ccb; }"
            "QPushButton:hover { background-color: #368ccb; }"
            "QPushButton:pressed { background-color: #5074ac; }"
            "QPushButton { border: none; }")
        fileButton.clicked.connect(lambda: print('file clicked'))
        # 重新设置文件背景色和鼠标悬停背景色
        fileButton.setMouseTracking(True)

        """添加第1个标签页"""
        group_base_width = 62  # 标准分组宽度
        tab = self.addTab("标签1")
        # 创建第1个分组
        widget = QLabel()
        widget.setFixedWidth(group_base_width * 2)  # 设置分组的宽度
        # 添加布局
        gridLayout = QGridLayout(widget)
        gridLayout.setContentsMargins(3, 3, 3, 3)   # 边距
        gridLayout.setSpacing(0)                    # 间距
        # 添加工具按钮
        pasteToolBtn = QToolButton(widget)
        pasteToolBtn.setObjectName("pasteToolBtn")
        pasteToolBtn.setAutoRaise(True)
        pasteToolBtn.clicked.connect(lambda: print("11"))
        pasteToolBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        pasteToolBtn.setPopupMode(QToolButton.MenuButtonPopup)
        pasteToolBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 为工具按钮创建菜单
        menu = QMenu(pasteToolBtn)
        menu.addAction(QAction(QIcon(self._default_icon), "工具选项1", menu))
        menu.addAction(QAction(QIcon(self._default_icon), "工具选项2", menu))
        pasteToolBtn.setMenu(menu)
        pasteToolBtn.setIcon(QIcon(self._default_icon))
        pasteToolBtn.setDefaultAction(QAction(QIcon(self._default_icon), "工具按钮"))
        # 添加其他按钮
        bt1 = self._create_button(widget, '按钮1', self._default_icon)
        bt1.clicked.connect(lambda: print("点击按钮1"))    # 绑定按钮的clicked事件
        bt2 = self._create_button(widget, '按钮2', self._default_icon)
        bt3 = self._create_button(widget, '按钮3', self._default_icon)

        # 添加到布局中
        gridLayout.addWidget(bt1, 0, 1, 1, 1)   # 添加到布局中 位置为0行1列 占1行1列
        gridLayout.addWidget(bt2, 1, 1, 1, 1)   # 添加到布局中 位置为1行1列 占1行1列
        gridLayout.addWidget(bt3, 2, 1, 1, 1)   # 添加到布局中 位置为2行1列 占1行1列
        gridLayout.addWidget(pasteToolBtn, 0, 0, 3, 1)  # 添加到布局中 位置为0行0列 占3行1列
        # 最后设置分组1名称
        tab.addGroup("分组1", widget)

        # 创建第2个分组
        widget = QLabel()
        widget.setFixedWidth(group_base_width * 2)
        # 创建布局
        gridLayout = QGridLayout(widget)
        gridLayout.setContentsMargins(3, 3, 3, 3)
        gridLayout.setSpacing(0)
        # 添加按钮
        gridLayout.addWidget(self._create_button(widget, '按钮', self._default_icon, lambda: print("点击按钮00")), 0, 0, 1, 1)
        gridLayout.addWidget(self._create_button(widget, '按钮', self._default_icon, lambda: print("点击按钮10")), 1, 0, 1, 1)
        gridLayout.addWidget(self._create_button(widget, '按钮', self._default_icon, lambda: print("点击按钮20")), 2, 0, 1, 1)
        gridLayout.addWidget(self._create_button(widget, '按钮', self._default_icon, lambda: print("点击按钮01")), 0, 1, 1, 1)
        gridLayout.addWidget(self._create_button(widget, '按钮', self._default_icon, lambda: print("点击按钮11")), 1, 1, 1, 1)
        gridLayout.addWidget(self._create_button(widget, '按钮', self._default_icon, lambda: print("点击按钮21")), 2, 1, 1, 1)
        # 设置名称
        tab.addGroup("分组2", widget)

        # 创建第3个分组
        widget = QLabel()
        widget.setFixedWidth(group_base_width)
        # 创建布局
        gridLayout = QGridLayout(widget)
        gridLayout.setContentsMargins(3, 3, 3, 3)
        gridLayout.setSpacing(0)
        # 创建一个大按钮
        button = self._create_big_button(widget, '', self._default_icon, lambda: print("点击按钮"))
        text = QLabel("大按钮")
        # 文字水平居中 对齐顶部
        text.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        gridLayout.addWidget(button, 0, 0, 3, 2)
        gridLayout.addWidget(text, 2, 0, 2, 2)
        tab.addGroup("分组3", widget)

        """添加第2个标签页"""
        tab = self.addTab('标签2')
        tab.addGroup('设计', QLabel("在这里添加一个控件..."))

        """添加第3个标签页"""
        tab = self.addTab('标签3')
        tab.addGroup(widget=QLabel(" 标签 "), line=True)
        tab.addGroup(widget=QPushButton(" 按钮 "), line=False)




        # 设置窗口布局
        self._layout_setting()
        # 初始化窗口
        self._init_tree_view(self._dock_tree_view, {"key1": "value1", "key2": "value2", "key3": {"key4": "value4"}})
        self._init_tree_view(self._dock_tree_view, {"123": {
            "key4": "value4",
            "key5": {'key6': 'value6', 'key7': 'value7'},
        }
        }
                             )
        self._init_setting_view(self._dock_setting_view)
        self._init_chart_view(self._dock_chart_view)

    def _init_tree_view(self, dock_widget: QDockWidget, tree_dict: dict):
        """根据字典创建树形控件"""
        # 创建一个容器 QFrame，并设置为 DockWidget 的窗口部件
        frame = QFrame()
        frame.setStyleSheet(self._tree_dock_style_sheet_normal)

        dock_widget.setWidget(frame)

        # 使用布局管理器添加文本编辑器和树形控件到 QFrame
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)

        # 创建文本
        title = QLabel()
        title.setText("Setting View")

        # 设置字体
        title.setFont(self._dock_font)

        # 设置文本颜色 和 边框颜色
        title.setStyleSheet("color: #5074ac; border: 0px;")
        # 设置文本的固定高度
        title.setFixedHeight(self._dock_title_fixed_height)
        layout.addWidget(title)

        # 创建树形控件
        tree_widget = QTreeWidget(dock_widget)
        # 设置缩进
        tree_widget.setIndentation(10)  # 设置缩进 单位是像素
        tree_widget.setHeaderHidden(True)  # 隐藏表头
        # 设置样式
        tree_widget.setStyleSheet(
            "QTreeWidget { "
            "color: 'black';"
            "background: #00000000; "
            "border: 1px solid #e5e5e8;"
            "margin: 1px; "
            "}"
            "QTreeWidget:focus { border: 1px solid  #e5e5e8; }"
            "QTreeWidget::item { border:1px solid #00000000; }"
            "QTreeWidget::item:hover { background: #e2f2fe; }"  
            "QTreeWidget::item:selected { color: 'black'; }"
            "QTreeWidget::item:selected:active { background: #c0e2fc; }"
        )

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
        layout.addWidget(tree_widget)

        # 容器获取焦点时 设置frame边框颜色
        tree_widget.focusInEvent = lambda event: frame.setStyleSheet(self._tree_dock_style_sheet_focus)
        # 容器失去焦点时 设置frame边框颜色 同时让文本编辑器也失去焦点
        tree_widget.focusOutEvent = lambda event: frame.setStyleSheet(self._tree_dock_style_sheet_normal)

        return

        # 创建一个容器 widget，并设置为 DockWidget 的主要窗口部件
        container_widget = QWidget()
        dock_widget.setWidget(container_widget)

        # 使用布局管理器添加文本编辑器和树形控件到 QFrame
        layout = QVBoxLayout(container_widget)
        layout.setContentsMargins(3, 0, 0, 0)
        # 创建文本
        title = QLabel()
        title.setText("Tree View")
        # 设置字体
        title.setFont(self._dock_font)
        # 设置文本颜色
        title.setStyleSheet("color: #5074ac;")
        # 设置文本编辑器的固定高度
        title.setFixedHeight(self._dock_title_fixed_height)
        layout.addWidget(title)

        # 创建树形控件
        tree_widget = QTreeWidget(dock_widget)
        # 设置缩进
        tree_widget.setIndentation(10)  # 设置缩进 单位是像素
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
        # dock_widget.setWidget(tree_widget)
        layout.addWidget(tree_widget)

    def _init_setting_view(self, dock_widget: QDockWidget):
        """初始化设置窗口"""
        # 创建一个容器 QFrame，并设置为 DockWidget 的窗口部件
        frame = QFrame()
        frame.setStyleSheet(self._dock_style_sheet_normal)
        dock_widget.setWidget(frame)

        # 使用布局管理器添加文本编辑器和树形控件到 QFrame
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)

        # 创建文本
        title = QLabel()
        title.setText("Setting View")

        # 设置字体
        title.setFont(self._dock_font)

        # 设置文本颜色 和 边框颜色
        title.setStyleSheet("color: #5074ac; border: 0px;")
        # 设置文本的固定高度
        title.setFixedHeight(self._dock_title_fixed_height)
        layout.addWidget(title)

        # 临时创建一个文本编辑器
        text_edit = QTextEdit(dock_widget)
        # 设置边框0
        text_edit.setStyleSheet("border: 0px;")
        layout.addWidget(text_edit)

        # 容器获取焦点时 设置frame边框颜色
        text_edit.focusInEvent = lambda event: frame.setStyleSheet(self._dock_style_sheet_focus)
        # 容器失去焦点时 设置frame边框颜色 同时让文本编辑器也失去焦点
        text_edit.focusOutEvent = lambda event: frame.setStyleSheet(self._dock_style_sheet_normal)

    def _init_chart_view(self, dock_widget: QDockWidget):
        """初始化图表窗口"""
        # 创建一个容器 QFrame，并设置为 DockWidget 的窗口部件
        frame = QFrame()
        frame.setStyleSheet(self._dock_style_sheet_normal)
        dock_widget.setWidget(frame)

        # 使用布局管理器添加文本编辑器和树形控件到 QFrame
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)

        # 创建文本
        title = QLabel()
        title.setText("Chart View")

        # 设置字体
        title.setFont(self._dock_font)

        # 设置文本颜色 和 边框颜色
        title.setStyleSheet("color: #5074ac; border: 0px;")
        # 设置文本的固定高度
        title.setFixedHeight(self._dock_title_fixed_height)
        layout.addWidget(title)

        # 临时创建一个文本编辑器
        text_edit = QTextEdit(dock_widget)
        # 设置边框0
        text_edit.setStyleSheet("border: 0px;")
        layout.addWidget(text_edit)

        # 容器获取焦点时 设置frame边框颜色
        text_edit.focusInEvent = lambda event: frame.setStyleSheet(self._dock_style_sheet_focus)
        # 容器失去焦点时 设置frame边框颜色 同时让文本编辑器也失去焦点
        text_edit.focusOutEvent = lambda event: frame.setStyleSheet(self._dock_style_sheet_normal)

    # 布局设置
    def _layout_setting(self):
        """布局设置"""
        # 添加左侧两个窗口
        self.addDockWidget(Qt.LeftDockWidgetArea, self._dock_tree_view)
        self.addDockWidget(Qt.RightDockWidgetArea, self._dock_setting_view)
        # 设置self._dock_tree_view 和  self._dock_setting_view 的占比策略 前者占宽度的1/3
        w = int(self.width() * 2 / 3)
        docks = [self._dock_tree_view, self._dock_setting_view]
        sizes = [int(w * 1 / 4), int(w * 3 / 4)]
        self.resizeDocks(docks, sizes, Qt.Horizontal)
        # 使用 Splitter 放置左1和左2停靠窗口
        splitter_left = QSplitter(self)
        splitter_left.addWidget(self._dock_tree_view)
        splitter_left.addWidget(self._dock_setting_view)
        # 设置分隔条的宽度
        splitter_left.setHandleWidth(3)
        self.setCentralWidget(splitter_left)

        # 添加右侧窗口
        self.addDockWidget(Qt.RightDockWidgetArea, self._dock_chart_view)
        self.addDockWidget(Qt.RightDockWidgetArea, self._dock_msg_view)
        # 将图标窗口放在左1和左2窗口的右侧
        self.addDockWidget(2, self._dock_chart_view)
        # 将消息窗口放在左1和左2窗口的右侧
        self.addDockWidget(2, self._dock_msg_view)
        self.addDockWidget(2, self._dock_progress_view)
        # 设置self._dock_chart_view 和  self._dock_msg_view 的占比策略 前者占高度度的1/3
        docks = [self._dock_chart_view, self._dock_msg_view]
        sizes = [int(self.height() * 2 / 3), int(self.height() * 1 / 3)]
        self.resizeDocks(docks, sizes, Qt.Vertical)
        # 添加标签页
        self.tabifyDockWidget(self._dock_msg_view, self._dock_log_view)
        self.tabifyDockWidget(self._dock_msg_view, self._dock_progress_view)

    @staticmethod
    def _create_button(parent: QWidget, text='button', icon_path='', func=None) -> QPushButton:
        """创建一个按钮"""
        bt = QPushButton(QIcon(icon_path), text, parent)
        # 如果func是一个函数，那么绑定到按钮的clicked事件
        if callable(func):
            bt.clicked.connect(func)
        bt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        return bt

    @staticmethod
    def _create_big_button(parent: QWidget, text='button', icon_path='', func=None) -> QPushButton:
        """创建一个大图标按钮"""
        bt = QPushButton(text, parent)
        # 如果func是一个函数，那么绑定到按钮的clicked事件
        if callable(func):
            bt.clicked.connect(func)
        bt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 使用opencv读取图标放大后设置为按钮的图标
        img = cv2.imread(icon_path, cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
        bt.setIcon(QIcon(QPixmap.fromImage(QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGBA8888))))
        bt.setIconSize(QSize(32, 32))
        return bt

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 这里是为了适配高分屏
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
