from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit
from PyQt5.QtCore import Qt

app = QApplication([])

# 创建主窗口
main_window = QMainWindow()
# main_window.setStyleSheet("background-color: black;")

# 创建可停靠的窗口
dock_widget = QDockWidget("可停靠窗口", main_window)
# 停靠窗
# dock_widget.setAllowedAreas(Qt.RightDockWidgetArea | Qt.LeftDockWidgetArea)
text_edit = QTextEdit()
dock_widget.setWidget(text_edit)

# 将可停靠窗口添加到主窗口
main_window.addDockWidget(Qt.RightDockWidgetArea, dock_widget)

# 显示主窗口
main_window.show()
app.exec_()
