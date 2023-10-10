# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MAIN_WINDOW(object):
    def setupUi(self, MAIN_WINDOW):
        if not MAIN_WINDOW.objectName():
            MAIN_WINDOW.setObjectName("MAIN_WINDOW")
        MAIN_WINDOW.resize(420, 564)
        MAIN_WINDOW.setAutoFillBackground(False)
        MAIN_WINDOW.setStyleSheet(
            "QWidget {\n"
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
            "\n"
            "QLabel {\n"
            "    color: rgb(132, 132, 134);\n"
            "    \n"
            "}\n"
            "QLabel:pressed {\n"
            "    background-color: rgb(209, 81, 77);\n"
            "    selection-background-color: rgb(41, 40, 46);\n"
            "    alternate-background-color: rgb(45, 160, 145);\n"
            "}\n"
            "\n"
            "QGroupBox {\n"
            "	color: rgb(132, 132, 134);\n"
            "    border-style: solid;\n"
            "    border-color :#ABABAB;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(210, 210, 210);\n"
            "	background-color: rgb(51, 50, 56);\n"
            "    selection-color: rgb(128, 128, 128);\n"
            "    alternate-background-color: rgb(128, 128, 128);\n"
            "    selection-background-color: rgb(128, 128, 128);\n"
            "    border-color: rgb(41, 30, 36);\n"
            "	border-radius: 30px;\n"
            "}\n"
            "\n"
            "QPushButto"
            "n:pressed {\n"
            "    background-color: rgb(229, 101, 97);\n"
            "	border-color: rgb(31, 30, 36);\n"
            "	border-radius: 30px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(209, 81, 77);\n"
            "    alternate-background-color: rgb(209, 81, 77);\n"
            "    selection-background-color: rgb(209, 81, 77);\n"
            "	border-color: rgb(31, 30, 36);\n"
            "}\n"
            "QPushButton#btn_about:hover {\n"
            "    background-color: rgb(61, 60, 66);\n"
            "    alternate-background-color: rgb(209, 81, 77);\n"
            "    selection-background-color: rgb(209, 81, 77);\n"
            "	border-color: rgb(31, 30, 36);\n"
            "}\n"
            "QPushButton#btn_export_stills {\n"
            "    color: rgb(210, 210, 210);\n"
            "	background-color: rgb(121, 50, 56);\n"
            "    selection-color: rgb(128, 128, 128);\n"
            "    alternate-background-color: rgb(128, 128, 128);\n"
            "    selection-background-color: rgb(128, 128, 128);\n"
            "    border-color: rgb(41, 30, 36);\n"
            "	border-radius: 30px;\n"
            "}\n"
            "QPushButto#btn_export_stills:pressed {\n"
            "    background-color: rgb(229, 101, 97);\n"
            "	border-color: rgb(31, "
            "30, 36);\n"
            "	border-radius: 30px;\n"
            "}\n"
            "QPushButton#btn_export_stills:hover {\n"
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
            "QRadioButton {\n"
            "    color: rgb(200, 200, 200);\n"
            "    background-color: rgb(132, 132, 134);\n"
            "    selection-color: rgb(45, 160, 145);\n"
            "    alternate-background-color: rgb(45, 160, 145);\n"
            "    selection-background-color: rgb(41, 40, 46);\n"
            "    border-color: rgb(60, 60, 67);  \n"
            "}\n"
            "\n"
            "\n"
            ""
        )
        self.verticalLayout_2 = QVBoxLayout(MAIN_WINDOW)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.group_SETTINGS = QGroupBox(MAIN_WINDOW)
        self.group_SETTINGS.setObjectName("group_SETTINGS")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.group_SETTINGS.sizePolicy().hasHeightForWidth()
        )
        self.group_SETTINGS.setSizePolicy(sizePolicy)
        self.group_SETTINGS.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.group_SETTINGS)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 12)
        self.label_chosemarker = QLabel(self.group_SETTINGS)
        self.label_chosemarker.setObjectName("label_chosemarker")

        self.verticalLayout_4.addWidget(self.label_chosemarker)

        self.cb_markers = QComboBox(self.group_SETTINGS)
        self.cb_markers.addItem("")
        self.cb_markers.setObjectName("cb_markers")
        self.cb_markers.setMaxVisibleItems(17)

        self.verticalLayout_4.addWidget(self.cb_markers)

        self.label_2 = QLabel(self.group_SETTINGS)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.label = QLabel(self.group_SETTINGS)
        self.label.setObjectName("label")

        self.verticalLayout_4.addWidget(self.label)

        self.cb_file_type = QComboBox(self.group_SETTINGS)
        self.cb_file_type.addItem("")
        self.cb_file_type.addItem("")
        self.cb_file_type.addItem("")
        self.cb_file_type.addItem("")
        self.cb_file_type.addItem("")
        self.cb_file_type.addItem("")
        self.cb_file_type.addItem("")
        self.cb_file_type.addItem("")
        self.cb_file_type.setObjectName("cb_file_type")

        self.verticalLayout_4.addWidget(self.cb_file_type)

        self.verticalSpacer_2 = QSpacerItem(
            20, 190, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.line_2 = QFrame(self.group_SETTINGS)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.btn_about = QPushButton(self.group_SETTINGS)
        self.btn_about.setObjectName("btn_about")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.btn_about)

        self.line = QFrame(self.group_SETTINGS)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.btn_export_stills = QPushButton(self.group_SETTINGS)
        self.btn_export_stills.setObjectName("btn_export_stills")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(
            self.btn_export_stills.sizePolicy().hasHeightForWidth()
        )
        self.btn_export_stills.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.btn_export_stills)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout.addWidget(self.group_SETTINGS)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(MAIN_WINDOW)

        QMetaObject.connectSlotsByName(MAIN_WINDOW)

    # setupUi

    def retranslateUi(self, MAIN_WINDOW):
        MAIN_WINDOW.setWindowTitle(
            QCoreApplication.translate(
                "MAIN_WINDOW", "NJUPIXEL - DaVinci Resolve Markers to Images -", None
            )
        )
        # if QT_CONFIG(tooltip)
        MAIN_WINDOW.setToolTip(
            QCoreApplication.translate(
                "MAIN_WINDOW", "NJUPIXEL - DaVinci Resolve Markers to Images -", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        MAIN_WINDOW.setStatusTip(
            QCoreApplication.translate(
                "MAIN_WINDOW", "NJUPIXEL - DaVinci Resolve Markers to Images -", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        MAIN_WINDOW.setWhatsThis(
            QCoreApplication.translate("MAIN_WINDOW", "NJUPIXEL STILL EXPORTER", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.group_SETTINGS.setTitle("")
        self.label_chosemarker.setText(
            QCoreApplication.translate("MAIN_WINDOW", "CHOOSE MARKER:", None)
        )
        self.cb_markers.setItemText(
            0, QCoreApplication.translate("MAIN_WINDOW", "- ALL MARKERS -", None)
        )

        # if QT_CONFIG(tooltip)
        self.cb_markers.setToolTip(
            QCoreApplication.translate(
                "MAIN_WINDOW", "choose marker color to export", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cb_markers.setWhatsThis(
            QCoreApplication.translate(
                "MAIN_WINDOW", "choose marker color to export", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_2.setText(
            QCoreApplication.translate(
                "MAIN_WINDOW", "EXPORT ALL IF MARKER COLOR NOT SELECTED", None
            )
        )
        self.label.setText(
            QCoreApplication.translate("MAIN_WINDOW", "CHOOSE FILE TYPE:", None)
        )
        self.cb_file_type.setItemText(
            0, QCoreApplication.translate("MAIN_WINDOW", "JPG", None)
        )
        self.cb_file_type.setItemText(
            1, QCoreApplication.translate("MAIN_WINDOW", "BMP", None)
        )
        self.cb_file_type.setItemText(
            2, QCoreApplication.translate("MAIN_WINDOW", "CIN", None)
        )
        self.cb_file_type.setItemText(
            3, QCoreApplication.translate("MAIN_WINDOW", "DPX", None)
        )
        self.cb_file_type.setItemText(
            4, QCoreApplication.translate("MAIN_WINDOW", "PNG", None)
        )
        self.cb_file_type.setItemText(
            5, QCoreApplication.translate("MAIN_WINDOW", "PPM", None)
        )
        self.cb_file_type.setItemText(
            6, QCoreApplication.translate("MAIN_WINDOW", "TIF", None)
        )
        self.cb_file_type.setItemText(
            7, QCoreApplication.translate("MAIN_WINDOW", "XPM", None)
        )

        # if QT_CONFIG(tooltip)
        self.cb_file_type.setToolTip(
            QCoreApplication.translate(
                "MAIN_WINDOW", "choose file type to export", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.cb_file_type.setStatusTip(
            QCoreApplication.translate(
                "MAIN_WINDOW", "choose file type to export", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.cb_file_type.setWhatsThis(
            QCoreApplication.translate(
                "MAIN_WINDOW", "choose file type to export", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.btn_about.setToolTip(
            QCoreApplication.translate("MAIN_WINDOW", "about", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn_about.setStatusTip(
            QCoreApplication.translate("MAIN_WINDOW", "about", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.btn_about.setWhatsThis(
            QCoreApplication.translate("MAIN_WINDOW", "about", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_about.setText(QCoreApplication.translate("MAIN_WINDOW", "ABOUT", None))
        # if QT_CONFIG(tooltip)
        self.btn_export_stills.setToolTip(
            QCoreApplication.translate("MAIN_WINDOW", "export still file", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.btn_export_stills.setWhatsThis(
            QCoreApplication.translate("MAIN_WINDOW", "export still file", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_export_stills.setText(
            QCoreApplication.translate("MAIN_WINDOW", "EXPORT STILLS", None)
        )

    # retranslateUi
