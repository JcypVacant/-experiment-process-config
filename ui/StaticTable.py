# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statictable.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_StaticTable(object):
    def setupUi(self, StaticTable):
        if not StaticTable.objectName():
            StaticTable.setObjectName(u"StaticTable")
        StaticTable.resize(363, 231)
        self.buttonBox = QDialogButtonBox(StaticTable)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setStandardButtons(QDialogButtonBox.NoButton)
        self.lineEdit = QLineEdit(StaticTable)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 80, 81, 20))
        self.lineEdit.setMaxLength(32767)
        self.pushButton_3 = QPushButton(StaticTable)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(250, 190, 75, 24))
        self.layoutWidget = QWidget(StaticTable)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(29, 36, 191, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(StaticTable)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 80, 75, 24))
        self.label_2 = QLabel(StaticTable)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(31, 81, 84, 16))

        self.retranslateUi(StaticTable)
        self.buttonBox.accepted.connect(StaticTable.accept)
        self.buttonBox.rejected.connect(StaticTable.reject)

        QMetaObject.connectSlotsByName(StaticTable)
    # setupUi

    def retranslateUi(self, StaticTable):
        StaticTable.setWindowTitle(QCoreApplication.translate("StaticTable", u"Dialog", None))
        self.pushButton_3.setText(QCoreApplication.translate("StaticTable", u"\u751f\u6210\u9759\u6001\u8868", None))
        self.label.setText(QCoreApplication.translate("StaticTable", u"\u8ba1\u7b97\u6bcf\u7c7b\u7684\u52a8\u4f5c\u6570\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("StaticTable", u"\u70b9\u51fb\u83b7\u53d6", None))
        self.pushButton.setText(QCoreApplication.translate("StaticTable", u"\u70b9\u51fb\u83b7\u53d6", None))
        self.label_2.setText(QCoreApplication.translate("StaticTable", u"\u83b7\u53d6\u6d41\u7a0b\u8868\u6570\uff1a", None))
    # retranslateUi

