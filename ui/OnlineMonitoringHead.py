# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'onlinemonitoringhead.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_OnlineMonitoringHead(object):
    def setupUi(self, OnlineMonitoringHead):
        if not OnlineMonitoringHead.objectName():
            OnlineMonitoringHead.setObjectName(u"OnlineMonitoringHead")
        OnlineMonitoringHead.resize(727, 301)
        self.label = QLabel(OnlineMonitoringHead)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 10, 111, 16))
        self.label_2 = QLabel(OnlineMonitoringHead)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 131, 16))
        self.valLineEdit_1 = QLineEdit(OnlineMonitoringHead)
        self.valLineEdit_1.setObjectName(u"valLineEdit_1")
        self.valLineEdit_1.setGeometry(QRect(190, 80, 151, 21))
        self.label_3 = QLabel(OnlineMonitoringHead)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 120, 131, 16))
        self.valLineEdit_2 = QLineEdit(OnlineMonitoringHead)
        self.valLineEdit_2.setObjectName(u"valLineEdit_2")
        self.valLineEdit_2.setGeometry(QRect(190, 120, 151, 21))
        self.label_4 = QLabel(OnlineMonitoringHead)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 181, 20))
        self.valLineEdit_3 = QLineEdit(OnlineMonitoringHead)
        self.valLineEdit_3.setObjectName(u"valLineEdit_3")
        self.valLineEdit_3.setGeometry(QRect(190, 160, 151, 21))
        self.label_5 = QLabel(OnlineMonitoringHead)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 195, 171, 21))
        self.valLineEdit_4 = QLineEdit(OnlineMonitoringHead)
        self.valLineEdit_4.setObjectName(u"valLineEdit_4")
        self.valLineEdit_4.setGeometry(QRect(190, 200, 151, 21))
        self.label_6 = QLabel(OnlineMonitoringHead)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(420, 50, 81, 16))
        self.label_7 = QLabel(OnlineMonitoringHead)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(570, 50, 51, 16))
        self.hexOmitLineEdit_1 = QLineEdit(OnlineMonitoringHead)
        self.hexOmitLineEdit_1.setObjectName(u"hexOmitLineEdit_1")
        self.hexOmitLineEdit_1.setGeometry(QRect(400, 80, 113, 21))
        self.hexOmitLineEdit_1.setReadOnly(True)
        self.hexLineEdit_1 = QLineEdit(OnlineMonitoringHead)
        self.hexLineEdit_1.setObjectName(u"hexLineEdit_1")
        self.hexLineEdit_1.setGeometry(QRect(540, 80, 131, 21))
        self.hexLineEdit_1.setReadOnly(True)
        self.hexLineEdit_2 = QLineEdit(OnlineMonitoringHead)
        self.hexLineEdit_2.setObjectName(u"hexLineEdit_2")
        self.hexLineEdit_2.setGeometry(QRect(540, 120, 131, 21))
        self.hexLineEdit_2.setReadOnly(True)
        self.hexOmitLineEdit_2 = QLineEdit(OnlineMonitoringHead)
        self.hexOmitLineEdit_2.setObjectName(u"hexOmitLineEdit_2")
        self.hexOmitLineEdit_2.setGeometry(QRect(400, 120, 113, 21))
        self.hexOmitLineEdit_2.setReadOnly(True)
        self.hexLineEdit_3 = QLineEdit(OnlineMonitoringHead)
        self.hexLineEdit_3.setObjectName(u"hexLineEdit_3")
        self.hexLineEdit_3.setGeometry(QRect(540, 160, 131, 21))
        self.hexLineEdit_3.setReadOnly(True)
        self.hexOmitLineEdit_3 = QLineEdit(OnlineMonitoringHead)
        self.hexOmitLineEdit_3.setObjectName(u"hexOmitLineEdit_3")
        self.hexOmitLineEdit_3.setGeometry(QRect(400, 160, 113, 21))
        self.hexOmitLineEdit_3.setReadOnly(True)
        self.hexLineEdit_4 = QLineEdit(OnlineMonitoringHead)
        self.hexLineEdit_4.setObjectName(u"hexLineEdit_4")
        self.hexLineEdit_4.setGeometry(QRect(540, 200, 131, 21))
        self.hexLineEdit_4.setReadOnly(True)
        self.hexOmitLineEdit_4 = QLineEdit(OnlineMonitoringHead)
        self.hexOmitLineEdit_4.setObjectName(u"hexOmitLineEdit_4")
        self.hexOmitLineEdit_4.setGeometry(QRect(400, 200, 113, 21))
        self.hexOmitLineEdit_4.setReadOnly(True)
        self.label_8 = QLabel(OnlineMonitoringHead)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 240, 54, 16))
        self.actionIDLineEdit = QLineEdit(OnlineMonitoringHead)
        self.actionIDLineEdit.setObjectName(u"actionIDLineEdit")
        self.actionIDLineEdit.setGeometry(QRect(120, 240, 121, 21))
        self.generateIDPushButton = QPushButton(OnlineMonitoringHead)
        self.generateIDPushButton.setObjectName(u"generateIDPushButton")
        self.generateIDPushButton.setGeometry(QRect(260, 240, 75, 24))
        self.commitPushButton = QPushButton(OnlineMonitoringHead)
        self.commitPushButton.setObjectName(u"commitPushButton")
        self.commitPushButton.setGeometry(QRect(420, 260, 75, 24))
        self.cancelPushButton = QPushButton(OnlineMonitoringHead)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(570, 260, 75, 24))

        self.retranslateUi(OnlineMonitoringHead)

        QMetaObject.connectSlotsByName(OnlineMonitoringHead)
    # setupUi

    def retranslateUi(self, OnlineMonitoringHead):
        OnlineMonitoringHead.setWindowTitle(QCoreApplication.translate("OnlineMonitoringHead", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("OnlineMonitoringHead", u"E\u5728\u7ebf\u76d1\u63a7\u8868\u5934\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("OnlineMonitoringHead", u"\u5728\u7ebf\u76d1\u63a7\u7981\u6b62\u8bbe\u7f6e\u5e8f\u53f7", None))
        self.valLineEdit_1.setText(QCoreApplication.translate("OnlineMonitoringHead", u"00FF", None))
        self.label_3.setText(QCoreApplication.translate("OnlineMonitoringHead", u"\u5728\u7ebf\u76d1\u63a7\u4f7f\u80fd\u8bbe\u7f6e\u5e8f\u53f7", None))
        self.valLineEdit_2.setText(QCoreApplication.translate("OnlineMonitoringHead", u"00FF", None))
        self.label_4.setText(QCoreApplication.translate("OnlineMonitoringHead", u"\u9700\u4fee\u6539\u52a8\u4f5c\u6307\u9488\u7684\u52a8\u6001\u76d1\u63a7\u8868\u53f7", None))
        self.valLineEdit_3.setText(QCoreApplication.translate("OnlineMonitoringHead", u"00", None))
        self.label_5.setText(QCoreApplication.translate("OnlineMonitoringHead", u"\u8bbe\u7f6e\u5728\u7ebf\u76d1\u63a7\u52a8\u6001\u8868\u7684\u52a8\u4f5c\u6307\u9488", None))
        self.valLineEdit_4.setText(QCoreApplication.translate("OnlineMonitoringHead", u"00", None))
        self.label_6.setText(QCoreApplication.translate("OnlineMonitoringHead", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_7.setText(QCoreApplication.translate("OnlineMonitoringHead", u"\u5341\u516d\u8fdb\u5236", None))
        self.label_8.setText(QCoreApplication.translate("OnlineMonitoringHead", u"\u52a8\u4f5cID", None))
        self.generateIDPushButton.setText(QCoreApplication.translate("OnlineMonitoringHead", u"\u751f\u6210\u52a8\u4f5cID", None))
        self.commitPushButton.setText(QCoreApplication.translate("OnlineMonitoringHead", u"\u786e\u5b9a", None))
        self.cancelPushButton.setText(QCoreApplication.translate("OnlineMonitoringHead", u"\u53d6\u6d88", None))
    # retranslateUi

