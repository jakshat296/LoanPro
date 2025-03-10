# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1291, 722)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"color:#000;\n"
"border:none;\n"
"}\n"
"#centralwidget{\n"
"background-color: rgb(239, 249, 254);\n"
"}\n"
"#leftmenu{\n"
"background-color: rgb(37, 150, 190);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:transparent;\n"
"}\n"
"\n"
"#searchFrame{\n"
"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"}\n"
"\n"
"#appheader{\n"
"color: #2596be\n"
"}\n"
"\n"
"#card1,#card2,#card3,#card4 {\n"
"background-color: #fefeff;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#invesbtn, #returnbtn, #interestbtn, #viewbtn, #generatebtn_3, #backupbtn_3, #savebtn_3, #addcash, #removecash, #settingbtn {\n"
"background-color: #2596be;\n"
"color: #fff;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#daily_line {\n"
"border: 1px solid #2596be;\n"
"}\n"
"\n"
"#dailyreport {\n"
"background-color: #fefeff;\n"
"}\n"
"\n"
"#daily_section {\n"
"color: #000000;\n"
"}\n"
"\n"
"#widget {\n"
"background-color: #fefeff;\n"
"}\n"
"\n"
"#headerframe_2{\n"
"background-color: #fefeff;\n"
"}\n"
"\n"
"#dashbtn {\n"
"background-color: #fefeff;\n"
"padding"
                        ":10px 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"#addbtn, #removebtn, #depositbtn, #viewbtn_2, #accountsbtn {\n"
"padding:10px 5px;\n"
"text-align: left;\n"
"}\n"
"\n"
"#label_2, #label_14, #label_17, #label_20 {\n"
"color: #2596be;\n"
"}\n"
"\n"
"#profilecont{\n"
"background-color: #fefeff;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftmenu = QCustomSlideMenu(self.centralwidget)
        self.leftmenu.setObjectName(u"leftmenu")
        self.leftmenu.setMinimumSize(QSize(0, 0))
        self.verticalLayout_11 = QVBoxLayout(self.leftmenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(15, 0, 0, 0)
        self.frame_11 = QFrame(self.leftmenu)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
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
        icon.addFile(u":/whiteicons/assets/icons/blue/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashbtn.setIcon(icon)
        self.dashbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.dashbtn, 0, Qt.AlignTop)

        self.addbtn = QPushButton(self.frame_15)
        self.addbtn.setObjectName(u"addbtn")
        self.addbtn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/white icons/assets/icons/white/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addbtn.setIcon(icon1)
        self.addbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.addbtn, 0, Qt.AlignTop)

        self.removebtn = QPushButton(self.frame_15)
        self.removebtn.setObjectName(u"removebtn")
        self.removebtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/white icons/assets/icons/white/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.removebtn.setIcon(icon2)
        self.removebtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.removebtn)

        self.depositbtn = QPushButton(self.frame_15)
        self.depositbtn.setObjectName(u"depositbtn")
        self.depositbtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/white icons/assets/icons/white/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.depositbtn.setIcon(icon3)
        self.depositbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.depositbtn)

        self.viewbtn_2 = QPushButton(self.frame_15)
        self.viewbtn_2.setObjectName(u"viewbtn_2")
        self.viewbtn_2.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/white icons/assets/icons/white/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.viewbtn_2.setIcon(icon4)
        self.viewbtn_2.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.viewbtn_2)

        self.accountsbtn = QPushButton(self.frame_15)
        self.accountsbtn.setObjectName(u"accountsbtn")
        self.accountsbtn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/white icons/assets/icons/white/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountsbtn.setIcon(icon5)
        self.accountsbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.accountsbtn)


        self.verticalLayout_16.addWidget(self.frame_15, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_14)


        self.verticalLayout_11.addWidget(self.frame_11)


        self.horizontalLayout.addWidget(self.leftmenu)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashpage = QWidget()
        self.dashpage.setObjectName(u"dashpage")
        self.verticalLayout_2 = QVBoxLayout(self.dashpage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainBody_2 = QWidget(self.dashpage)
        self.mainBody_2.setObjectName(u"mainBody_2")
        self.verticalLayout_3 = QVBoxLayout(self.mainBody_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.headerframe_2 = QWidget(self.mainBody_2)
        self.headerframe_2.setObjectName(u"headerframe_2")
        self.horizontalLayout_7 = QHBoxLayout(self.headerframe_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.widget_4 = QWidget(self.headerframe_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.menubtn = QPushButton(self.widget_4)
        self.menubtn.setObjectName(u"menubtn")
        icon6 = QIcon()
        icon6.addFile(u":/whiteicons/assets/icons/blue/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menubtn.setIcon(icon6)
        self.menubtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.menubtn)

        self.appheader = QLabel(self.widget_4)
        self.appheader.setObjectName(u"appheader")
        self.appheader.setFont(font)

        self.horizontalLayout_8.addWidget(self.appheader)


        self.horizontalLayout_7.addWidget(self.widget_4, 0, Qt.AlignLeft)

        self.widget_5 = QWidget(self.headerframe_2)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.searchFrame = QFrame(self.widget_5)
        self.searchFrame.setObjectName(u"searchFrame")
        sizePolicy1.setHeightForWidth(self.searchFrame.sizePolicy().hasHeightForWidth())
        self.searchFrame.setSizePolicy(sizePolicy1)
        self.searchFrame.setMinimumSize(QSize(260, 0))
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.searchFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 30))
        self.label_4.setMaximumSize(QSize(30, 30))
        self.label_4.setPixmap(QPixmap(u":/whiteicons/assets/icons/blue/search.svg"))

        self.horizontalLayout_10.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.searchFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_10.addWidget(self.lineEdit_2)


        self.horizontalLayout_9.addWidget(self.searchFrame, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.widget_5, 0, Qt.AlignHCenter)

        self.widget_6 = QWidget(self.headerframe_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.addcash = QPushButton(self.widget_6)
        self.addcash.setObjectName(u"addcash")
        self.addcash.setMinimumSize(QSize(85, 26))
        self.addcash.setMaximumSize(QSize(150, 26))
        font2 = QFont()
        font2.setPointSize(7)
        font2.setBold(False)
        self.addcash.setFont(font2)
        self.addcash.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/white icons/assets/icons/white/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addcash.setIcon(icon7)
        self.addcash.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.addcash)

        self.removecash = QPushButton(self.widget_6)
        self.removecash.setObjectName(u"removecash")
        self.removecash.setMinimumSize(QSize(85, 26))
        self.removecash.setMaximumSize(QSize(200, 26))
        self.removecash.setFont(font2)
        self.removecash.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/white icons/assets/icons/white/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.removecash.setIcon(icon8)
        self.removecash.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.removecash)

        self.settingbtn = QPushButton(self.widget_6)
        self.settingbtn.setObjectName(u"settingbtn")
        self.settingbtn.setMinimumSize(QSize(85, 26))
        self.settingbtn.setMaximumSize(QSize(150, 26))
        self.settingbtn.setFont(font2)
        self.settingbtn.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/white icons/assets/icons/white/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingbtn.setIcon(icon9)
        self.settingbtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.settingbtn)

        self.accountbtn = QPushButton(self.widget_6)
        self.accountbtn.setObjectName(u"accountbtn")
        icon10 = QIcon()
        icon10.addFile(u":/whiteicons/assets/icons/blue/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountbtn.setIcon(icon10)
        self.accountbtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.accountbtn, 0, Qt.AlignRight)


        self.horizontalLayout_7.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.headerframe_2, 0, Qt.AlignTop)

        self.cardsframe_2 = QWidget(self.mainBody_2)
        self.cardsframe_2.setObjectName(u"cardsframe_2")
        self.horizontalLayout_2 = QHBoxLayout(self.cardsframe_2)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.card1 = QFrame(self.cardsframe_2)
        self.card1.setObjectName(u"card1")
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.card1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.card1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        self.label_2.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(35, 35))
        self.label.setPixmap(QPixmap(u":/extra/assets/investment.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_3 = QLabel(self.card1)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setPointSize(13)
        self.label_3.setFont(font4)

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_23 = QLabel(self.card1)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout.addWidget(self.label_23, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.card1)

        self.card3 = QFrame(self.cardsframe_2)
        self.card3.setObjectName(u"card3")
        self.card3.setFrameShape(QFrame.StyledPanel)
        self.card3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.card3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_6 = QFrame(self.card3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(35, 35))
        self.label_18.setPixmap(QPixmap(u":/extra/assets/total_investment.svg"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.label_19 = QLabel(self.card3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.label_24 = QLabel(self.card3)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_7.addWidget(self.label_24, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.card3)

        self.card2 = QFrame(self.cardsframe_2)
        self.card2.setObjectName(u"card2")
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.card2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.card2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.horizontalLayout_12.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(35, 35))
        self.label_15.setPixmap(QPixmap(u":/extra/assets/returns.svg"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.label_16 = QLabel(self.card2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font4)

        self.verticalLayout_6.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.label_25 = QLabel(self.card2)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_6.addWidget(self.label_25, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.card2)

        self.card4 = QFrame(self.cardsframe_2)
        self.card4.setObjectName(u"card4")
        self.card4.setFrameShape(QFrame.StyledPanel)
        self.card4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.card4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_7 = QFrame(self.card4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.horizontalLayout_14.addWidget(self.label_20, 0, Qt.AlignHCenter)

        self.label_21 = QLabel(self.frame_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(35, 35))
        self.label_21.setPixmap(QPixmap(u":/extra/assets/interest.svg"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_21, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        self.label_22 = QLabel(self.card4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_22, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.card4)


        self.verticalLayout_3.addWidget(self.cardsframe_2)

        self.mainframe_2 = QWidget(self.mainBody_2)
        self.mainframe_2.setObjectName(u"mainframe_2")
        sizePolicy.setHeightForWidth(self.mainframe_2.sizePolicy().hasHeightForWidth())
        self.mainframe_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_15 = QHBoxLayout(self.mainframe_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget = QWidget(self.mainframe_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.invesbtn = QPushButton(self.frame_8)
        self.invesbtn.setObjectName(u"invesbtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.invesbtn.sizePolicy().hasHeightForWidth())
        self.invesbtn.setSizePolicy(sizePolicy2)
        self.invesbtn.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(False)
        self.invesbtn.setFont(font5)
        icon11 = QIcon()
        icon11.addFile(u":/white icons/assets/icons/white/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.invesbtn.setIcon(icon11)
        self.invesbtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.invesbtn)

        self.returnbtn = QPushButton(self.frame_8)
        self.returnbtn.setObjectName(u"returnbtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.returnbtn.sizePolicy().hasHeightForWidth())
        self.returnbtn.setSizePolicy(sizePolicy3)
        self.returnbtn.setMinimumSize(QSize(0, 40))
        font6 = QFont()
        font6.setPointSize(15)
        self.returnbtn.setFont(font6)
        icon12 = QIcon()
        icon12.addFile(u":/white icons/assets/icons/white/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.returnbtn.setIcon(icon12)
        self.returnbtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.returnbtn)

        self.interestbtn = QPushButton(self.frame_8)
        self.interestbtn.setObjectName(u"interestbtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(15)
        sizePolicy4.setHeightForWidth(self.interestbtn.sizePolicy().hasHeightForWidth())
        self.interestbtn.setSizePolicy(sizePolicy4)
        self.interestbtn.setMinimumSize(QSize(0, 40))
        self.interestbtn.setFont(font6)
        icon13 = QIcon()
        icon13.addFile(u":/white icons/assets/icons/white/sidebar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.interestbtn.setIcon(icon13)

        self.horizontalLayout_16.addWidget(self.interestbtn)


        self.verticalLayout_9.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.frame_9 = QFrame(self.widget)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.stackedWidget_2 = QStackedWidget(self.frame_9)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.investment_chart = QWidget()
        self.investment_chart.setObjectName(u"investment_chart")
        self.horizontalLayout_18 = QHBoxLayout(self.investment_chart)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.Ichart = QWidget(self.investment_chart)
        self.Ichart.setObjectName(u"Ichart")

        self.horizontalLayout_18.addWidget(self.Ichart)

        self.stackedWidget_2.addWidget(self.investment_chart)
        self.return_chart = QWidget()
        self.return_chart.setObjectName(u"return_chart")
        self.horizontalLayout_19 = QHBoxLayout(self.return_chart)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.Rchart = QWidget(self.return_chart)
        self.Rchart.setObjectName(u"Rchart")

        self.horizontalLayout_19.addWidget(self.Rchart)

        self.stackedWidget_2.addWidget(self.return_chart)
        self.interest_chart = QWidget()
        self.interest_chart.setObjectName(u"interest_chart")
        self.horizontalLayout_20 = QHBoxLayout(self.interest_chart)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.Inchart = QWidget(self.interest_chart)
        self.Inchart.setObjectName(u"Inchart")

        self.horizontalLayout_20.addWidget(self.Inchart)

        self.stackedWidget_2.addWidget(self.interest_chart)

        self.horizontalLayout_17.addWidget(self.stackedWidget_2)


        self.verticalLayout_9.addWidget(self.frame_9)


        self.horizontalLayout_15.addWidget(self.widget)

        self.dailyreport = QWidget(self.mainframe_2)
        self.dailyreport.setObjectName(u"dailyreport")
        self.dailyreport.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.dailyreport)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_17 = QFrame(self.dailyreport)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_17)
        self.label_26.setObjectName(u"label_26")
        font7 = QFont()
        font7.setPointSize(13)
        font7.setBold(True)
        self.label_26.setFont(font7)
        self.label_26.setStyleSheet(u"")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_26)

        self.daily_line = QLineEdit(self.frame_17)
        self.daily_line.setObjectName(u"daily_line")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.daily_line.sizePolicy().hasHeightForWidth())
        self.daily_line.setSizePolicy(sizePolicy5)
        self.daily_line.setMinimumSize(QSize(250, 0))
        self.daily_line.setMaximumSize(QSize(16777215, 16777215))
        self.daily_line.setFont(font4)
        self.daily_line.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.daily_line)

        self.viewbtn = QPushButton(self.frame_17)
        self.viewbtn.setObjectName(u"viewbtn")
        self.viewbtn.setMinimumSize(QSize(85, 26))
        self.viewbtn.setMaximumSize(QSize(85, 26))
        self.viewbtn.setFont(font5)
        self.viewbtn.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/white icons/assets/icons/white/file-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.viewbtn.setIcon(icon14)
        self.viewbtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_21.addWidget(self.viewbtn)


        self.verticalLayout_10.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.dailyreport)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_18)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_16 = QFrame(self.frame_18)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"border:none;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.daily_section_2 = QPlainTextEdit(self.frame_16)
        self.daily_section_2.setObjectName(u"daily_section_2")
        self.daily_section_2.setMinimumSize(QSize(0, 240))
        font8 = QFont()
        font8.setPointSize(18)
        self.daily_section_2.setFont(font8)
        self.daily_section_2.setStyleSheet(u"")

        self.horizontalLayout_25.addWidget(self.daily_section_2)


        self.verticalLayout_17.addWidget(self.frame_16)

        self.frame_344 = QFrame(self.frame_18)
        self.frame_344.setObjectName(u"frame_344")
        self.frame_344.setStyleSheet(u"border:none;")
        self.frame_344.setFrameShape(QFrame.StyledPanel)
        self.frame_344.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_344)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.backupbtn_3 = QPushButton(self.frame_344)
        self.backupbtn_3.setObjectName(u"backupbtn_3")
        self.backupbtn_3.setMinimumSize(QSize(90, 40))
        self.backupbtn_3.setMaximumSize(QSize(200, 40))
        font9 = QFont()
        font9.setPointSize(14)
        font9.setBold(False)
        font9.setItalic(False)
        self.backupbtn_3.setFont(font9)
        self.backupbtn_3.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/white icons/assets/icons/white/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backupbtn_3.setIcon(icon15)
        self.backupbtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.backupbtn_3)

        self.generatebtn_3 = QPushButton(self.frame_344)
        self.generatebtn_3.setObjectName(u"generatebtn_3")
        self.generatebtn_3.setMinimumSize(QSize(90, 40))
        self.generatebtn_3.setMaximumSize(QSize(200, 40))
        self.generatebtn_3.setFont(font9)
        self.generatebtn_3.setStyleSheet(u"")
        icon16 = QIcon()
        icon16.addFile(u":/white icons/assets/icons/white/arrow-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.generatebtn_3.setIcon(icon16)
        self.generatebtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.generatebtn_3)

        self.savebtn_3 = QPushButton(self.frame_344)
        self.savebtn_3.setObjectName(u"savebtn_3")
        self.savebtn_3.setMinimumSize(QSize(90, 40))
        self.savebtn_3.setMaximumSize(QSize(200, 40))
        self.savebtn_3.setFont(font9)
        self.savebtn_3.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/white icons/assets/icons/white/rotate-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.savebtn_3.setIcon(icon17)
        self.savebtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.savebtn_3)


        self.verticalLayout_17.addWidget(self.frame_344)


        self.verticalLayout_10.addWidget(self.frame_18)


        self.horizontalLayout_15.addWidget(self.dailyreport)

        self.horizontalLayout_15.setStretch(0, 5)
        self.horizontalLayout_15.setStretch(1, 3)

        self.verticalLayout_3.addWidget(self.mainframe_2)


        self.verticalLayout_2.addWidget(self.mainBody_2)

        self.stackedWidget.addWidget(self.dashpage)
        self.addpage = QWidget()
        self.addpage.setObjectName(u"addpage")
        self.stackedWidget.addWidget(self.addpage)
        self.removepage = QWidget()
        self.removepage.setObjectName(u"removepage")
        self.stackedWidget.addWidget(self.removepage)
        self.depositpage = QWidget()
        self.depositpage.setObjectName(u"depositpage")
        self.stackedWidget.addWidget(self.depositpage)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.profilecont = QCustomSlideMenu(self.centralwidget)
        self.profilecont.setObjectName(u"profilecont")
        self.profilecont.setMinimumSize(QSize(100, 0))
        self.verticalLayout_4 = QVBoxLayout(self.profilecont)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.profilecont)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font10 = QFont()
        font10.setPointSize(12)
        self.label_5.setFont(font10)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(20, 20))
        self.label_7.setMaximumSize(QSize(20, 50))
        self.label_7.setPixmap(QPixmap(u":/extra/assets/loanmate.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon10)

        self.verticalLayout_5.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon18 = QIcon()
        icon18.addFile(u":/whiteicons/assets/icons/blue/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon18)

        self.verticalLayout_5.addWidget(self.pushButton_2, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.profilecont, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(2)


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
        self.menubtn.setText("")
        self.appheader.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.label_4.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Customer", None))
        self.addcash.setText(QCoreApplication.translate("MainWindow", u"Add Cash", None))
        self.removecash.setText(QCoreApplication.translate("MainWindow", u"Remove Cash", None))
        self.settingbtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.accountbtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Investment", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"2,00,000", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"[1250]", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Investment", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"2,00,000", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"[1250]", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Returns", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"2,00,000", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"[1250]", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Interest", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"2,00,000", None))
        self.invesbtn.setText(QCoreApplication.translate("MainWindow", u"Investment", None))
        self.returnbtn.setText(QCoreApplication.translate("MainWindow", u"Returns", None))
        self.interestbtn.setText(QCoreApplication.translate("MainWindow", u"Interest", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Daily Report", None))
        self.viewbtn.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.backupbtn_3.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.generatebtn_3.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.savebtn_3.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LoanMate", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_7.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"My Profile", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"LogOut", None))
    # retranslateUi

