# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dynamictable.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_DynamicTable(object):
    def setupUi(self, DynamicTable):
        if not DynamicTable.objectName():
            DynamicTable.setObjectName(u"DynamicTable")
        DynamicTable.resize(269, 219)
        self.dynamic_pushButton = QPushButton(DynamicTable)
        self.dynamic_pushButton.setObjectName(u"dynamic_pushButton")
        self.dynamic_pushButton.setGeometry(QRect(150, 170, 75, 24))
        self.dynamic_lineEdit = QLineEdit(DynamicTable)
        self.dynamic_lineEdit.setObjectName(u"dynamic_lineEdit")
        self.dynamic_lineEdit.setGeometry(QRect(120, 80, 91, 20))
        self.label = QLabel(DynamicTable)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 80, 81, 21))
        self.label_2 = QLabel(DynamicTable)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 10, 111, 21))

        self.retranslateUi(DynamicTable)

        QMetaObject.connectSlotsByName(DynamicTable)
    # setupUi

    def retranslateUi(self, DynamicTable):
        DynamicTable.setWindowTitle(QCoreApplication.translate("DynamicTable", u"Dialog", None))
        self.dynamic_pushButton.setText(QCoreApplication.translate("DynamicTable", u"\u786e\u5b9a", None))
        self.label.setText(QCoreApplication.translate("DynamicTable", u"\u52a8\u6001\u914d\u7f6e\u5e8f\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("DynamicTable", u"\u8f93\u5165\u52a8\u6001\u8868\u914d\u7f6e\u5e8f\u53f7", None))
    # retranslateUi

