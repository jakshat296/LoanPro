# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1218, 757)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"color:#000;\n"
"border:none;\n"
"}\n"
"#centralwidget{\n"
"background-color: rgb(239, 249, 254);\n"
"}\n"
"#frame_11{\n"
"background-color: rgb(37, 150, 190);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:transparent;\n"
"}\n"
"\n"
"#searchFrame_4{\n"
"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"}\n"
"\n"
"#appheader_4{\n"
"color: #2596be\n"
"}\n"
"\n"
"#card1_4,#card2_4,#card3_4,#card4_4 {\n"
"background-color: #fefeff;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#viewbtn_5, #generatebtn_6, #backupbtn_6, #savebtn_6, #addcash_4, #removecash_4, #settingbtn_4 {\n"
"background-color: #2596be;\n"
"color: #fff;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#daily_line_4 {\n"
"border: 1px solid #2596be;\n"
"}\n"
"\n"
"#dailyreport_4, #widget_16 {\n"
"background-color: #fefeff;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#daily_section {\n"
"color: #000000;\n"
"}\n"
"\n"
"#headerframe_3{\n"
"background-color: #fefeff;\n"
"}\n"
"\n"
"#dashbtn {\n"
"padding:10px 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20"
                        "px;\n"
"}\n"
"\n"
"#addbtn, #removebtn, #depositbtn, #viewbtn_2, #accountsbtn {\n"
"padding:10px 5px;\n"
"text-align: left;\n"
"}\n"
"\n"
"#label_54, #label_58, #label_62, #label_66 {\n"
"color: #2596be;\n"
"}\n"
"\n"
"#label_57, #label_61, #label_65{\n"
"color: #3bc012;\n"
"}\n"
"#frame_2{\n"
"background-color: #fefeff;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftmenu = QCustomSlideMenu(self.centralwidget)
        self.leftmenu.setObjectName(u"leftmenu")
        self.leftmenu.setMinimumSize(QSize(230, 0))
        self.leftmenu.setMaximumSize(QSize(230, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.leftmenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.leftmenu)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(15, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_27 = QLabel(self.frame_12)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(180, 16777215))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setPixmap(QPixmap(u":/extra/assets/loanmate.png"))
        self.label_27.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.label_27, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.dashbtn = QPushButton(self.frame_15)
        self.dashbtn.setObjectName(u"dashbtn")
        font1 = QFont()
        font1.setPointSize(14)
        self.dashbtn.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/black icons/assets/icons/black/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashbtn.setIcon(icon)
        self.dashbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.dashbtn, 0, Qt.AlignTop)

        self.addbtn = QPushButton(self.frame_15)
        self.addbtn.setObjectName(u"addbtn")
        self.addbtn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/black icons/assets/icons/black/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addbtn.setIcon(icon1)
        self.addbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.addbtn, 0, Qt.AlignTop)

        self.removebtn = QPushButton(self.frame_15)
        self.removebtn.setObjectName(u"removebtn")
        self.removebtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/black icons/assets/icons/black/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.removebtn.setIcon(icon2)
        self.removebtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.removebtn)

        self.depositbtn = QPushButton(self.frame_15)
        self.depositbtn.setObjectName(u"depositbtn")
        self.depositbtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/black icons/assets/icons/black/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.depositbtn.setIcon(icon3)
        self.depositbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.depositbtn)

        self.viewbtn_2 = QPushButton(self.frame_15)
        self.viewbtn_2.setObjectName(u"viewbtn_2")
        self.viewbtn_2.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/black icons/assets/icons/black/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.viewbtn_2.setIcon(icon4)
        self.viewbtn_2.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.viewbtn_2)

        self.accountsbtn = QPushButton(self.frame_15)
        self.accountsbtn.setObjectName(u"accountsbtn")
        self.accountsbtn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/black icons/assets/icons/black/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountsbtn.setIcon(icon5)
        self.accountsbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.accountsbtn)


        self.verticalLayout_16.addWidget(self.frame_15, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_14)


        self.verticalLayout_11.addWidget(self.frame_11)


        self.horizontalLayout.addWidget(self.leftmenu)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.headerframe_3 = QWidget(self.frame)
        self.headerframe_3.setObjectName(u"headerframe_3")
        self.horizontalLayout_59 = QHBoxLayout(self.headerframe_3)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 10)
        self.widget_13 = QWidget(self.headerframe_3)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_60 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.menubtn_4 = QPushButton(self.widget_13)
        self.menubtn_4.setObjectName(u"menubtn_4")
        icon6 = QIcon()
        icon6.addFile(u":/whiteicons/assets/icons/blue/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menubtn_4.setIcon(icon6)
        self.menubtn_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_60.addWidget(self.menubtn_4)

        self.appheader_4 = QLabel(self.widget_13)
        self.appheader_4.setObjectName(u"appheader_4")
        self.appheader_4.setFont(font)

        self.horizontalLayout_60.addWidget(self.appheader_4)


        self.horizontalLayout_59.addWidget(self.widget_13, 0, Qt.AlignLeft)

        self.widget_14 = QWidget(self.headerframe_3)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy1)
        self.horizontalLayout_61 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.searchFrame_4 = QFrame(self.widget_14)
        self.searchFrame_4.setObjectName(u"searchFrame_4")
        sizePolicy1.setHeightForWidth(self.searchFrame_4.sizePolicy().hasHeightForWidth())
        self.searchFrame_4.setSizePolicy(sizePolicy1)
        self.searchFrame_4.setMinimumSize(QSize(260, 0))
        self.searchFrame_4.setFrameShape(QFrame.StyledPanel)
        self.searchFrame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.searchFrame_4)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.searchFrame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(30, 30))
        self.label_13.setMaximumSize(QSize(30, 30))
        self.label_13.setPixmap(QPixmap(u":/whiteicons/assets/icons/blue/search.svg"))

        self.horizontalLayout_62.addWidget(self.label_13)

        self.lineEdit_5 = QLineEdit(self.searchFrame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_62.addWidget(self.lineEdit_5)


        self.horizontalLayout_61.addWidget(self.searchFrame_4, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_59.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.headerframe_3)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_63 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.addcash_4 = QPushButton(self.widget_15)
        self.addcash_4.setObjectName(u"addcash_4")
        self.addcash_4.setMinimumSize(QSize(85, 26))
        self.addcash_4.setMaximumSize(QSize(150, 26))
        font2 = QFont()
        font2.setPointSize(7)
        font2.setBold(False)
        self.addcash_4.setFont(font2)
        self.addcash_4.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/white icons/assets/icons/white/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addcash_4.setIcon(icon7)
        self.addcash_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_63.addWidget(self.addcash_4)

        self.removecash_4 = QPushButton(self.widget_15)
        self.removecash_4.setObjectName(u"removecash_4")
        self.removecash_4.setMinimumSize(QSize(85, 26))
        self.removecash_4.setMaximumSize(QSize(200, 26))
        self.removecash_4.setFont(font2)
        self.removecash_4.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/white icons/assets/icons/white/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.removecash_4.setIcon(icon8)
        self.removecash_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_63.addWidget(self.removecash_4)

        self.settingbtn_4 = QPushButton(self.widget_15)
        self.settingbtn_4.setObjectName(u"settingbtn_4")
        self.settingbtn_4.setMinimumSize(QSize(85, 26))
        self.settingbtn_4.setMaximumSize(QSize(150, 26))
        self.settingbtn_4.setFont(font2)
        self.settingbtn_4.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/white icons/assets/icons/white/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingbtn_4.setIcon(icon9)
        self.settingbtn_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_63.addWidget(self.settingbtn_4)

        self.accountbtn_4 = QPushButton(self.widget_15)
        self.accountbtn_4.setObjectName(u"accountbtn_4")
        icon10 = QIcon()
        icon10.addFile(u":/whiteicons/assets/icons/blue/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountbtn_4.setIcon(icon10)
        self.accountbtn_4.setIconSize(QSize(32, 32))

        self.horizontalLayout_63.addWidget(self.accountbtn_4, 0, Qt.AlignRight)


        self.horizontalLayout_59.addWidget(self.widget_15)


        self.verticalLayout_31.addWidget(self.headerframe_3)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashpage_2 = QWidget()
        self.dashpage_2.setObjectName(u"dashpage_2")
        self.horizontalLayout_78 = QHBoxLayout(self.dashpage_2)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.mainBody_3 = QWidget(self.dashpage_2)
        self.mainBody_3.setObjectName(u"mainBody_3")
        self.verticalLayout_32 = QVBoxLayout(self.mainBody_3)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.cardsframe_5 = QWidget(self.mainBody_3)
        self.cardsframe_5.setObjectName(u"cardsframe_5")
        self.horizontalLayout_64 = QHBoxLayout(self.cardsframe_5)
        self.horizontalLayout_64.setSpacing(20)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(10, 10, 10, 10)
        self.card1_4 = QFrame(self.cardsframe_5)
        self.card1_4.setObjectName(u"card1_4")
        self.card1_4.setFrameShape(QFrame.StyledPanel)
        self.card1_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.card1_4)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_33 = QFrame(self.card1_4)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_54 = QLabel(self.frame_33)
        self.label_54.setObjectName(u"label_54")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(False)
        self.label_54.setFont(font3)

        self.horizontalLayout_65.addWidget(self.label_54, 0, Qt.AlignHCenter)

        self.label_55 = QLabel(self.frame_33)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(35, 35))
        font4 = QFont()
        font4.setPointSize(12)
        self.label_55.setFont(font4)
        self.label_55.setPixmap(QPixmap(u":/extra/assets/investment.svg"))
        self.label_55.setScaledContents(True)

        self.horizontalLayout_65.addWidget(self.label_55, 0, Qt.AlignHCenter)


        self.verticalLayout_33.addWidget(self.frame_33, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_56 = QLabel(self.card1_4)
        self.label_56.setObjectName(u"label_56")
        font5 = QFont()
        font5.setPointSize(20)
        self.label_56.setFont(font5)

        self.verticalLayout_33.addWidget(self.label_56, 0, Qt.AlignHCenter)

        self.label_57 = QLabel(self.card1_4)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font1)

        self.verticalLayout_33.addWidget(self.label_57, 0, Qt.AlignHCenter)


        self.horizontalLayout_64.addWidget(self.card1_4)

        self.card3_4 = QFrame(self.cardsframe_5)
        self.card3_4.setObjectName(u"card3_4")
        self.card3_4.setFrameShape(QFrame.StyledPanel)
        self.card3_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.card3_4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_34 = QFrame(self.card3_4)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_58 = QLabel(self.frame_34)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font3)

        self.horizontalLayout_66.addWidget(self.label_58, 0, Qt.AlignHCenter)

        self.label_59 = QLabel(self.frame_34)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(35, 35))
        self.label_59.setPixmap(QPixmap(u":/extra/assets/total_investment.svg"))
        self.label_59.setScaledContents(True)

        self.horizontalLayout_66.addWidget(self.label_59, 0, Qt.AlignHCenter)


        self.verticalLayout_34.addWidget(self.frame_34, 0, Qt.AlignHCenter)

        self.label_60 = QLabel(self.card3_4)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font5)

        self.verticalLayout_34.addWidget(self.label_60, 0, Qt.AlignHCenter)

        self.label_61 = QLabel(self.card3_4)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font1)

        self.verticalLayout_34.addWidget(self.label_61, 0, Qt.AlignHCenter)


        self.horizontalLayout_64.addWidget(self.card3_4)

        self.card2_4 = QFrame(self.cardsframe_5)
        self.card2_4.setObjectName(u"card2_4")
        self.card2_4.setFrameShape(QFrame.StyledPanel)
        self.card2_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.card2_4)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_35 = QFrame(self.card2_4)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_62 = QLabel(self.frame_35)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font3)

        self.horizontalLayout_67.addWidget(self.label_62, 0, Qt.AlignHCenter)

        self.label_63 = QLabel(self.frame_35)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(35, 35))
        self.label_63.setPixmap(QPixmap(u":/extra/assets/returns.svg"))
        self.label_63.setScaledContents(True)

        self.horizontalLayout_67.addWidget(self.label_63, 0, Qt.AlignHCenter)


        self.verticalLayout_35.addWidget(self.frame_35, 0, Qt.AlignHCenter)

        self.label_64 = QLabel(self.card2_4)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font5)

        self.verticalLayout_35.addWidget(self.label_64, 0, Qt.AlignHCenter)

        self.label_65 = QLabel(self.card2_4)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font1)

        self.verticalLayout_35.addWidget(self.label_65, 0, Qt.AlignHCenter)


        self.horizontalLayout_64.addWidget(self.card2_4)

        self.card4_4 = QFrame(self.cardsframe_5)
        self.card4_4.setObjectName(u"card4_4")
        self.card4_4.setFrameShape(QFrame.StyledPanel)
        self.card4_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.card4_4)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_36 = QFrame(self.card4_4)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_66 = QLabel(self.frame_36)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font3)

        self.horizontalLayout_68.addWidget(self.label_66, 0, Qt.AlignHCenter)

        self.label_67 = QLabel(self.frame_36)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(35, 35))
        self.label_67.setPixmap(QPixmap(u":/extra/assets/interest.svg"))
        self.label_67.setScaledContents(True)

        self.horizontalLayout_68.addWidget(self.label_67, 0, Qt.AlignHCenter)


        self.verticalLayout_36.addWidget(self.frame_36, 0, Qt.AlignHCenter)

        self.label_68 = QLabel(self.card4_4)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font5)

        self.verticalLayout_36.addWidget(self.label_68, 0, Qt.AlignHCenter)


        self.horizontalLayout_64.addWidget(self.card4_4)


        self.verticalLayout_32.addWidget(self.cardsframe_5)

        self.mainframe_5 = QWidget(self.mainBody_3)
        self.mainframe_5.setObjectName(u"mainframe_5")
        sizePolicy.setHeightForWidth(self.mainframe_5.sizePolicy().hasHeightForWidth())
        self.mainframe_5.setSizePolicy(sizePolicy)
        self.horizontalLayout_69 = QHBoxLayout(self.mainframe_5)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.widget_16 = QWidget(self.mainframe_5)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setStyleSheet(u"")
        self.verticalLayout_37 = QVBoxLayout(self.widget_16)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_37 = QFrame(self.widget_16)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"QPushButton:checked {\n"
"background-color: #2596be;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font-weight: bold;\n"
"}")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.invesbtn_4 = QPushButton(self.frame_37)
        self.invesbtn_4.setObjectName(u"invesbtn_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.invesbtn_4.sizePolicy().hasHeightForWidth())
        self.invesbtn_4.setSizePolicy(sizePolicy2)
        self.invesbtn_4.setMinimumSize(QSize(0, 40))
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(False)
        self.invesbtn_4.setFont(font6)
        icon11 = QIcon()
        icon11.addFile(u":/black icons/assets/icons/black/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.invesbtn_4.setIcon(icon11)
        self.invesbtn_4.setIconSize(QSize(24, 24))
        self.invesbtn_4.setCheckable(True)
        self.invesbtn_4.setChecked(True)
        self.invesbtn_4.setAutoExclusive(True)

        self.horizontalLayout_70.addWidget(self.invesbtn_4)

        self.returnbtn_4 = QPushButton(self.frame_37)
        self.returnbtn_4.setObjectName(u"returnbtn_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.returnbtn_4.sizePolicy().hasHeightForWidth())
        self.returnbtn_4.setSizePolicy(sizePolicy3)
        self.returnbtn_4.setMinimumSize(QSize(0, 40))
        font7 = QFont()
        font7.setPointSize(15)
        self.returnbtn_4.setFont(font7)
        self.returnbtn_4.setIcon(icon)
        self.returnbtn_4.setIconSize(QSize(24, 24))
        self.returnbtn_4.setCheckable(True)
        self.returnbtn_4.setAutoExclusive(True)

        self.horizontalLayout_70.addWidget(self.returnbtn_4)

        self.interestbtn_4 = QPushButton(self.frame_37)
        self.interestbtn_4.setObjectName(u"interestbtn_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(15)
        sizePolicy4.setHeightForWidth(self.interestbtn_4.sizePolicy().hasHeightForWidth())
        self.interestbtn_4.setSizePolicy(sizePolicy4)
        self.interestbtn_4.setMinimumSize(QSize(0, 40))
        self.interestbtn_4.setFont(font7)
        icon12 = QIcon()
        icon12.addFile(u":/black icons/assets/icons/black/sidebar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.interestbtn_4.setIcon(icon12)
        self.interestbtn_4.setCheckable(True)
        self.interestbtn_4.setAutoExclusive(True)

        self.horizontalLayout_70.addWidget(self.interestbtn_4)


        self.verticalLayout_37.addWidget(self.frame_37, 0, Qt.AlignTop)

        self.frame_38 = QFrame(self.widget_16)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.stackedWidget_5 = QStackedWidget(self.frame_38)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.investment_chart_4 = QWidget()
        self.investment_chart_4.setObjectName(u"investment_chart_4")
        self.horizontalLayout_2 = QHBoxLayout(self.investment_chart_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.graphicsView_2 = QChartView(self.investment_chart_4)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.horizontalLayout_2.addWidget(self.graphicsView_2)

        self.stackedWidget_5.addWidget(self.investment_chart_4)
        self.return_chart_4 = QWidget()
        self.return_chart_4.setObjectName(u"return_chart_4")
        self.horizontalLayout_3 = QHBoxLayout(self.return_chart_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.graphicsView_3 = QChartView(self.return_chart_4)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.horizontalLayout_3.addWidget(self.graphicsView_3)

        self.stackedWidget_5.addWidget(self.return_chart_4)
        self.interest_chart_4 = QWidget()
        self.interest_chart_4.setObjectName(u"interest_chart_4")
        self.horizontalLayout_74 = QHBoxLayout(self.interest_chart_4)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.graphicsView = QChartView(self.interest_chart_4)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_74.addWidget(self.graphicsView)

        self.stackedWidget_5.addWidget(self.interest_chart_4)

        self.horizontalLayout_71.addWidget(self.stackedWidget_5)


        self.verticalLayout_37.addWidget(self.frame_38)


        self.horizontalLayout_69.addWidget(self.widget_16)

        self.dailyreport_4 = QWidget(self.mainframe_5)
        self.dailyreport_4.setObjectName(u"dailyreport_4")
        self.dailyreport_4.setStyleSheet(u"")
        self.verticalLayout_38 = QVBoxLayout(self.dailyreport_4)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_39 = QFrame(self.dailyreport_4)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 50))
        self.frame_39.setMaximumSize(QSize(16777215, 50))
        self.frame_39.setStyleSheet(u"")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.frame_39)
        self.label_69.setObjectName(u"label_69")
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(True)
        self.label_69.setFont(font8)
        self.label_69.setStyleSheet(u"")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.label_69)

        self.daily_line_4 = QLineEdit(self.frame_39)
        self.daily_line_4.setObjectName(u"daily_line_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.daily_line_4.sizePolicy().hasHeightForWidth())
        self.daily_line_4.setSizePolicy(sizePolicy5)
        self.daily_line_4.setMinimumSize(QSize(250, 0))
        self.daily_line_4.setMaximumSize(QSize(16777215, 16777215))
        font9 = QFont()
        font9.setPointSize(13)
        self.daily_line_4.setFont(font9)
        self.daily_line_4.setStyleSheet(u"")

        self.horizontalLayout_75.addWidget(self.daily_line_4)

        self.viewbtn_5 = QPushButton(self.frame_39)
        self.viewbtn_5.setObjectName(u"viewbtn_5")
        self.viewbtn_5.setMinimumSize(QSize(85, 26))
        self.viewbtn_5.setMaximumSize(QSize(85, 26))
        self.viewbtn_5.setFont(font6)
        self.viewbtn_5.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/white icons/assets/icons/white/file-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.viewbtn_5.setIcon(icon13)
        self.viewbtn_5.setIconSize(QSize(20, 20))

        self.horizontalLayout_75.addWidget(self.viewbtn_5)


        self.verticalLayout_38.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.dailyreport_4)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_40)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"border:none;")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.daily_section_5 = QPlainTextEdit(self.frame_41)
        self.daily_section_5.setObjectName(u"daily_section_5")
        self.daily_section_5.setMinimumSize(QSize(0, 240))
        font10 = QFont()
        font10.setPointSize(18)
        self.daily_section_5.setFont(font10)
        self.daily_section_5.setStyleSheet(u"")

        self.horizontalLayout_76.addWidget(self.daily_section_5)


        self.verticalLayout_39.addWidget(self.frame_41)

        self.frame_347 = QFrame(self.frame_40)
        self.frame_347.setObjectName(u"frame_347")
        self.frame_347.setStyleSheet(u"border:none;")
        self.frame_347.setFrameShape(QFrame.StyledPanel)
        self.frame_347.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_347)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.backupbtn_6 = QPushButton(self.frame_347)
        self.backupbtn_6.setObjectName(u"backupbtn_6")
        self.backupbtn_6.setMinimumSize(QSize(90, 40))
        self.backupbtn_6.setMaximumSize(QSize(200, 40))
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(False)
        font11.setItalic(False)
        self.backupbtn_6.setFont(font11)
        self.backupbtn_6.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/white icons/assets/icons/white/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backupbtn_6.setIcon(icon14)
        self.backupbtn_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_77.addWidget(self.backupbtn_6)

        self.generatebtn_6 = QPushButton(self.frame_347)
        self.generatebtn_6.setObjectName(u"generatebtn_6")
        self.generatebtn_6.setMinimumSize(QSize(90, 40))
        self.generatebtn_6.setMaximumSize(QSize(200, 40))
        self.generatebtn_6.setFont(font11)
        self.generatebtn_6.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/white icons/assets/icons/white/arrow-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.generatebtn_6.setIcon(icon15)
        self.generatebtn_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_77.addWidget(self.generatebtn_6)

        self.savebtn_6 = QPushButton(self.frame_347)
        self.savebtn_6.setObjectName(u"savebtn_6")
        self.savebtn_6.setMinimumSize(QSize(90, 40))
        self.savebtn_6.setMaximumSize(QSize(200, 40))
        self.savebtn_6.setFont(font11)
        self.savebtn_6.setStyleSheet(u"")
        icon16 = QIcon()
        icon16.addFile(u":/white icons/assets/icons/white/rotate-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.savebtn_6.setIcon(icon16)
        self.savebtn_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_77.addWidget(self.savebtn_6)


        self.verticalLayout_39.addWidget(self.frame_347)


        self.verticalLayout_38.addWidget(self.frame_40)


        self.horizontalLayout_69.addWidget(self.dailyreport_4)

        self.horizontalLayout_69.setStretch(0, 5)
        self.horizontalLayout_69.setStretch(1, 3)

        self.verticalLayout_32.addWidget(self.mainframe_5)


        self.horizontalLayout_78.addWidget(self.mainBody_3)

        self.stackedWidget.addWidget(self.dashpage_2)
        self.addpage_3 = QWidget()
        self.addpage_3.setObjectName(u"addpage_3")
        self.verticalLayout_40 = QVBoxLayout(self.addpage_3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_70 = QLabel(self.addpage_3)
        self.label_70.setObjectName(u"label_70")

        self.verticalLayout_40.addWidget(self.label_70)

        self.stackedWidget.addWidget(self.addpage_3)
        self.removepage_2 = QWidget()
        self.removepage_2.setObjectName(u"removepage_2")
        self.verticalLayout_41 = QVBoxLayout(self.removepage_2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_71 = QLabel(self.removepage_2)
        self.label_71.setObjectName(u"label_71")

        self.verticalLayout_41.addWidget(self.label_71)

        self.stackedWidget.addWidget(self.removepage_2)
        self.depositpage_2 = QWidget()
        self.depositpage_2.setObjectName(u"depositpage_2")
        self.verticalLayout_42 = QVBoxLayout(self.depositpage_2)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_72 = QLabel(self.depositpage_2)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_42.addWidget(self.label_72)

        self.stackedWidget.addWidget(self.depositpage_2)
        self.viewpage_2 = QWidget()
        self.viewpage_2.setObjectName(u"viewpage_2")
        self.verticalLayout_43 = QVBoxLayout(self.viewpage_2)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_73 = QLabel(self.viewpage_2)
        self.label_73.setObjectName(u"label_73")

        self.verticalLayout_43.addWidget(self.label_73)

        self.stackedWidget.addWidget(self.viewpage_2)
        self.accountspage_2 = QWidget()
        self.accountspage_2.setObjectName(u"accountspage_2")
        self.horizontalLayout_79 = QHBoxLayout(self.accountspage_2)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_74 = QLabel(self.accountspage_2)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_79.addWidget(self.label_74)

        self.stackedWidget.addWidget(self.accountspage_2)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.horizontalLayout_80 = QHBoxLayout(self.settings)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_75 = QLabel(self.settings)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_80.addWidget(self.label_75)

        self.stackedWidget.addWidget(self.settings)
        self.alterationpage = QWidget()
        self.alterationpage.setObjectName(u"alterationpage")
        self.horizontalLayout_81 = QHBoxLayout(self.alterationpage)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_76 = QLabel(self.alterationpage)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_81.addWidget(self.label_76)

        self.stackedWidget.addWidget(self.alterationpage)

        self.verticalLayout_31.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_27.setText("")
        self.dashbtn.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.addbtn.setText(QCoreApplication.translate("MainWindow", u"Add New record", None))
        self.removebtn.setText(QCoreApplication.translate("MainWindow", u"Remove Record", None))
        self.depositbtn.setText(QCoreApplication.translate("MainWindow", u"Add Deposit", None))
        self.viewbtn_2.setText(QCoreApplication.translate("MainWindow", u"View Records", None))
        self.accountsbtn.setText(QCoreApplication.translate("MainWindow", u"View Accounts", None))
        self.menubtn_4.setText("")
        self.appheader_4.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.label_13.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Customer", None))
        self.addcash_4.setText(QCoreApplication.translate("MainWindow", u"Add Cash", None))
        self.removecash_4.setText(QCoreApplication.translate("MainWindow", u"Remove Cash", None))
        self.settingbtn_4.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.accountbtn_4.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Total Investment", None))
        self.label_55.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"2,00,000", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"[1250]", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Investment", None))
        self.label_59.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"2,00,000", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"[1250]", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Returns", None))
        self.label_63.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"2,00,000", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"[1250]", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Interest", None))
        self.label_67.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"2,00,000", None))
        self.invesbtn_4.setText(QCoreApplication.translate("MainWindow", u"Investment", None))
        self.returnbtn_4.setText(QCoreApplication.translate("MainWindow", u"Returns", None))
        self.interestbtn_4.setText(QCoreApplication.translate("MainWindow", u"Interest", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Daily Report", None))
        self.viewbtn_5.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.backupbtn_6.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.generatebtn_6.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.savebtn_6.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"add record", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"remove record", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"add deposit", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"view records", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"view accounts", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"alteration", None))
    # retranslateUi

