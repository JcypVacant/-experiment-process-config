# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'furnaceswitch.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_FurnaceSwitch(object):
    def setupUi(self, FurnaceSwitch):
        if not FurnaceSwitch.objectName():
            FurnaceSwitch.setObjectName(u"FurnaceSwitch")
        FurnaceSwitch.resize(1166, 664)
        self.label = QLabel(FurnaceSwitch)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(570, 10, 101, 31))
        self.layoutWidget = QWidget(FurnaceSwitch)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 530, 215, 26))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.generateIDPushButton = QPushButton(self.layoutWidget)
        self.generateIDPushButton.setObjectName(u"generateIDPushButton")

        self.horizontalLayout_13.addWidget(self.generateIDPushButton)

        self.actionIDLineEdit = QLineEdit(self.layoutWidget)
        self.actionIDLineEdit.setObjectName(u"actionIDLineEdit")
        self.actionIDLineEdit.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.actionIDLineEdit)

        self.layoutWidget1 = QWidget(FurnaceSwitch)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(70, 50, 1041, 457))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(50)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.LEDCheckBox = QCheckBox(self.layoutWidget1)
        self.LEDCheckBox.setObjectName(u"LEDCheckBox")

        self.horizontalLayout_7.addWidget(self.LEDCheckBox)

        self.CCDCheckBox = QCheckBox(self.layoutWidget1)
        self.CCDCheckBox.setObjectName(u"CCDCheckBox")

        self.horizontalLayout_7.addWidget(self.CCDCheckBox)

        self.valveCheckBox = QCheckBox(self.layoutWidget1)
        self.valveCheckBox.setObjectName(u"valveCheckBox")

        self.horizontalLayout_7.addWidget(self.valveCheckBox)

        self.accCheckBox = QCheckBox(self.layoutWidget1)
        self.accCheckBox.setObjectName(u"accCheckBox")

        self.horizontalLayout_7.addWidget(self.accCheckBox)

        self.sampleBoxCheckBox = QCheckBox(self.layoutWidget1)
        self.sampleBoxCheckBox.setObjectName(u"sampleBoxCheckBox")

        self.horizontalLayout_7.addWidget(self.sampleBoxCheckBox)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.hexOmitLineEdit_1 = QLineEdit(self.layoutWidget1)
        self.hexOmitLineEdit_1.setObjectName(u"hexOmitLineEdit_1")
        self.hexOmitLineEdit_1.setReadOnly(True)

        self.horizontalLayout.addWidget(self.hexOmitLineEdit_1)

        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.hexLineEdit_1 = QLineEdit(self.layoutWidget1)
        self.hexLineEdit_1.setObjectName(u"hexLineEdit_1")
        self.hexLineEdit_1.setReadOnly(True)

        self.horizontalLayout.addWidget(self.hexLineEdit_1)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.LEDComboBox = QComboBox(self.layoutWidget1)
        self.LEDComboBox.addItem("")
        self.LEDComboBox.addItem("")
        self.LEDComboBox.addItem("")
        self.LEDComboBox.addItem("")
        self.LEDComboBox.setObjectName(u"LEDComboBox")

        self.horizontalLayout_8.addWidget(self.LEDComboBox)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.hexOmitLineEdit_2 = QLineEdit(self.layoutWidget1)
        self.hexOmitLineEdit_2.setObjectName(u"hexOmitLineEdit_2")
        self.hexOmitLineEdit_2.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.hexOmitLineEdit_2)

        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.hexLineEdit_2 = QLineEdit(self.layoutWidget1)
        self.hexLineEdit_2.setObjectName(u"hexLineEdit_2")
        self.hexLineEdit_2.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.hexLineEdit_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.CCDComboBox = QComboBox(self.layoutWidget1)
        self.CCDComboBox.addItem("")
        self.CCDComboBox.addItem("")
        self.CCDComboBox.addItem("")
        self.CCDComboBox.addItem("")
        self.CCDComboBox.setObjectName(u"CCDComboBox")

        self.horizontalLayout_9.addWidget(self.CCDComboBox)


        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.hexOmitLineEdit_3 = QLineEdit(self.layoutWidget1)
        self.hexOmitLineEdit_3.setObjectName(u"hexOmitLineEdit_3")
        self.hexOmitLineEdit_3.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.hexOmitLineEdit_3)

        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.hexLineEdit_3 = QLineEdit(self.layoutWidget1)
        self.hexLineEdit_3.setObjectName(u"hexLineEdit_3")
        self.hexLineEdit_3.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.hexLineEdit_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.valveComboBox = QComboBox(self.layoutWidget1)
        self.valveComboBox.addItem("")
        self.valveComboBox.addItem("")
        self.valveComboBox.addItem("")
        self.valveComboBox.addItem("")
        self.valveComboBox.addItem("")
        self.valveComboBox.addItem("")
        self.valveComboBox.addItem("")
        self.valveComboBox.addItem("")
        self.valveComboBox.setObjectName(u"valveComboBox")

        self.horizontalLayout_10.addWidget(self.valveComboBox)


        self.gridLayout.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.hexOmitLineEdit_4 = QLineEdit(self.layoutWidget1)
        self.hexOmitLineEdit_4.setObjectName(u"hexOmitLineEdit_4")
        self.hexOmitLineEdit_4.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.hexOmitLineEdit_4)

        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.hexLineEdit_4 = QLineEdit(self.layoutWidget1)
        self.hexLineEdit_4.setObjectName(u"hexLineEdit_4")
        self.hexLineEdit_4.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.hexLineEdit_4)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.accComboBox = QComboBox(self.layoutWidget1)
        self.accComboBox.addItem("")
        self.accComboBox.addItem("")
        self.accComboBox.setObjectName(u"accComboBox")

        self.horizontalLayout_11.addWidget(self.accComboBox)


        self.gridLayout.addLayout(self.horizontalLayout_11, 4, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_5.addWidget(self.label_17)

        self.hexOmitLineEdit_5 = QLineEdit(self.layoutWidget1)
        self.hexOmitLineEdit_5.setObjectName(u"hexOmitLineEdit_5")
        self.hexOmitLineEdit_5.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.hexOmitLineEdit_5)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_5.addWidget(self.label_16)

        self.hexLineEdit_5 = QLineEdit(self.layoutWidget1)
        self.hexLineEdit_5.setObjectName(u"hexLineEdit_5")
        self.hexLineEdit_5.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.hexLineEdit_5)


        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.sampleBoxComboBox = QComboBox(self.layoutWidget1)
        self.sampleBoxComboBox.addItem("")
        self.sampleBoxComboBox.addItem("")
        self.sampleBoxComboBox.setObjectName(u"sampleBoxComboBox")

        self.horizontalLayout_12.addWidget(self.sampleBoxComboBox)


        self.gridLayout.addLayout(self.horizontalLayout_12, 5, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_19 = QLabel(self.layoutWidget1)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_6.addWidget(self.label_19)

        self.hexOmitLineEdit_6 = QLineEdit(self.layoutWidget1)
        self.hexOmitLineEdit_6.setObjectName(u"hexOmitLineEdit_6")
        self.hexOmitLineEdit_6.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.hexOmitLineEdit_6)

        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_6.addWidget(self.label_18)

        self.hexLineEdit_6 = QLineEdit(self.layoutWidget1)
        self.hexLineEdit_6.setObjectName(u"hexLineEdit_6")
        self.hexLineEdit_6.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.hexLineEdit_6)


        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 1, 1, 1)

        self.layoutWidget2 = QWidget(FurnaceSwitch)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(650, 570, 327, 26))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_14.setSpacing(50)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.commitPushButton = QPushButton(self.layoutWidget2)
        self.commitPushButton.setObjectName(u"commitPushButton")

        self.horizontalLayout_14.addWidget(self.commitPushButton)

        self.cancelPushButton = QPushButton(self.layoutWidget2)
        self.cancelPushButton.setObjectName(u"cancelPushButton")

        self.horizontalLayout_14.addWidget(self.cancelPushButton)


        self.retranslateUi(FurnaceSwitch)

        QMetaObject.connectSlotsByName(FurnaceSwitch)
    # setupUi

    def retranslateUi(self, FurnaceSwitch):
        FurnaceSwitch.setWindowTitle(QCoreApplication.translate("FurnaceSwitch", u"\u7089\u5b50\u5f00\u5173", None))
        self.label.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5f00\u5173\u91cf\u52a8\u4f5c\u8bbe\u7f6e", None))
        self.generateIDPushButton.setText(QCoreApplication.translate("FurnaceSwitch", u"\u751f\u6210\u52a8\u4f5cID", None))
        self.label_2.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5f00\u5173\u91cf\u7247\u9009\uff08LED-CCD-\u9600\uff09", None))
        self.LEDCheckBox.setText(QCoreApplication.translate("FurnaceSwitch", u"LED", None))
        self.CCDCheckBox.setText(QCoreApplication.translate("FurnaceSwitch", u"CCD", None))
        self.valveCheckBox.setText(QCoreApplication.translate("FurnaceSwitch", u"\u9600", None))
        self.accCheckBox.setText(QCoreApplication.translate("FurnaceSwitch", u"\u52a0\u901f\u5ea6", None))
        self.sampleBoxCheckBox.setText(QCoreApplication.translate("FurnaceSwitch", u"\u6837\u54c1\u76d2", None))
        self.label_8.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_9.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u503c", None))
        self.label_3.setText(QCoreApplication.translate("FurnaceSwitch", u"LED\u4f7f\u80fd\u8bbe\u7f6e\uff08LED1\u5f00~\u51732\u5f00~\u5173\uff09", None))
        self.LEDComboBox.setItemText(0, QCoreApplication.translate("FurnaceSwitch", u"LED1\u4f7f\u80fd", None))
        self.LEDComboBox.setItemText(1, QCoreApplication.translate("FurnaceSwitch", u"LED1\u5173", None))
        self.LEDComboBox.setItemText(2, QCoreApplication.translate("FurnaceSwitch", u"LED2\u4f7f\u80fd", None))
        self.LEDComboBox.setItemText(3, QCoreApplication.translate("FurnaceSwitch", u"LED2\u5173", None))

        self.label_11.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_10.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u503c", None))
        self.label_4.setText(QCoreApplication.translate("FurnaceSwitch", u"CCD\u4f7f\u80fd\u8bbe\u7f6e\uff08CCD1\u5f00~\u5173 2\u5f00~\u5173\uff09", None))
        self.CCDComboBox.setItemText(0, QCoreApplication.translate("FurnaceSwitch", u"CCD1\u4f7f\u80fd", None))
        self.CCDComboBox.setItemText(1, QCoreApplication.translate("FurnaceSwitch", u"CCD1\u5173", None))
        self.CCDComboBox.setItemText(2, QCoreApplication.translate("FurnaceSwitch", u"CCD2\u4f7f\u80fd", None))
        self.CCDComboBox.setItemText(3, QCoreApplication.translate("FurnaceSwitch", u"CCD2\u5173", None))

        self.label_13.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_12.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u503c", None))
        self.label_5.setText(QCoreApplication.translate("FurnaceSwitch", u"\u9600\u95e8\u4f7f\u80fd\u8bbe\u7f6e", None))
        self.valveComboBox.setItemText(0, QCoreApplication.translate("FurnaceSwitch", u"\u6c2e\u6c14\u9600\u95e8\u5f00\uff08\u7535\u5e73\uff09", None))
        self.valveComboBox.setItemText(1, QCoreApplication.translate("FurnaceSwitch", u"\u6c2e\u6c14\u9600\u95e8\u5173\uff08\u7535\u5e73\uff09", None))
        self.valveComboBox.setItemText(2, QCoreApplication.translate("FurnaceSwitch", u"\u590d\u538b\u5f00\u5173\u5f00\uff08\u7535\u5e73\uff09", None))
        self.valveComboBox.setItemText(3, QCoreApplication.translate("FurnaceSwitch", u"\u590d\u538b\u5f00\u5173\u5173\uff08\u7535\u5e73\uff09", None))
        self.valveComboBox.setItemText(4, QCoreApplication.translate("FurnaceSwitch", u"\u6392\u5e9f\u6c14\u5207\u6362", None))
        self.valveComboBox.setItemText(5, QCoreApplication.translate("FurnaceSwitch", u"\u771f\u7a7a\u63a7\u5236\u5207\u6362", None))
        self.valveComboBox.setItemText(6, QCoreApplication.translate("FurnaceSwitch", u"\u5e9f\u6c14\u771f\u7a7a\u5f00", None))
        self.valveComboBox.setItemText(7, QCoreApplication.translate("FurnaceSwitch", u"\u5e9f\u6c14\u771f\u7a7a\u5173", None))

        self.label_15.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_14.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u503c", None))
        self.label_6.setText(QCoreApplication.translate("FurnaceSwitch", u"\u52a0\u901f\u5ea6\u8bbe\u7f6e\uff08\u52a0\u901f\u5ea6\u5f00~\u5173\uff09", None))
        self.accComboBox.setItemText(0, QCoreApplication.translate("FurnaceSwitch", u"\u52a0\u901f\u5ea6\u5f00", None))
        self.accComboBox.setItemText(1, QCoreApplication.translate("FurnaceSwitch", u"\u52a0\u901f\u5ea6\u5173", None))

        self.label_17.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_16.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u503c", None))
        self.label_7.setText(QCoreApplication.translate("FurnaceSwitch", u"\u6837\u54c1\u76d2\u5f00\u5173 \uff08\u6837\u54c1\u76d2\u5f00~\u5173\uff09", None))
        self.sampleBoxComboBox.setItemText(0, QCoreApplication.translate("FurnaceSwitch", u"\u4f7f\u80fd", None))
        self.sampleBoxComboBox.setItemText(1, QCoreApplication.translate("FurnaceSwitch", u"\u5173\u95ed", None))

        self.label_19.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_18.setText(QCoreApplication.translate("FurnaceSwitch", u"\u5341\u516d\u8fdb\u5236\u503c", None))
        self.commitPushButton.setText(QCoreApplication.translate("FurnaceSwitch", u"\u786e\u5b9a", None))
        self.cancelPushButton.setText(QCoreApplication.translate("FurnaceSwitch", u"\u53d6\u6d88", None))
    # retranslateUi

