import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QMenu, QAction, QVBoxLayout, QWidget, QDockWidget, QMainWindow

class TreeViewExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建DockWidget
        dock_widget = QDockWidget('Tree View with Context Menu', self)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

        # 创建树形视图
        tree_widget = QTreeWidget(dock_widget)
        tree_widget.setColumnCount(1)

        # 添加根节点
        root_item = QTreeWidgetItem(tree_widget, ['Root'])
        root_item.setIcon(0, QIcon('comsol_icons/material_32.png'))

        # 添加树形数据
        data = {'Folder': {'Item1': None, 'Item2': None},
                'File': {'Item3': None, 'Item4': None}}
        self.addTreeItems(data, root_item)

        # 启用右键菜单
        tree_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        tree_widget.customContextMenuRequested.connect(self.showContextMenu)

        # 将树形视图设置为DockWidget的widget
        dock_widget.setWidget(tree_widget)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Tree View with Context Menu')
        self.show()

    def addTreeItems(self, data, parent_item):
        for key, value in data.items():
            item = QTreeWidgetItem(parent_item, [str(key)])
            item.setIcon(0, QIcon('comsol_icons/material_32.png'))
            if isinstance(value, dict):
                # 如果值是字典，递归添加子项
                self.addTreeItems(value, item)

    def showContextMenu(self, pos):
        # 获取选中的item
        tree_widget = self.sender()
        item = tree_widget.itemAt(pos)
        if item is not None:
            item_text = item.text(0)

            # 根据item类型创建不同的右键菜单
            context_menu = self.createContextMenu(item)

            # 显示菜单
            context_menu.exec_(tree_widget.mapToGlobal(pos))

    def createContextMenu(self, item):
        item_type = 'Folder'  # 假设所有item的类型都是'Folder'，实际情况应根据你的数据结构进行判断

        # 创建右键菜单
        context_menu = QMenu(self)

        if item_type == 'Folder':
            # 添加文件夹菜单项
            action_open_folder = QAction('Open Folder', self)
            action_open_folder.triggered.connect(lambda: self.openFolder(item.text(0)))
            context_menu.addAction(action_open_folder)
        elif item_type == 'File':
            # 添加文件菜单项
            action_open_file = QAction('Open File', self)
            action_open_file.triggered.connect(lambda: self.openFile(item.text(0)))
            context_menu.addAction(action_open_file)

        # 添加通用菜单项
        action_common = QAction(f'Common Action for {item.text(0)}', self)
        action_common.triggered.connect(lambda: self.commonAction(item.text(0)))
        context_menu.addAction(action_common)

        return context_menu

    def openFolder(self, folder_name):
        print(f'Opening folder: {folder_name}')

    def openFile(self, file_name):
        print(f'Opening file: {file_name}')

    def commonAction(self, item_name):
        print(f'Performing common action for: {item_name}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TreeViewExample()
    sys.exit(app.exec_())
