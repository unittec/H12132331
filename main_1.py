import copy

import cv2
from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQRibbon import QRibbonWindow
from MyDockWidget import MyDockWidget
from AppConfig import *


class MyWindow(QRibbonWindow):

    def __init__(self):
        super(MyWindow, self).__init__()



        # 树形视图
        self.tree_view_dict = {
            "根节点1": {
                "这是一个excel类型节点": ['excel'],  # 值为若不是字典，那么就是叶子节点，当该节点为叶子节点时，用户数据使用列表表示，列表第一个元素在这个软件中为自定义的文件类型，例如['excel', ...]
                "文件": {
                    '这是一个txt类型节点': ['txt'],
                    '这是一个通用类型节点': ['None'],
                },
            },
            "根节点2": {
                "这是一个excel类型节点": ['excel'],
                "文件": {
                    '这是一个txt类型节点': ['txt'],
                    '这是一个通用类型节点': ['None'],
                    'nas文件': ['nas'],
                    'step文件': ['step'],
                    'dxf文件': ['dxf'],
                },
            }
        }
        # 树形视图图标
        self.file_type_icon = FILE_TYPE_ICON

        # 默认图标
        self._default_icon = "comsol_icons/animate.png"
        # 默认窗口大小
        self.resize(1000, 600)


        # 标题栏固定高度
        self._dock_title_fixed_height = 35  # 标题栏固定高度
        # 标题栏字体
        self._dock_font = QFont("Microsoft YaHei", 18, QFont.NoFontMerging, False)
        # 字体水平向上对齐
        self._dock_font.setLetterSpacing(QFont.AbsoluteSpacing, 0)
        # 停靠窗口边框样式表
        self._dock_style_sheet_normal = "QFrame { border: 1px solid  #e5e5e8;}"
        self._dock_style_sheet_focus = "QFrame { border: 1px solid  #9dd1f9;}"
        self._tree_dock_style_sheet_normal = "QFrame { border: 1px solid  #e5e5e8;; margin-left: 3px;}"
        self._tree_dock_style_sheet_focus = "QFrame { border: 1px solid  #9dd1f9;; margin-left: 3px;}"
        # 初始化内部停靠窗口
        self._dock_tree_view = MyDockWidget("左1", self)
        self._dock_setting_view = MyDockWidget("左2", self)
        self._dock_chart_view = MyDockWidget("右上", self)
        self._dock_msg_view = MyDockWidget("Messages", self)  # 消息窗口
        self._dock_log_view = MyDockWidget("Log", self)  # 日志窗口
        self._dock_progress_view = MyDockWidget("Progress", self)  # 进度窗口

        # 存储消息窗口的消息 列表数据模型
        self._msg_model = QStandardItemModel(self._dock_msg_view)

        # 记录当前选中的树形节点
        self._current_tree_item = None


        self.__init_ui()

    def __init_ui(self):
        # 设置标题
        self.setWindowTitle("MyWindow")

        self.ribbonWidget.tabPanel.foldButton.setVisible(False)

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
        gridLayout.addWidget(self._create_button(widget, '按钮01', self._default_icon, lambda: print("点击按钮00")), 0, 0, 1, 1)
        gridLayout.addWidget(self._create_button(widget, '按钮02', self._default_icon, lambda: print("点击按钮10")), 1, 0, 1, 1)
        gridLayout.addWidget(self._create_button(widget, '按钮03', self._default_icon, lambda: print("点击按钮20")), 2, 0, 1, 1)
        gridLayout.addWidget(self._create_button(widget, '按钮04', self._default_icon, lambda: print("点击按钮01")), 0, 1, 1, 1)
        gridLayout.addWidget(self._create_button(widget, '按钮05', self._default_icon, lambda: print("点击按钮11")), 1, 1, 1, 1)
        gridLayout.addWidget(self._create_button(widget, '按钮06', self._default_icon, lambda: print("点击按钮21")), 2, 1, 1, 1)
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
        # 按钮 文字 添加到布局中
        gridLayout.addWidget(button, 0, 0, 3, 2)
        gridLayout.addWidget(text, 2, 0, 2, 2)
        tab.addGroup("分组3", widget)

        """添加第2个标签页"""
        tab = self.addTab('标签2')
        # 创建第1个分组
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
        # 按钮 文字 添加到布局中
        gridLayout.addWidget(button, 0, 0, 3, 2)
        gridLayout.addWidget(text, 2, 0, 2, 2)
        tab.addGroup('分组1', widget)

        """添加第3个标签页"""
        tab = self.addTab('标签3')
        tab.addGroup('分组1', QLabel("在这里添加一个控件..."))

        # 设置窗口布局
        self._layout_setting()
        # 初始化树形视图窗
        self._init_tree_view(self._dock_tree_view, self.tree_view_dict)
        # 初始化设置窗口
        self._init_setting_view(self._dock_setting_view)
        # 初始化图表窗口
        self._init_chart_view(self._dock_chart_view)
        # 初始化消息窗口
        self._init_msg_view(self._dock_msg_view)


    def _init_tree_view(self, dock_widget: QDockWidget, tree_dict: dict):
        """根据字典初始化树形控件"""
        # 创建一个容器 QFrame，并设置为 DockWidget 的窗口部件
        frame = QFrame()
        frame.setStyleSheet(self._tree_dock_style_sheet_normal)

        dock_widget.setWidget(frame)    # set的时候会自动删除之前的widget 也就是说当修改了tree_dict后，再次调用_init_tree_view时，会重新创建一个新的树形控件

        # 使用布局管理器添加文本编辑器和树形控件到 QFrame
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)

        # 创建文本
        title = QLabel()
        title.setText("Tree View")

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
        # 节点被选中时 记录当前节点到self._current_tree_item
        tree_widget.itemSelectionChanged.connect(lambda: setattr(self, '_current_tree_item', tree_widget.currentItem()))

        # 内部函数，递归添加子项
        def add_tree_items(data, parent_item):
            for key, value in data.items():
                # 添加节点 并设置节点名称
                item = QTreeWidgetItem(parent_item, [str(key)])
                # 设置节点默认图标
                item.setIcon(0, QIcon(self._default_icon))
                # 如果值是字典，递归添加子节点
                if isinstance(value, dict):
                    add_tree_items(value, item)
                # 如果值是列表，那么就是叶子节点，设置item的类型和图标
                elif isinstance(value, list):
                    item_type = value[0]
                    if item_type:
                        item.setIcon(0, QIcon(self.file_type_icon[item_type]))
                    else:
                        item.setIcon(0, QIcon(self.file_type_icon['None']))
                    # 最后把值设置为item的data 以便后续右键菜单创建时使用 注意这里把整个列表都设置为data 使用时取第一个元素来判断类型
                    item.setData(0, Qt.UserRole, value)



        # 调用内部函数开始递归添加子项
        add_tree_items(tree_dict, tree_widget)
        # 启用右键菜单
        tree_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        tree_widget.customContextMenuRequested.connect(self.showContextMenu)
        # 将树形视图设置为DockWidget的widget
        layout.addWidget(tree_widget)

        # 容器获取焦点时 设置frame边框颜色
        tree_widget.focusInEvent = lambda event: frame.setStyleSheet(self._tree_dock_style_sheet_focus)
        # 容器失去焦点时 设置frame边框颜色 同时让文本编辑器也失去焦点
        tree_widget.focusOutEvent = lambda event: frame.setStyleSheet(self._tree_dock_style_sheet_normal)

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

    def _init_msg_view(self, dock_widget: QDockWidget):
        """初始化消息窗口"""
        # 创建一个容器 QFrame，并设置为 DockWidget 的窗口部件
        frame = QFrame()
        frame.setStyleSheet(self._dock_style_sheet_normal)
        dock_widget.setWidget(frame)

        # 使用布局管理器添加文本编辑器和树形控件到 QFrame
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)

        # 创建按钮条
        button_bar = QWidget()
        button_bar.setFixedHeight(24)
        # button_bar.setStyleSheet("background: #e5e5e8;")
        button_bar_layout = QHBoxLayout(button_bar)
        button_bar_layout.setContentsMargins(0, 0, 0, 0)
        button_bar_layout.setSpacing(0)
        # 按钮条内部按钮 左侧对齐 水平居中对齐
        button_bar_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)


        # 创建按钮
        button = self._create_icon_button(self._default_icon, QSize(20, 20), '清空')
        # 绑定点击事件
        # button.clicked.connect(lambda: self._msg_model.clear())
        button.clicked.connect(lambda: print("清空消息窗口"))
        button_bar_layout.addWidget(button)
        # 创建按钮
        button = self._create_icon_button(self._default_icon, QSize(20, 20), '添加消息')
        # 绑定点击事件 这里设置为添加一条消息到消息窗口
        button.clicked.connect(lambda: self._msg_model.appendRow(QStandardItem(f"{self._msg_model.rowCount() + 1}: 添加一条消息")))
        ...
        button_bar_layout.addWidget(button)

        # 添加按钮条到布局中
        layout.addWidget(button_bar)
        # 设置按钮条固定显示在顶部
        button_bar_layout.addStretch(1)


        # 创建列表视图 用于显示消息 位置在按钮条下方
        list_view = QListView(dock_widget)
        # 禁止编辑
        list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置垂直滚动条样式 滑动槽不显示 只显示滑动条 滑动条圆角4 颜色蓝色

        # 设置模型
        list_view.setModel(self._msg_model)
        # 设置边框1 颜色为 #d6d6d8
        list_view.setStyleSheet("border: 1px solid #d6d6d8;")
        layout.addWidget(list_view)

        # 容器获取焦点时 设置frame边框颜色
        list_view.focusInEvent = lambda event: frame.setStyleSheet(self._dock_style_sheet_focus)
        # 容器失去焦点时 设置frame边框颜色
        list_view.focusOutEvent = lambda event: frame.setStyleSheet(self._dock_style_sheet_normal)






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

    def showContextMenu(self, pos):
        # 获取选中的item
        tree_widget = self.sender()
        item = tree_widget.itemAt(pos)
        if item is not None:
            # 获取节点名称
            # item_text = item.text(0)

            # 根据节点类型创建不同的右键菜单
            context_menu = self.createContextMenu(item, node_type=item.data(0, Qt.UserRole))

            # 显示菜单
            context_menu.exec_(self._dock_tree_view.mapToGlobal(pos))

    def createContextMenu(self, item, node_type):
        _type = node_type[0] if isinstance(node_type, list) else None

        # 创建右键菜单
        context_menu = QMenu(self)

        def_icon = QIcon(self._default_icon)

        # 添加第一种节点菜单项
        if _type == 'excel':
            # 添加第一种节点菜单项
            action = QAction('excel类型节点 选项1', self)
            # 绑定选项1的点击事件
            action.triggered.connect(lambda: print("选中右键菜单.excel类型节点.选项1"))
            # 设置图标
            action.setIcon(def_icon)
            # 添加到右键菜单
            context_menu.addAction(action)
            # 完成第一种节点菜单项的添加


            action = QAction('excel类型节点 选项2', self)
            action.triggered.connect(lambda: print("选中右键菜单.excel类型节点.选项2"))
            action.setIcon(def_icon)
            context_menu.addAction(action)
        # 添加第二种节点菜单项
        elif _type == 'txt':
            action = QAction('txt类型节点 选项1', self)
            action.triggered.connect(lambda: print("选中右键菜单.txt类型节点.选项1"))
            action.setIcon(def_icon)
            context_menu.addAction(action)
            action = QAction('txt类型节点 选项2', self)
            action.triggered.connect(lambda: print("选中右键菜单.txt类型节点.选项2"))
            action.setIcon(def_icon)
            context_menu.addAction(action)

        # 添加分隔线
        context_menu.addSeparator()

        # 最后默认添加通用菜单项
        action_name = '删除'
        action = QAction(action_name, self)
        action.triggered.connect(lambda: self.delete_node(item))
        action.setIcon(def_icon)
        context_menu.addAction(action)

        # 如果有子节点，那么就添加添加子节点的菜单项
        if item.childCount() > 0:
            action_name = '添加子节点'
            # 为子节点添加用户数据
            user_data = ['txt']
            action = QAction(action_name, self)
            action.triggered.connect(lambda: self.add_child_node(item, '新节点', user_data))
            action.setIcon(def_icon)
            context_menu.addAction(action)

        action_name = '重命名'
        action = QAction(action_name, self)
        action.triggered.connect(lambda: print(f"选中右键菜单.重命名"))
        action.setIcon(def_icon)
        context_menu.addAction(action)

        # 添加分隔线
        context_menu.addSeparator()

        action_name = '设置'
        action = QAction(action_name, self)
        action.triggered.connect(lambda: print(f"选中右键菜单.设置"))
        action.setIcon(def_icon)
        context_menu.addAction(action)

        action_name = '属性'
        action = QAction(action_name, self)
        action.triggered.connect(lambda: print(f"选中右键菜单.属性"))
        action.setIcon(def_icon)
        context_menu.addAction(action)

        action_name = '帮助'
        action = QAction(action_name, self)
        action.triggered.connect(lambda: print(f"选中右键菜单.帮助"))
        action.setIcon(def_icon)
        context_menu.addAction(action)

        return context_menu

    # 删除节点
    def delete_node(self, item):
        # 获取节点的父节点
        parent = item.parent()
        # 如果父节点不为空，那么就删除该节点
        if parent is not None:
            parent.removeChild(item)

    # 添加子节点
    def add_child_node(self, item, text, user_data=None):
        # 根据用户数据获取节点类型
        _type = user_data[0] if isinstance(user_data, list) else None
        # 创建一个新的节点
        child = QTreeWidgetItem()
        # 设置节点名称
        child.setText(0, text)
        # 设置节点图标 使用默认图标
        child.setIcon(0, QIcon(self.file_type_icon[_type]))
        # 设置节点的用户数据
        if user_data is not None:
            child.setData(0, Qt.UserRole, user_data)
        # 添加到父节点中
        item.addChild(child)




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
    def _create_icon_button(icon_path: str, icon_size: QSize, tooltip_text: str) -> QPushButton:
        """创建一个纯图标按钮"""
        # 创建按钮
        bt = QPushButton()
        # 设置按钮图标
        bt.setIcon(QIcon(icon_path))
        # 设置按钮尺寸
        bt.setFixedSize(icon_size)
        bt.setToolTip(tooltip_text)

        return bt

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 这里是为了适配高分屏
    app = QApplication([])
    form = MyWindow()
    form.show()

    # 加载了一个外部样式文件 作为窗口的初始化样式
    app.setStyleSheet(open('./window.qss', encoding='utf-8').read())

    # from pyqss import Qss
    # qss = Qss(form)
    # qss.show()

    app.exec_()
