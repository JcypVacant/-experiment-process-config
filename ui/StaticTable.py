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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_StaticTable(object):
    def setupUi(self, StaticTable):
        if not StaticTable.objectName():
            StaticTable.setObjectName(u"StaticTable")
        StaticTable.resize(363, 231)
        self.buttonBox = QDialogButtonBox(StaticTable)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setStandardButtons(QDialogButtonBox.NoButton)
        self.layoutWidget = QWidget(StaticTable)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 50, 193, 81))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layoutWidget1 = QWidget(StaticTable)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(160, 180, 158, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.retranslateUi(StaticTable)
        self.buttonBox.accepted.connect(StaticTable.accept)
        self.buttonBox.rejected.connect(StaticTable.reject)

        QMetaObject.connectSlotsByName(StaticTable)
    # setupUi

    def retranslateUi(self, StaticTable):
        StaticTable.setWindowTitle(QCoreApplication.translate("StaticTable", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("StaticTable", u"\u8ba1\u7b97\u6bcf\u7c7b\u7684\u52a8\u4f5c\u6570\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("StaticTable", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("StaticTable", u"\u8ba1\u7b97\u6d41\u7a0b\u8868\u6570\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("StaticTable", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.pushButton_3.setText(QCoreApplication.translate("StaticTable", u"\u786e\u5b9a", None))
        self.pushButton_4.setText(QCoreApplication.translate("StaticTable", u"\u53d6\u6d88", None))
    # retranslateUi

