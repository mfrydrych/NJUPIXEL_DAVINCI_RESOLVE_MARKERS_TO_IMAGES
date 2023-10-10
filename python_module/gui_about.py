# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_about.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ABOUT_WINDOW(object):
    def setupUi(self, ABOUT_WINDOW):
        if not ABOUT_WINDOW.objectName():
            ABOUT_WINDOW.setObjectName(u"ABOUT_WINDOW")
        ABOUT_WINDOW.resize(570, 509)
        ABOUT_WINDOW.setWindowOpacity(1.000000000000000)
        ABOUT_WINDOW.setAutoFillBackground(False)
        ABOUT_WINDOW.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(41, 40, 46);\n"
"    border-color: rgb(41, 40, 46);\n"
"	border-image: none;\n"
"	padding: 2px 2px 2px 2px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(41, 40, 46);\n"
"    color: rgb(200, 200, 200);\n"
"    padding-left: 2px;\n"
"    border: none;\n"
"}\n"
"QLabel {\n"
"    color: rgb(132, 132, 134);\n"
"	font-size: 14pt;\n"
"}\n"
"QLabel#label_info_1,#label_info_2 {\n"
"    color: rgb(132, 132, 134);\n"
"	font-size: 15pt;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: rgb(209, 81, 77);\n"
"    selection-background-color: rgb(41, 40, 46);\n"
"    alternate-background-color: rgb(45, 160, 145);\n"
"}\n"
"QGroupBox {\n"
"	color: rgb(132, 132, 134);\n"
"    border-style: solid;\n"
"    border-color :#ABABAB;\n"
"}\n"
"QPushButton {\n"
"    color: rgb(210, 210, 210);\n"
"	background-color: rgb(51, 50, 56);\n"
"    selection-color: rgb(128, 128, 128);\n"
"    alternate-background-color: rgb(128, 128, 128);\n"
"    selection-background-color: rgb(128, "
                        "128, 128);\n"
"    border-color: rgb(41, 30, 36);\n"
"    	border-radius: 30px;\n"
"	font-size: 16pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(229, 101, 97);\n"
"	border-color: rgb(31, 30, 36);\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(209, 81, 77);\n"
"    alternate-background-color: rgb(209, 81, 77);\n"
"    selection-background-color: rgb(209, 81, 77);\n"
"	border-color: rgb(31, 30, 36);\n"
"}\n"
"QComboBox::item:first {\n"
"    color: red;\n"
"	background-color: red;\n"
"}\n"
"QComboBox {\n"
"    color: white;\n"
"    border: 2px solid rgb(41, 40, 46);\n"
"    padding: 3 16px;\n"
"    background-color: rgb(51, 50, 56);\n"
"    selection-color: rgb(209, 81, 77);\n"
"    alternate-background-color: rgb(220, 220, 220);\n"
"}\n"
"#QComboBox::drop-down:editable {\n"
"    background: rgb(132, 132, 134);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(ABOUT_WINDOW)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.group_SETTINGS = QGroupBox(ABOUT_WINDOW)
        self.group_SETTINGS.setObjectName(u"group_SETTINGS")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_SETTINGS.sizePolicy().hasHeightForWidth())
        self.group_SETTINGS.setSizePolicy(sizePolicy)
        self.group_SETTINGS.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.group_SETTINGS)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 12)
        self.label_info_1 = QLabel(self.group_SETTINGS)
        self.label_info_1.setObjectName(u"label_info_1")

        self.verticalLayout_4.addWidget(self.label_info_1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.label_info_2 = QLabel(self.group_SETTINGS)
        self.label_info_2.setObjectName(u"label_info_2")

        self.verticalLayout_4.addWidget(self.label_info_2)

        self.label_2 = QLabel(self.group_SETTINGS)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.line_2 = QFrame(self.group_SETTINGS)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.verticalSpacer_3 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.group_SETTINGS)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.label_info_3 = QLabel(self.group_SETTINGS)
        self.label_info_3.setObjectName(u"label_info_3")
        self.label_info_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_info_3)

        self.line = QFrame(self.group_SETTINGS)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.group_SETTINGS)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ABOUT_WINDOW)

        QMetaObject.connectSlotsByName(ABOUT_WINDOW)
    # setupUi

    def retranslateUi(self, ABOUT_WINDOW):
        ABOUT_WINDOW.setWindowTitle(QCoreApplication.translate("ABOUT_WINDOW", u"About", None))
#if QT_CONFIG(tooltip)
        ABOUT_WINDOW.setToolTip(QCoreApplication.translate("ABOUT_WINDOW", u"About", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        ABOUT_WINDOW.setStatusTip(QCoreApplication.translate("ABOUT_WINDOW", u"About", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        ABOUT_WINDOW.setWhatsThis(QCoreApplication.translate("ABOUT_WINDOW", u"About", None))
#endif // QT_CONFIG(whatsthis)
        self.group_SETTINGS.setTitle("")
        self.label_info_1.setText(QCoreApplication.translate("ABOUT_WINDOW", u"NJUPIXEL - DaVinci Resolve Markers To Images - v 1.0", None))
        self.label_info_2.setText(QCoreApplication.translate("ABOUT_WINDOW", u"This aplication allows you to export timeline markers as images file.\n"
"You can choose JPEG, PNG, DPX, TIFF, CIN, PPM, BMP, XPM file type.", None))
        self.label_2.setText(QCoreApplication.translate("ABOUT_WINDOW", u"This application use:\n"
"- PySide6 Framework\n"
"- Timecode conversion module by Igor Ridanovic.\n"
"- https://github.com/IgorRidanovic/smpte/blob/master/SMPTE.py", None))
        self.label.setText(QCoreApplication.translate("ABOUT_WINDOW", u"njupixel@gmail.com", None))
        self.label_info_3.setText(QCoreApplication.translate("ABOUT_WINDOW", u"Copyright \u00a9 2023 NJUPIXEL Maciej Frydrych", None))
    # retranslateUi

