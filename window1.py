# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '001.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1111, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(250, 251, 254);")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.action001 = QAction(MainWindow)
        self.action001.setObjectName(u"action001")
        self.action001_2 = QAction(MainWindow)
        self.action001_2.setObjectName(u"action001_2")
        self.action123456 = QAction(MainWindow)
        self.action123456.setObjectName(u"action123456")
        icon1 = QIcon(QIcon.fromTheme(u"applications-system"))
        self.action123456.setIcon(icon1)
        self.action123456.setMenuRole(QAction.NoRole)
        self.action999 = QAction(MainWindow)
        self.action999.setObjectName(u"action999")
        self.action999.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1111, 21))
        self.menubar.setStyleSheet(u"QMenuBar::item:selected {\n"
"	background-color: #368ccb; /* \u8bbe\u7f6e\u9009\u4e2d\u65f6\u7684\u80cc\u666f\u8272 */\n"
"	color: #FFFFFF; /* \u8bbe\u7f6e\u9009\u4e2d\u65f6\u7684\u6587\u5b57\u989c\u8272 */\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #368ccb; /* \u9009\u4e2d\u65f6\u7684\u80cc\u666f\u8272 */\n"
"    color: #FFFFFF; /* \u9009\u4e2d\u65f6\u7684\u6587\u5b57\u989c\u8272 */\n"
"}\n"
"")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setStyleSheet(u"")
        self.menu_1 = QMenu(self.menubar)
        self.menu_1.setObjectName(u"menu_1")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_6 = QMenu(self.menubar)
        self.menu_6.setObjectName(u"menu_6")
        self.menu_7 = QMenu(self.menubar)
        self.menu_7.setObjectName(u"menu_7")
        self.menu_8 = QMenu(self.menubar)
        self.menu_8.setObjectName(u"menu_8")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu_8.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menu_1.addAction(self.action001)
        self.menu_2.addAction(self.action001_2)
        self.toolBar.addAction(self.action999)
        self.toolBar.addAction(self.action123456)
        self.toolBar_2.addAction(self.action123456)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.action001.setText(QCoreApplication.translate("MainWindow", u"001", None))
        self.action001_2.setText(QCoreApplication.translate("MainWindow", u"0096", None))
        self.action123456.setText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.action999.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_1.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u6309\u94ae1", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u6309\u94ae2", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u6309\u94ae3", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u6309\u94ae4", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u6309\u94ae5", None))
        self.menu_6.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u6309\u94ae6", None))
        self.menu_7.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u6309\u94ae7", None))
        self.menu_8.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u6309\u94ae8", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

