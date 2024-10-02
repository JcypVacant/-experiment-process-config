# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newflowitem.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_NewFlowItem(object):
    def setupUi(self, NewFlowItem):
        if not NewFlowItem.objectName():
            NewFlowItem.setObjectName(u"NewFlowItem")
        NewFlowItem.resize(448, 427)
        NewFlowItem.setModal(True)
        self.label = QLabel(NewFlowItem)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 10, 91, 41))
        self.confirmPushButton = QPushButton(NewFlowItem)
        self.confirmPushButton.setObjectName(u"confirmPushButton")
        self.confirmPushButton.setGeometry(QRect(240, 350, 75, 24))
        self.pushButton_3 = QPushButton(NewFlowItem)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(350, 350, 75, 24))
        self.layoutWidget = QWidget(NewFlowItem)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 240, 189, 23))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.actionIDLineEdit = QLineEdit(self.layoutWidget)
        self.actionIDLineEdit.setObjectName(u"actionIDLineEdit")

        self.horizontalLayout_8.addWidget(self.actionIDLineEdit)

        self.layoutWidget1 = QWidget(NewFlowItem)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(80, 160, 291, 26))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.actionComboBox = QComboBox(self.layoutWidget1)
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.addItem("")
        self.actionComboBox.setObjectName(u"actionComboBox")

        self.horizontalLayout_9.addWidget(self.actionComboBox)

        self.createActionPushButton = QPushButton(self.layoutWidget1)
        self.createActionPushButton.setObjectName(u"createActionPushButton")

        self.horizontalLayout_9.addWidget(self.createActionPushButton)

        self.startTimeLineEdit = QLineEdit(NewFlowItem)
        self.startTimeLineEdit.setObjectName(u"startTimeLineEdit")
        self.startTimeLineEdit.setGeometry(QRect(146, 90, 133, 21))
        self.label_2 = QLabel(NewFlowItem)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 90, 60, 16))

        self.retranslateUi(NewFlowItem)

        QMetaObject.connectSlotsByName(NewFlowItem)
    # setupUi

    def retranslateUi(self, NewFlowItem):
        NewFlowItem.setWindowTitle(QCoreApplication.translate("NewFlowItem", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("NewFlowItem", u"\u521b\u5efa\u5b9e\u9a8c\u6d41\u7a0b\u9879", None))
        self.confirmPushButton.setText(QCoreApplication.translate("NewFlowItem", u"\u786e\u5b9a", None))
        self.pushButton_3.setText(QCoreApplication.translate("NewFlowItem", u"\u53d6\u6d88", None))
        self.label_9.setText(QCoreApplication.translate("NewFlowItem", u"\u52a8\u4f5cID\uff1a", None))
        self.actionComboBox.setItemText(0, QCoreApplication.translate("NewFlowItem", u"0\u7089\u5b50\u5f00\u5173", None))
        self.actionComboBox.setItemText(1, QCoreApplication.translate("NewFlowItem", u"1\u7089\u4e1d\u7535\u673a\u53c2\u6570", None))
        self.actionComboBox.setItemText(2, QCoreApplication.translate("NewFlowItem", u"2\u8f6c\u673a1", None))
        self.actionComboBox.setItemText(3, QCoreApplication.translate("NewFlowItem", u"3\u6837\u63d0\u673a2", None))
        self.actionComboBox.setItemText(4, QCoreApplication.translate("NewFlowItem", u"4\u7089\u4e0a\u673a3", None))
        self.actionComboBox.setItemText(5, QCoreApplication.translate("NewFlowItem", u"5\u7089\u4e2d\u673a4", None))
        self.actionComboBox.setItemText(6, QCoreApplication.translate("NewFlowItem", u"6\u7089\u4e0b\u673a5", None))
        self.actionComboBox.setItemText(7, QCoreApplication.translate("NewFlowItem", u"7\u7535\u673a\u72b6\u6001\u67e5\u8be2", None))
        self.actionComboBox.setItemText(8, QCoreApplication.translate("NewFlowItem", u"8\u78c1\u573a", None))
        self.actionComboBox.setItemText(9, QCoreApplication.translate("NewFlowItem", u"9\u7535\u673a\u78c1\u573a\u7535\u6d41", None))
        self.actionComboBox.setItemText(10, QCoreApplication.translate("NewFlowItem", u"10\u7089\u4e1d\u52a0\u70ed\u7535\u538b", None))
        self.actionComboBox.setItemText(11, QCoreApplication.translate("NewFlowItem", u"11PID\u63a7\u6e29\u66f2\u7ebf\u8bbe\u7f6e", None))
        self.actionComboBox.setItemText(12, QCoreApplication.translate("NewFlowItem", u"12\u5728\u7ebf\u76d1\u63a7\u72b6\u6001\u67e5\u8be2\u8868", None))
        self.actionComboBox.setItemText(13, QCoreApplication.translate("NewFlowItem", u"13\u7535\u673a\u5173\u95ed\u8bbe\u7f6e", None))
        self.actionComboBox.setItemText(14, QCoreApplication.translate("NewFlowItem", u"14\u5728\u7ebf\u76d1\u63a7\u8868\u5934\u8bbe\u7f6e", None))
        self.actionComboBox.setItemText(15, QCoreApplication.translate("NewFlowItem", u"15PID\u53c2\u6570\u8bbe\u7f6e\u52a8\u4f5c\u8868", None))

        self.createActionPushButton.setText(QCoreApplication.translate("NewFlowItem", u"\u521b\u5efa\u52a8\u4f5c", None))
        self.label_2.setText(QCoreApplication.translate("NewFlowItem", u"\u8d77\u59cb\u65f6\u523b\uff1a", None))
    # retranslateUi

