# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stove3.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Stove3(object):
    def setupUi(self, Stove3):
        if not Stove3.objectName():
            Stove3.setObjectName(u"Stove3")
        Stove3.resize(797, 687)
        self.label = QLabel(Stove3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 10, 101, 31))
        self.label_2 = QLabel(Stove3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 80, 121, 21))
        self.runModeComboBox = QComboBox(Stove3)
        self.runModeComboBox.addItem("")
        self.runModeComboBox.addItem("")
        self.runModeComboBox.addItem("")
        self.runModeComboBox.setObjectName(u"runModeComboBox")
        self.runModeComboBox.setGeometry(QRect(210, 80, 131, 22))
        self.label_3 = QLabel(Stove3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 120, 141, 21))
        self.valLineEdit_1 = QLineEdit(Stove3)
        self.valLineEdit_1.setObjectName(u"valLineEdit_1")
        self.valLineEdit_1.setGeometry(QRect(210, 120, 131, 21))
        self.label_4 = QLabel(Stove3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 160, 151, 21))
        self.valLineEdit_2 = QLineEdit(Stove3)
        self.valLineEdit_2.setObjectName(u"valLineEdit_2")
        self.valLineEdit_2.setGeometry(QRect(210, 160, 131, 21))
        self.valLineEdit_3 = QLineEdit(Stove3)
        self.valLineEdit_3.setObjectName(u"valLineEdit_3")
        self.valLineEdit_3.setGeometry(QRect(210, 200, 131, 21))
        self.label_5 = QLabel(Stove3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 200, 131, 21))
        self.valLineEdit_4 = QLineEdit(Stove3)
        self.valLineEdit_4.setObjectName(u"valLineEdit_4")
        self.valLineEdit_4.setGeometry(QRect(210, 240, 131, 21))
        self.label_6 = QLabel(Stove3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 240, 131, 21))
        self.label_7 = QLabel(Stove3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 280, 111, 21))
        self.switchValComboBox = QComboBox(Stove3)
        self.switchValComboBox.addItem("")
        self.switchValComboBox.addItem("")
        self.switchValComboBox.addItem("")
        self.switchValComboBox.addItem("")
        self.switchValComboBox.addItem("")
        self.switchValComboBox.addItem("")
        self.switchValComboBox.addItem("")
        self.switchValComboBox.addItem("")
        self.switchValComboBox.addItem("")
        self.switchValComboBox.addItem("")
        self.switchValComboBox.addItem("")
        self.switchValComboBox.setObjectName(u"switchValComboBox")
        self.switchValComboBox.setGeometry(QRect(210, 280, 131, 22))
        self.label_8 = QLabel(Stove3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 320, 131, 21))
        self.valLineEdit_5 = QLineEdit(Stove3)
        self.valLineEdit_5.setObjectName(u"valLineEdit_5")
        self.valLineEdit_5.setGeometry(QRect(210, 320, 131, 21))
        self.label_9 = QLabel(Stove3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(410, 50, 81, 20))
        self.label_10 = QLabel(Stove3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(600, 50, 81, 20))
        self.hexOmitLineEdit_1 = QLineEdit(Stove3)
        self.hexOmitLineEdit_1.setObjectName(u"hexOmitLineEdit_1")
        self.hexOmitLineEdit_1.setGeometry(QRect(380, 80, 131, 21))
        self.hexOmitLineEdit_1.setReadOnly(True)
        self.hexLineEdit_1 = QLineEdit(Stove3)
        self.hexLineEdit_1.setObjectName(u"hexLineEdit_1")
        self.hexLineEdit_1.setGeometry(QRect(550, 80, 151, 21))
        self.hexLineEdit_1.setReadOnly(True)
        self.hexLineEdit_2 = QLineEdit(Stove3)
        self.hexLineEdit_2.setObjectName(u"hexLineEdit_2")
        self.hexLineEdit_2.setGeometry(QRect(550, 120, 151, 21))
        self.hexLineEdit_2.setReadOnly(True)
        self.hexOmitLineEdit_2 = QLineEdit(Stove3)
        self.hexOmitLineEdit_2.setObjectName(u"hexOmitLineEdit_2")
        self.hexOmitLineEdit_2.setGeometry(QRect(380, 120, 131, 21))
        self.hexOmitLineEdit_2.setReadOnly(True)
        self.hexLineEdit_3 = QLineEdit(Stove3)
        self.hexLineEdit_3.setObjectName(u"hexLineEdit_3")
        self.hexLineEdit_3.setGeometry(QRect(550, 160, 151, 21))
        self.hexLineEdit_3.setReadOnly(True)
        self.hexOmitLineEdit_3 = QLineEdit(Stove3)
        self.hexOmitLineEdit_3.setObjectName(u"hexOmitLineEdit_3")
        self.hexOmitLineEdit_3.setGeometry(QRect(380, 160, 131, 21))
        self.hexOmitLineEdit_3.setReadOnly(True)
        self.hexLineEdit_4 = QLineEdit(Stove3)
        self.hexLineEdit_4.setObjectName(u"hexLineEdit_4")
        self.hexLineEdit_4.setGeometry(QRect(550, 200, 151, 21))
        self.hexLineEdit_4.setReadOnly(True)
        self.hexOmitLineEdit_4 = QLineEdit(Stove3)
        self.hexOmitLineEdit_4.setObjectName(u"hexOmitLineEdit_4")
        self.hexOmitLineEdit_4.setGeometry(QRect(380, 200, 131, 21))
        self.hexOmitLineEdit_4.setReadOnly(True)
        self.hexLineEdit_5 = QLineEdit(Stove3)
        self.hexLineEdit_5.setObjectName(u"hexLineEdit_5")
        self.hexLineEdit_5.setGeometry(QRect(550, 240, 151, 21))
        self.hexLineEdit_5.setReadOnly(True)
        self.hexOmitLineEdit_5 = QLineEdit(Stove3)
        self.hexOmitLineEdit_5.setObjectName(u"hexOmitLineEdit_5")
        self.hexOmitLineEdit_5.setGeometry(QRect(380, 240, 131, 21))
        self.hexOmitLineEdit_5.setReadOnly(True)
        self.hexLineEdit_6 = QLineEdit(Stove3)
        self.hexLineEdit_6.setObjectName(u"hexLineEdit_6")
        self.hexLineEdit_6.setGeometry(QRect(550, 280, 151, 21))
        self.hexLineEdit_6.setReadOnly(True)
        self.hexOmitLineEdit_6 = QLineEdit(Stove3)
        self.hexOmitLineEdit_6.setObjectName(u"hexOmitLineEdit_6")
        self.hexOmitLineEdit_6.setGeometry(QRect(380, 280, 131, 21))
        self.hexOmitLineEdit_6.setReadOnly(True)
        self.hexLineEdit_7 = QLineEdit(Stove3)
        self.hexLineEdit_7.setObjectName(u"hexLineEdit_7")
        self.hexLineEdit_7.setGeometry(QRect(550, 320, 151, 21))
        self.hexLineEdit_7.setReadOnly(True)
        self.hexOmitLineEdit_7 = QLineEdit(Stove3)
        self.hexOmitLineEdit_7.setObjectName(u"hexOmitLineEdit_7")
        self.hexOmitLineEdit_7.setGeometry(QRect(380, 320, 131, 21))
        self.hexOmitLineEdit_7.setReadOnly(True)
        self.label_11 = QLabel(Stove3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 570, 54, 16))
        self.actionIDLineEdit = QLineEdit(Stove3)
        self.actionIDLineEdit.setObjectName(u"actionIDLineEdit")
        self.actionIDLineEdit.setGeometry(QRect(100, 570, 111, 21))
        self.actionIDLineEdit.setReadOnly(True)
        self.generateIDPushButton = QPushButton(Stove3)
        self.generateIDPushButton.setObjectName(u"generateIDPushButton")
        self.generateIDPushButton.setGeometry(QRect(230, 570, 75, 24))
        self.commitPushButton = QPushButton(Stove3)
        self.commitPushButton.setObjectName(u"commitPushButton")
        self.commitPushButton.setGeometry(QRect(520, 610, 75, 24))
        self.cancelPushButton = QPushButton(Stove3)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(630, 610, 75, 24))
        self.groupBox = QGroupBox(Stove3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 350, 211, 201))
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 30, 31, 16))
        self.pLineEdit_1 = QLineEdit(self.groupBox)
        self.pLineEdit_1.setObjectName(u"pLineEdit_1")
        self.pLineEdit_1.setGeometry(QRect(60, 30, 113, 21))
        self.pLineEdit_1.setReadOnly(True)
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 60, 31, 16))
        self.iLineEdit_1 = QLineEdit(self.groupBox)
        self.iLineEdit_1.setObjectName(u"iLineEdit_1")
        self.iLineEdit_1.setGeometry(QRect(60, 60, 113, 21))
        self.iLineEdit_1.setReadOnly(True)
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 90, 31, 16))
        self.z1LineEdit_1 = QLineEdit(self.groupBox)
        self.z1LineEdit_1.setObjectName(u"z1LineEdit_1")
        self.z1LineEdit_1.setGeometry(QRect(60, 90, 113, 21))
        self.z1LineEdit_1.setReadOnly(True)
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 120, 31, 16))
        self.z2LineEdit_1 = QLineEdit(self.groupBox)
        self.z2LineEdit_1.setObjectName(u"z2LineEdit_1")
        self.z2LineEdit_1.setGeometry(QRect(60, 120, 113, 21))
        self.z2LineEdit_1.setReadOnly(True)
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 160, 51, 16))
        self.typeComboBox_1 = QComboBox(self.groupBox)
        self.typeComboBox_1.addItem("")
        self.typeComboBox_1.addItem("")
        self.typeComboBox_1.setObjectName(u"typeComboBox_1")
        self.typeComboBox_1.setGeometry(QRect(80, 160, 101, 22))
        self.groupBox_2 = QGroupBox(Stove3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(300, 350, 211, 201))
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 30, 31, 16))
        self.pLineEdit_2 = QLineEdit(self.groupBox_2)
        self.pLineEdit_2.setObjectName(u"pLineEdit_2")
        self.pLineEdit_2.setGeometry(QRect(60, 30, 113, 21))
        self.pLineEdit_2.setReadOnly(True)
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 60, 31, 16))
        self.iLineEdit_2 = QLineEdit(self.groupBox_2)
        self.iLineEdit_2.setObjectName(u"iLineEdit_2")
        self.iLineEdit_2.setGeometry(QRect(60, 60, 113, 21))
        self.iLineEdit_2.setReadOnly(True)
        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 90, 31, 16))
        self.z1LineEdit_2 = QLineEdit(self.groupBox_2)
        self.z1LineEdit_2.setObjectName(u"z1LineEdit_2")
        self.z1LineEdit_2.setGeometry(QRect(60, 90, 113, 21))
        self.z1LineEdit_2.setReadOnly(True)
        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 120, 31, 16))
        self.z2LineEdit_2 = QLineEdit(self.groupBox_2)
        self.z2LineEdit_2.setObjectName(u"z2LineEdit_2")
        self.z2LineEdit_2.setGeometry(QRect(60, 120, 113, 21))
        self.z2LineEdit_2.setReadOnly(True)
        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 160, 51, 16))
        self.typeComboBox_2 = QComboBox(self.groupBox_2)
        self.typeComboBox_2.addItem("")
        self.typeComboBox_2.addItem("")
        self.typeComboBox_2.setObjectName(u"typeComboBox_2")
        self.typeComboBox_2.setGeometry(QRect(80, 160, 101, 22))
        self.groupBox_3 = QGroupBox(Stove3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(550, 350, 211, 201))
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 30, 31, 16))
        self.pLineEdit_3 = QLineEdit(self.groupBox_3)
        self.pLineEdit_3.setObjectName(u"pLineEdit_3")
        self.pLineEdit_3.setGeometry(QRect(60, 30, 113, 21))
        self.pLineEdit_3.setReadOnly(True)
        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 60, 31, 16))
        self.iLineEdit_3 = QLineEdit(self.groupBox_3)
        self.iLineEdit_3.setObjectName(u"iLineEdit_3")
        self.iLineEdit_3.setGeometry(QRect(60, 60, 113, 21))
        self.iLineEdit_3.setReadOnly(True)
        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 90, 31, 16))
        self.z1LineEdit_3 = QLineEdit(self.groupBox_3)
        self.z1LineEdit_3.setObjectName(u"z1LineEdit_3")
        self.z1LineEdit_3.setGeometry(QRect(60, 90, 113, 21))
        self.z1LineEdit_3.setReadOnly(True)
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 120, 31, 16))
        self.z2LineEdit_3 = QLineEdit(self.groupBox_3)
        self.z2LineEdit_3.setObjectName(u"z2LineEdit_3")
        self.z2LineEdit_3.setGeometry(QRect(60, 120, 113, 21))
        self.z2LineEdit_3.setReadOnly(True)
        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 160, 51, 16))
        self.typeComboBox_3 = QComboBox(self.groupBox_3)
        self.typeComboBox_3.addItem("")
        self.typeComboBox_3.addItem("")
        self.typeComboBox_3.setObjectName(u"typeComboBox_3")
        self.typeComboBox_3.setGeometry(QRect(80, 160, 101, 22))

        self.retranslateUi(Stove3)

        QMetaObject.connectSlotsByName(Stove3)
    # setupUi

    def retranslateUi(self, Stove3):
        Stove3.setWindowTitle(QCoreApplication.translate("Stove3", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Stove3", u"4\u7089\u4e0a\u673a3\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Stove3", u"\u7089\u4e0a\u673a3\u8fd0\u884c\u65b9\u5f0f\u8bbe\u7f6e", None))
        self.runModeComboBox.setItemText(0, QCoreApplication.translate("Stove3", u"\u5f00\u73af", None))
        self.runModeComboBox.setItemText(1, QCoreApplication.translate("Stove3", u"\u9650\u4f4d\u5f00\u5173", None))
        self.runModeComboBox.setItemText(2, QCoreApplication.translate("Stove3", u"\u7f16\u7801\u5668", None))

        self.label_3.setText(QCoreApplication.translate("Stove3", u"\u7089\u4e0a\u673a3\u8fd0\u884c\u5f00\u73af\u8bbe\u7f6e\u503c", None))
        self.valLineEdit_1.setText(QCoreApplication.translate("Stove3", u"10", None))
        self.label_4.setText(QCoreApplication.translate("Stove3", u"\u7089\u4e0a\u673a3\u8fd0\u884c\u7f16\u7801\u5668\u8bbe\u7f6e\u503c", None))
        self.valLineEdit_2.setText(QCoreApplication.translate("Stove3", u"1", None))
        self.valLineEdit_3.setText(QCoreApplication.translate("Stove3", u"1", None))
        self.label_5.setText(QCoreApplication.translate("Stove3", u"\u7089\u4e0a\u673a3\u8109\u51b2\u8f93\u51fa\u9608\u503c", None))
        self.valLineEdit_4.setText(QCoreApplication.translate("Stove3", u"1", None))
        self.label_6.setText(QCoreApplication.translate("Stove3", u"\u7089\u4e0a\u673a3\u7eed\u8f6c\u6b65\u6570", None))
        self.label_7.setText(QCoreApplication.translate("Stove3", u"\u9650\u4f4d\u5f00\u5173\u8bbe\u7f6e\u503c", None))
        self.switchValComboBox.setItemText(0, QCoreApplication.translate("Stove3", u"\u63d0\u673a2\u4e0a\u9650", None))
        self.switchValComboBox.setItemText(1, QCoreApplication.translate("Stove3", u"\u63d0\u673a2\u4e0b\u9650", None))
        self.switchValComboBox.setItemText(2, QCoreApplication.translate("Stove3", u"\u8f6c\u673a1\u96f6", None))
        self.switchValComboBox.setItemText(3, QCoreApplication.translate("Stove3", u"\u8f6c\u673a1\u8ba1", None))
        self.switchValComboBox.setItemText(4, QCoreApplication.translate("Stove3", u"5\u53f7", None))
        self.switchValComboBox.setItemText(5, QCoreApplication.translate("Stove3", u"6\u53f7", None))
        self.switchValComboBox.setItemText(6, QCoreApplication.translate("Stove3", u"\u7089\u4e0a\u673a3\u4e0a\u9650", None))
        self.switchValComboBox.setItemText(7, QCoreApplication.translate("Stove3", u"\u7089\u4e0a\u673a3\u4e0b\u9650", None))
        self.switchValComboBox.setItemText(8, QCoreApplication.translate("Stove3", u"\u7089\u4e0b\u673a5\u4e0a\u9650", None))
        self.switchValComboBox.setItemText(9, QCoreApplication.translate("Stove3", u"\u7089\u4e0b\u673a5\u4e0b\u9650", None))
        self.switchValComboBox.setItemText(10, QCoreApplication.translate("Stove3", u"\u4e0d\u4f7f\u7528", None))

        self.label_8.setText(QCoreApplication.translate("Stove3", u"\u5931\u6b65\u9608\u503c", None))
        self.valLineEdit_5.setText(QCoreApplication.translate("Stove3", u"10", None))
        self.label_9.setText(QCoreApplication.translate("Stove3", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_10.setText(QCoreApplication.translate("Stove3", u"\u5341\u516d\u8fdb\u5236", None))
        self.hexOmitLineEdit_1.setText("")
        self.hexLineEdit_1.setText("")
        self.hexLineEdit_2.setText("")
        self.hexOmitLineEdit_2.setText("")
        self.hexLineEdit_3.setText("")
        self.hexOmitLineEdit_3.setText("")
        self.hexLineEdit_4.setText("")
        self.hexOmitLineEdit_4.setText("")
        self.hexLineEdit_5.setText("")
        self.hexOmitLineEdit_5.setText("")
        self.hexLineEdit_6.setText("")
        self.hexOmitLineEdit_6.setText("")
        self.hexLineEdit_7.setText("")
        self.hexOmitLineEdit_7.setText("")
        self.label_11.setText(QCoreApplication.translate("Stove3", u"\u52a8\u4f5cID", None))
        self.actionIDLineEdit.setText("")
        self.generateIDPushButton.setText(QCoreApplication.translate("Stove3", u"\u751f\u6210\u52a8\u4f5cID", None))
        self.commitPushButton.setText(QCoreApplication.translate("Stove3", u"\u786e\u5b9a", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Stove3", u"\u53d6\u6d88", None))
        self.groupBox.setTitle(QCoreApplication.translate("Stove3", u"\u5f00\u73af\u53c2\u6570", None))
        self.label_12.setText(QCoreApplication.translate("Stove3", u"P", None))
        self.label_13.setText(QCoreApplication.translate("Stove3", u"i", None))
        self.label_14.setText(QCoreApplication.translate("Stove3", u"z1", None))
        self.label_15.setText(QCoreApplication.translate("Stove3", u"z2", None))
        self.label_16.setText(QCoreApplication.translate("Stove3", u"\u8fd0\u52a8\u7c7b\u522b", None))
        self.typeComboBox_1.setItemText(0, QCoreApplication.translate("Stove3", u"\u76f4\u7ebf\u8fd0\u52a8", None))
        self.typeComboBox_1.setItemText(1, QCoreApplication.translate("Stove3", u"\u5706\u5468\u8fd0\u52a8", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("Stove3", u"\u975e\u5f00\u73af\u53c2\u6570", None))
        self.label_17.setText(QCoreApplication.translate("Stove3", u"P", None))
        self.label_18.setText(QCoreApplication.translate("Stove3", u"i", None))
        self.label_19.setText(QCoreApplication.translate("Stove3", u"z1", None))
        self.label_20.setText(QCoreApplication.translate("Stove3", u"z2", None))
        self.label_21.setText(QCoreApplication.translate("Stove3", u"\u8fd0\u52a8\u7c7b\u522b", None))
        self.typeComboBox_2.setItemText(0, QCoreApplication.translate("Stove3", u"\u76f4\u7ebf\u8fd0\u52a8", None))
        self.typeComboBox_2.setItemText(1, QCoreApplication.translate("Stove3", u"\u5706\u5468\u8fd0\u52a8", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("Stove3", u"\u9650\u4f4d\u5f00\u5173\u6709\u6548\u53c2\u6570", None))
        self.label_22.setText(QCoreApplication.translate("Stove3", u"P", None))
        self.label_23.setText(QCoreApplication.translate("Stove3", u"i", None))
        self.label_24.setText(QCoreApplication.translate("Stove3", u"z1", None))
        self.label_25.setText(QCoreApplication.translate("Stove3", u"z2", None))
        self.label_26.setText(QCoreApplication.translate("Stove3", u"\u8fd0\u52a8\u7c7b\u522b", None))
        self.typeComboBox_3.setItemText(0, QCoreApplication.translate("Stove3", u"\u76f4\u7ebf\u8fd0\u52a8", None))
        self.typeComboBox_3.setItemText(1, QCoreApplication.translate("Stove3", u"\u5706\u5468\u8fd0\u52a8", None))

    # retranslateUi

