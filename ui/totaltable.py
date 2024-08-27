# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'totaltable.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_TotalTable(object):
    def setupUi(self, TotalTable):
        if not TotalTable.objectName():
            TotalTable.setObjectName(u"TotalTable")
        TotalTable.resize(598, 375)
        self.totalTable_lineEdit = QLineEdit(TotalTable)
        self.totalTable_lineEdit.setObjectName(u"totalTable_lineEdit")
        self.totalTable_lineEdit.setGeometry(QRect(100, 210, 132, 20))
        self.label_7 = QLabel(TotalTable)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 40, 71, 21))
        self.layoutWidget2 = QWidget(TotalTable)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(21, 120, 212, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.actionTable_lineEdit = QLineEdit(self.layoutWidget2)
        self.actionTable_lineEdit.setObjectName(u"actionTable_lineEdit")

        self.horizontalLayout_3.addWidget(self.actionTable_lineEdit)

        self.layoutWidget3 = QWidget(TotalTable)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(21, 150, 212, 22))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.dynamicTable_lineEdit = QLineEdit(self.layoutWidget3)
        self.dynamicTable_lineEdit.setObjectName(u"dynamicTable_lineEdit")

        self.horizontalLayout_4.addWidget(self.dynamicTable_lineEdit)

        self.layoutWidget4 = QWidget(TotalTable)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(21, 180, 212, 22))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.monitoringTable_lineEdit = QLineEdit(self.layoutWidget4)
        self.monitoringTable_lineEdit.setObjectName(u"monitoringTable_lineEdit")

        self.horizontalLayout_5.addWidget(self.monitoringTable_lineEdit)

        self.label_6 = QLabel(TotalTable)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(22, 216, 60, 16))
        self.layoutWidget5 = QWidget(TotalTable)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(21, 90, 212, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.staticTable_lineEdit = QLineEdit(self.layoutWidget5)
        self.staticTable_lineEdit.setObjectName(u"staticTable_lineEdit")

        self.horizontalLayout_2.addWidget(self.staticTable_lineEdit)

        self.layoutWidget6 = QWidget(TotalTable)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(260, 80, 221, 161))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_7 = QLineEdit(self.layoutWidget6)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_2.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.layoutWidget6)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_2.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.layoutWidget6)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_2.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(self.layoutWidget6)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_2.addWidget(self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.layoutWidget6)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_2.addWidget(self.lineEdit_11)

        self.layoutWidget7 = QWidget(TotalTable)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(500, 80, 82, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.totalStatic_pushButton = QPushButton(self.layoutWidget7)
        self.totalStatic_pushButton.setObjectName(u"totalStatic_pushButton")

        self.verticalLayout.addWidget(self.totalStatic_pushButton)

        self.totalAction_pushButton = QPushButton(self.layoutWidget7)
        self.totalAction_pushButton.setObjectName(u"totalAction_pushButton")

        self.verticalLayout.addWidget(self.totalAction_pushButton)

        self.totalDynamic_pushButton = QPushButton(self.layoutWidget7)
        self.totalDynamic_pushButton.setObjectName(u"totalDynamic_pushButton")

        self.verticalLayout.addWidget(self.totalDynamic_pushButton)

        self.totalMonitoring_pushButton = QPushButton(self.layoutWidget7)
        self.totalMonitoring_pushButton.setObjectName(u"totalMonitoring_pushButton")

        self.verticalLayout.addWidget(self.totalMonitoring_pushButton)

        self.total_pushButton = QPushButton(self.layoutWidget7)
        self.total_pushButton.setObjectName(u"total_pushButton")

        self.verticalLayout.addWidget(self.total_pushButton)

        self.layoutWidget8 = QWidget(TotalTable)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(130, 290, 267, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tableHead_pushButton = QPushButton(self.layoutWidget8)
        self.tableHead_pushButton.setObjectName(u"tableHead_pushButton")

        self.horizontalLayout_6.addWidget(self.tableHead_pushButton)

        self.totalTable_pushButton = QPushButton(self.layoutWidget8)
        self.totalTable_pushButton.setObjectName(u"totalTable_pushButton")

        self.horizontalLayout_6.addWidget(self.totalTable_pushButton)

        self.head_total_pushButton = QPushButton(self.layoutWidget8)
        self.head_total_pushButton.setObjectName(u"head_total_pushButton")

        self.horizontalLayout_6.addWidget(self.head_total_pushButton)

        self.label_8 = QLabel(TotalTable)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 40, 71, 21))

        self.retranslateUi(TotalTable)

        QMetaObject.connectSlotsByName(TotalTable)
    # setupUi

    def retranslateUi(self, TotalTable):
        TotalTable.setWindowTitle(QCoreApplication.translate("TotalTable", u"Dialog", None))
        self.label_7.setText(QCoreApplication.translate("TotalTable", u"\u5341\u516d\u8fdb\u5236\u503c", None))
        self.label_3.setText(QCoreApplication.translate("TotalTable", u"\u52a8\u4f5c\u8868\u957f\u5ea6\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("TotalTable", u"\u52a8\u6001\u8868\u957f\u5ea6\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("TotalTable", u"\u76d1\u63a7\u8868\u957f\u5ea6\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("TotalTable", u"\u603b\u8868\u957f\u5ea6\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("TotalTable", u"\u9759\u6001\u8868\u957f\u5ea6\uff1a", None))
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.totalStatic_pushButton.setText(QCoreApplication.translate("TotalTable", u"\u83b7\u53d6\u9759\u6001\u8868", None))
        self.totalAction_pushButton.setText(QCoreApplication.translate("TotalTable", u"\u83b7\u53d6\u603b\u52a8\u4f5c\u8868", None))
        self.totalDynamic_pushButton.setText(QCoreApplication.translate("TotalTable", u"\u83b7\u53d6\u603b\u52a8\u6001\u8868", None))
        self.totalMonitoring_pushButton.setText(QCoreApplication.translate("TotalTable", u"\u83b7\u53d6\u603b\u76d1\u63a7\u8868", None))
        self.total_pushButton.setText(QCoreApplication.translate("TotalTable", u"\u83b7\u53d6\u603b\u8868", None))
        self.tableHead_pushButton.setText(QCoreApplication.translate("TotalTable", u"\u751f\u6210\u8868\u5934", None))
        self.totalTable_pushButton.setText(QCoreApplication.translate("TotalTable", u"\u751f\u6210\u603b\u8868", None))
        self.head_total_pushButton.setText(QCoreApplication.translate("TotalTable", u"\u8868\u5934+3\u603b\u8868", None))
        self.label_8.setText(QCoreApplication.translate("TotalTable", u"\u957f\u5ea6", None))
    # retranslateUi

