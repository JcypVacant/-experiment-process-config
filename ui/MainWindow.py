# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1153, 823)
        self.newFlowTableAction = QAction(MainWindow)
        self.newFlowTableAction.setObjectName(u"newFlowTableAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 30, 61, 31))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(300, 40, 241, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(590, 40, 54, 16))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(650, 40, 113, 20))
        self.flowTableWidget = QTableWidget(self.centralwidget)
        if (self.flowTableWidget.columnCount() < 10):
            self.flowTableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.flowTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.flowTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.flowTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.flowTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.flowTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.flowTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.flowTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.flowTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.flowTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.flowTableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.flowTableWidget.rowCount() < 128):
            self.flowTableWidget.setRowCount(128)
        self.flowTableWidget.setObjectName(u"flowTableWidget")
        self.flowTableWidget.setGeometry(QRect(40, 130, 1051, 501))
        self.flowTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.flowTableWidget.setShowGrid(True)
        self.flowTableWidget.setWordWrap(True)
        self.flowTableWidget.setRowCount(128)
        self.flowTableWidget.setColumnCount(10)
        self.newItemButton = QPushButton(self.centralwidget)
        self.newItemButton.setObjectName(u"newItemButton")
        self.newItemButton.setGeometry(QRect(260, 80, 75, 24))
        self.savePushButton = QPushButton(self.centralwidget)
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(530, 80, 75, 24))
        self.resetPushButton = QPushButton(self.centralwidget)
        self.resetPushButton.setObjectName(u"resetPushButton")
        self.resetPushButton.setGeometry(QRect(670, 80, 75, 24))
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(200, 690, 101, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(350, 690, 75, 24))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(610, 690, 75, 24))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(750, 690, 75, 24))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(470, 690, 75, 24))
        self.deleteItemPushButton = QPushButton(self.centralwidget)
        self.deleteItemPushButton.setObjectName(u"deleteItemPushButton")
        self.deleteItemPushButton.setGeometry(QRect(390, 80, 75, 24))
        self.loadDataPushButton = QPushButton(self.centralwidget)
        self.loadDataPushButton.setObjectName(u"loadDataPushButton")
        self.loadDataPushButton.setGeometry(QRect(110, 80, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1153, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9ad8\u6e29\u67dc\u6d41\u7a0b\u8f6f\u4ef6", None))
        self.newFlowTableAction.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5b9e\u9a8c\u6d41\u7a0b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u9a8c\u540d\u79f0\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f7d\u8377\u540d\u79f0\uff1a", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u6e29\u67dc", None))
        ___qtablewidgetitem = self.flowTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.flowTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u8d77\u59cb\u65f6\u523b", None));
        ___qtablewidgetitem2 = self.flowTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u8d77\u59cb\u6761\u4ef6", None));
        ___qtablewidgetitem3 = self.flowTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u540d\u79f0\u4e0e\u63cf\u8ff0", None));
        ___qtablewidgetitem4 = self.flowTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u7ed3\u675f\u5224\u636e", None));
        ___qtablewidgetitem5 = self.flowTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u672c\u52a8\u4f5c\u591a\u957f\u65f6\u95f4\u540e\u4e0b\u4e00\u4e2a\u52a8\u4f5c", None));
        ___qtablewidgetitem6 = self.flowTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u65f6\u95f4\n"
"\uff08s\uff09", None));
        ___qtablewidgetitem7 = self.flowTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        ___qtablewidgetitem8 = self.flowTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5cID", None));
        ___qtablewidgetitem9 = self.flowTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u662f\u65b0\u52a8\u4f5c", None));
        self.newItemButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u6d41\u7a0b\u9879", None))
        self.savePushButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.resetPushButton.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u52a8\u4f5c\u8868", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u52a8\u6001\u8868", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u9759\u6001\u8868", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u603b\u8868", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u76d1\u63a7\u8868", None))
        self.deleteItemPushButton.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6d41\u7a0b\u9879", None))
        self.loadDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e", None))
    # retranslateUi

