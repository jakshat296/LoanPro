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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1640, 831)
        icon = QIcon()
        icon.addFile(u":/extra/assets/loanmate.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
"#frame_2, #add_recordwidget, #frame_3, #widget_4, #tableWidget_exist_8, #tableView_3, #widget_19 {\n"
"border: 1px solid black;\n"
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
"#appheader_4, #label, #label_2, #label_3, #label_10{\n"
"color: #2596be\n"
"}\n"
"\n"
"#card1_4,#card2_4,#card3_4,#card4_4 {\n"
"background-color: #fefeff;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#viewbtn_5, #generatebtn_6, #backupbtn, #generatebtn, #addcash_4, #removecash_4, #settingbtn_4, #search_remove {\n"
"background-color: #2596be;\n"
"color: #fff;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#daily_line_4 {\n"
"border: 1px solid #2596be;\n"
"}\n"
"\n"
"#dailyreport_4, #widget_16, #add_recordwidget, #widget_4, #widget_19 {\n"
"background-color: #fefeff;"
                        "\n"
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
"border-top-left-radius: 20px;\n"
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
"#frame_2, #frame_3{\n"
"background-color: #fefeff;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#label_93, #label_94, #label_95, #label_96, #label_97, #label_98,#label_100,#label_115,#label_120,#label_121,#label_126,#label_127,#label_124,#label_125,#label_128{\n"
"background-color: #fefeff;\n"
"border-radius: 10px;\n"
"font: 23pt \"Segoe UI\";\n"
"border: 2px solid #2596be;\n"
"}\n"
"\n"
"#name_line,#father_line,#date_line,#amount_line,#jewellery_line,#location_line,#weight_line, #remove_line, #remove_l"
                        "ine_4, #remove_line_9, #remove_line_10, #remove_line_11, #name_line_4,#father_line_4,#date_line_5,#amount_line_4,#jewellery_line_5,#location_line_4,#weight_line_4, #dateEdit, #dateEdit_2, #lineEdit_2{background-color: rgb(254, 254, 255);\n"
"border-radius: 5px;\n"
"font: 21pt \"Segoe UI\";\n"
"border: 2px solid rgb(37, 150, 190);\n"
"}\n"
"\n"
"#comboBox, #comboBox_2, #comboBox_3,#comboBox_4,#comboBox_5{\n"
"border: 2px solid rgb(37, 150, 190);\n"
"}\n"
"\n"
"#remove_line_2, #remove_line_3, #remove_line_6, #remove_line_5,#remove_line_7, #remove_line_8{\n"
"border-radius: 5px;\n"
"font: 21pt \"Segoe UI\";\n"
"border-bottom: 2px solid rgb(37, 150, 190); \n"
"}\n"
"\n"
"#frame_28 {\n"
"border-color: #2596be\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/black icons/assets/icons/black/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashbtn.setIcon(icon1)
        self.dashbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.dashbtn, 0, Qt.AlignTop)

        self.addbtn = QPushButton(self.frame_15)
        self.addbtn.setObjectName(u"addbtn")
        self.addbtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/black icons/assets/icons/black/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addbtn.setIcon(icon2)
        self.addbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.addbtn, 0, Qt.AlignTop)

        self.removebtn = QPushButton(self.frame_15)
        self.removebtn.setObjectName(u"removebtn")
        self.removebtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/black icons/assets/icons/black/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.removebtn.setIcon(icon3)
        self.removebtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.removebtn)

        self.depositbtn = QPushButton(self.frame_15)
        self.depositbtn.setObjectName(u"depositbtn")
        self.depositbtn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/black icons/assets/icons/black/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.depositbtn.setIcon(icon4)
        self.depositbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.depositbtn)

        self.viewbtn_2 = QPushButton(self.frame_15)
        self.viewbtn_2.setObjectName(u"viewbtn_2")
        self.viewbtn_2.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/black icons/assets/icons/black/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.viewbtn_2.setIcon(icon5)
        self.viewbtn_2.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.viewbtn_2)

        self.accountsbtn = QPushButton(self.frame_15)
        self.accountsbtn.setObjectName(u"accountsbtn")
        self.accountsbtn.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/black icons/assets/icons/black/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountsbtn.setIcon(icon6)
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
        self.headerframe_3.setStyleSheet(u"")
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
        self.menubtn_4.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/whiteicons/assets/icons/blue/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menubtn_4.setIcon(icon7)
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
        self.widget_15.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")
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
        icon8 = QIcon()
        icon8.addFile(u":/white icons/assets/icons/white/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addcash_4.setIcon(icon8)
        self.addcash_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_63.addWidget(self.addcash_4)

        self.removecash_4 = QPushButton(self.widget_15)
        self.removecash_4.setObjectName(u"removecash_4")
        self.removecash_4.setMinimumSize(QSize(85, 26))
        self.removecash_4.setMaximumSize(QSize(200, 26))
        self.removecash_4.setFont(font2)
        self.removecash_4.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/white icons/assets/icons/white/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.removecash_4.setIcon(icon9)
        self.removecash_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_63.addWidget(self.removecash_4)

        self.settingbtn_4 = QPushButton(self.widget_15)
        self.settingbtn_4.setObjectName(u"settingbtn_4")
        self.settingbtn_4.setMinimumSize(QSize(85, 26))
        self.settingbtn_4.setMaximumSize(QSize(150, 26))
        self.settingbtn_4.setFont(font2)
        self.settingbtn_4.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/white icons/assets/icons/white/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingbtn_4.setIcon(icon10)
        self.settingbtn_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_63.addWidget(self.settingbtn_4)

        self.accountbtn_4 = QPushButton(self.widget_15)
        self.accountbtn_4.setObjectName(u"accountbtn_4")
        icon11 = QIcon()
        icon11.addFile(u":/whiteicons/assets/icons/blue/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountbtn_4.setIcon(icon11)
        self.accountbtn_4.setIconSize(QSize(32, 32))

        self.horizontalLayout_63.addWidget(self.accountbtn_4, 0, Qt.AlignRight)


        self.horizontalLayout_59.addWidget(self.widget_15)


        self.verticalLayout_31.addWidget(self.headerframe_3)

        self.stackedWidget = QCustomQStackedWidget(self.frame)
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
        self.card1_4.setStyleSheet(u"border: 1px solid black;")
        self.card1_4.setFrameShape(QFrame.StyledPanel)
        self.card1_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.card1_4)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_33 = QFrame(self.card1_4)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"border:none;")
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
        self.label_56.setStyleSheet(u"border:none;")

        self.verticalLayout_33.addWidget(self.label_56, 0, Qt.AlignHCenter)

        self.label_57 = QLabel(self.card1_4)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font1)
        self.label_57.setStyleSheet(u"border:none;")

        self.verticalLayout_33.addWidget(self.label_57, 0, Qt.AlignHCenter)


        self.horizontalLayout_64.addWidget(self.card1_4)

        self.card3_4 = QFrame(self.cardsframe_5)
        self.card3_4.setObjectName(u"card3_4")
        self.card3_4.setStyleSheet(u"border: 1px solid black;")
        self.card3_4.setFrameShape(QFrame.StyledPanel)
        self.card3_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.card3_4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_34 = QFrame(self.card3_4)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"border:none;")
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
        self.label_60.setStyleSheet(u"border:none;")

        self.verticalLayout_34.addWidget(self.label_60, 0, Qt.AlignHCenter)

        self.label_61 = QLabel(self.card3_4)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font1)
        self.label_61.setStyleSheet(u"border:none;\n"
"")

        self.verticalLayout_34.addWidget(self.label_61, 0, Qt.AlignHCenter)


        self.horizontalLayout_64.addWidget(self.card3_4)

        self.card2_4 = QFrame(self.cardsframe_5)
        self.card2_4.setObjectName(u"card2_4")
        self.card2_4.setStyleSheet(u"border: 1px solid black;")
        self.card2_4.setFrameShape(QFrame.StyledPanel)
        self.card2_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.card2_4)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_35 = QFrame(self.card2_4)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"border:none;")
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
        self.label_64.setStyleSheet(u"border:none;")

        self.verticalLayout_35.addWidget(self.label_64, 0, Qt.AlignHCenter)

        self.label_65 = QLabel(self.card2_4)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font1)
        self.label_65.setStyleSheet(u"border:none;")

        self.verticalLayout_35.addWidget(self.label_65, 0, Qt.AlignHCenter)


        self.horizontalLayout_64.addWidget(self.card2_4)

        self.card4_4 = QFrame(self.cardsframe_5)
        self.card4_4.setObjectName(u"card4_4")
        self.card4_4.setStyleSheet(u"border: 1.5px solid black;")
        self.card4_4.setFrameShape(QFrame.StyledPanel)
        self.card4_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.card4_4)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_36 = QFrame(self.card4_4)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"border:none;")
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
        self.label_68.setStyleSheet(u"border:none;")

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
        self.widget_16.setStyleSheet(u"border: 1px solid black;")
        self.verticalLayout_37 = QVBoxLayout(self.widget_16)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_37 = QFrame(self.widget_16)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"QPushButton:checked {\n"
"background-color: #2596be;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QFrame {\n"
"border:none;\n"
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
        self.invesbtn_4.setStyleSheet(u"border:none;")
        icon12 = QIcon()
        icon12.addFile(u":/black icons/assets/icons/black/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.invesbtn_4.setIcon(icon12)
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
        self.returnbtn_4.setStyleSheet(u"border:none;")
        self.returnbtn_4.setIcon(icon1)
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
        self.interestbtn_4.setStyleSheet(u"border:none;")
        icon13 = QIcon()
        icon13.addFile(u":/black icons/assets/icons/black/sidebar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.interestbtn_4.setIcon(icon13)
        self.interestbtn_4.setCheckable(True)
        self.interestbtn_4.setAutoExclusive(True)

        self.horizontalLayout_70.addWidget(self.interestbtn_4)


        self.verticalLayout_37.addWidget(self.frame_37, 0, Qt.AlignTop)

        self.frame_38 = QFrame(self.widget_16)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setStyleSheet(u"border:none;")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.stackedWidget_5 = QCustomQStackedWidget(self.frame_38)
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
        self.dailyreport_4.setStyleSheet(u"border: 1px solid black;")
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
        self.label_69.setStyleSheet(u"border: 1 px solid white")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.label_69)


        self.verticalLayout_38.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.dailyreport_4)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"border:none;")
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
        self.daily_section_5 = QTextEdit(self.frame_41)
        self.daily_section_5.setObjectName(u"daily_section_5")
        self.daily_section_5.setMinimumSize(QSize(0, 240))
        font9 = QFont()
        font9.setPointSize(18)
        self.daily_section_5.setFont(font9)
        self.daily_section_5.setStyleSheet(u"")

        self.horizontalLayout_76.addWidget(self.daily_section_5)


        self.verticalLayout_39.addWidget(self.frame_41)

        self.frame_347 = QFrame(self.frame_40)
        self.frame_347.setObjectName(u"frame_347")
        self.frame_347.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")
        self.frame_347.setFrameShape(QFrame.StyledPanel)
        self.frame_347.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_347)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.generatebtn = QPushButton(self.frame_347)
        self.generatebtn.setObjectName(u"generatebtn")
        self.generatebtn.setMinimumSize(QSize(90, 40))
        self.generatebtn.setMaximumSize(QSize(200, 40))
        font10 = QFont()
        font10.setPointSize(14)
        font10.setBold(False)
        font10.setItalic(False)
        self.generatebtn.setFont(font10)
        self.generatebtn.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/white icons/assets/icons/white/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.generatebtn.setIcon(icon14)
        self.generatebtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_77.addWidget(self.generatebtn)

        self.backupbtn = QPushButton(self.frame_347)
        self.backupbtn.setObjectName(u"backupbtn")
        self.backupbtn.setMinimumSize(QSize(90, 40))
        self.backupbtn.setMaximumSize(QSize(200, 40))
        self.backupbtn.setFont(font10)
        self.backupbtn.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/white icons/assets/icons/white/rotate-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backupbtn.setIcon(icon15)
        self.backupbtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_77.addWidget(self.backupbtn)


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
        self.verticalLayout = QVBoxLayout(self.addpage_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.addpage_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font11 = QFont()
        font11.setPointSize(40)
        self.label.setFont(font11)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.widget)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.addpage_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.add_recordwidget = QWidget(self.frame_5)
        self.add_recordwidget.setObjectName(u"add_recordwidget")
        self.add_recordwidget.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.add_recordwidget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_21 = QFrame(self.add_recordwidget)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_21)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_23)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_93 = QLabel(self.frame_23)
        self.label_93.setObjectName(u"label_93")
        sizePolicy1.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy1)
        self.label_93.setMaximumSize(QSize(360, 16777215))
        self.label_93.setStyleSheet(u"")
        self.label_93.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_93, 0, 0, 1, 1)

        self.name_line = QLineEdit(self.frame_23)
        self.name_line.setObjectName(u"name_line")
        self.name_line.setMaximumSize(QSize(378, 16777215))
        self.name_line.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.gridLayout_2.addWidget(self.name_line, 0, 1, 1, 1)

        self.label_94 = QLabel(self.frame_23)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMaximumSize(QSize(360, 16777215))
        self.label_94.setStyleSheet(u"")
        self.label_94.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_94, 1, 0, 1, 1)

        self.father_line = QLineEdit(self.frame_23)
        self.father_line.setObjectName(u"father_line")
        self.father_line.setMaximumSize(QSize(378, 16777215))
        self.father_line.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.gridLayout_2.addWidget(self.father_line, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_23, 0, 0, 1, 1)

        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_24)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_96 = QLabel(self.frame_24)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMaximumSize(QSize(360, 16777215))
        self.label_96.setStyleSheet(u"")
        self.label_96.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_96, 0, 0, 1, 1)

        self.location_line = QLineEdit(self.frame_24)
        self.location_line.setObjectName(u"location_line")
        self.location_line.setMaximumSize(QSize(378, 16777215))
        self.location_line.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.gridLayout_3.addWidget(self.location_line, 0, 1, 1, 1)

        self.label_95 = QLabel(self.frame_24)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMaximumSize(QSize(360, 16777215))
        self.label_95.setStyleSheet(u"")
        self.label_95.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_95, 1, 0, 1, 1)

        self.amount_line = QLineEdit(self.frame_24)
        self.amount_line.setObjectName(u"amount_line")
        self.amount_line.setMaximumSize(QSize(378, 16777215))
        self.amount_line.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.gridLayout_3.addWidget(self.amount_line, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_24, 0, 1, 1, 1)

        self.frame_25 = QFrame(self.frame_21)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_25)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_98 = QLabel(self.frame_25)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMaximumSize(QSize(360, 16777215))
        self.label_98.setStyleSheet(u"")
        self.label_98.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_98, 0, 0, 1, 1)

        self.jewellery_line = QLineEdit(self.frame_25)
        self.jewellery_line.setObjectName(u"jewellery_line")
        self.jewellery_line.setMaximumSize(QSize(378, 16777215))
        self.jewellery_line.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.gridLayout_4.addWidget(self.jewellery_line, 0, 1, 1, 1)

        self.label_97 = QLabel(self.frame_25)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMaximumSize(QSize(360, 16777215))
        self.label_97.setStyleSheet(u"")
        self.label_97.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_97, 1, 0, 1, 1)

        self.date_line = QLineEdit(self.frame_25)
        self.date_line.setObjectName(u"date_line")
        self.date_line.setMaximumSize(QSize(378, 16777215))
        self.date_line.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.gridLayout_4.addWidget(self.date_line, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_25, 1, 0, 1, 1)

        self.frame_26 = QFrame(self.frame_21)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_26)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_100 = QLabel(self.frame_26)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMaximumSize(QSize(360, 16777215))
        self.label_100.setStyleSheet(u"")
        self.label_100.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_100, 0, 0, 1, 1)

        self.weight_line = QLineEdit(self.frame_26)
        self.weight_line.setObjectName(u"weight_line")
        self.weight_line.setMaximumSize(QSize(378, 16777215))
        self.weight_line.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.gridLayout_5.addWidget(self.weight_line, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_26, 1, 1, 1, 1)


        self.verticalLayout_18.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.add_recordwidget)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"border:none;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_45 = QFrame(self.frame_22)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(200, 200))
        self.frame_45.setStyleSheet(u"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_45)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_7 = QLabel(self.frame_45)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 25pt \"Segoe UI\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_45)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 25pt \"Segoe UI\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.label_8)


        self.horizontalLayout_5.addWidget(self.frame_45)

        self.frame_47 = QFrame(self.frame_22)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_47)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.image_label_3 = QLabel(self.frame_47)
        self.image_label_3.setObjectName(u"image_label_3")
        self.image_label_3.setPixmap(QPixmap(u":/extra/assets/download.png"))

        self.verticalLayout_48.addWidget(self.image_label_3)


        self.horizontalLayout_5.addWidget(self.frame_47)

        self.frame_46 = QFrame(self.frame_22)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_46)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.pushButton_14 = QPushButton(self.frame_46)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 141, 84);\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 15px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/icons/fingerprint.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon16)

        self.verticalLayout_49.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.frame_46)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"background-color: #2596be;\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 15px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}")
        self.pushButton_15.setIcon(icon16)

        self.verticalLayout_49.addWidget(self.pushButton_15)


        self.horizontalLayout_5.addWidget(self.frame_46)


        self.verticalLayout_18.addWidget(self.frame_22)

        self.verticalLayout_18.setStretch(0, 6)
        self.verticalLayout_18.setStretch(1, 2)

        self.verticalLayout_17.addWidget(self.add_recordwidget)


        self.verticalLayout.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.addpage_3)
        self.removepage_2 = QWidget()
        self.removepage_2.setObjectName(u"removepage_2")
        self.verticalLayout_4 = QVBoxLayout(self.removepage_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.removepage_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.widget_2 = QWidget(self.frame_3)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font11)
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_6.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.removepage_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 11, 0, 0)
        self.widget_3 = QWidget(self.frame_6)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setSpacing(7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy5)
        font12 = QFont()
        font12.setPointSize(21)
        self.comboBox.setFont(font12)

        self.horizontalLayout_7.addWidget(self.comboBox)

        self.remove_line = QLineEdit(self.widget_3)
        self.remove_line.setObjectName(u"remove_line")
        sizePolicy3.setHeightForWidth(self.remove_line.sizePolicy().hasHeightForWidth())
        self.remove_line.setSizePolicy(sizePolicy3)
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setPointSize(21)
        font13.setBold(False)
        font13.setItalic(False)
        self.remove_line.setFont(font13)
        self.remove_line.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.horizontalLayout_7.addWidget(self.remove_line)

        self.search_remove = QPushButton(self.widget_3)
        self.search_remove.setObjectName(u"search_remove")
        self.search_remove.setMinimumSize(QSize(200, 0))
        self.search_remove.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(37, 150, 190);\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")

        self.horizontalLayout_7.addWidget(self.search_remove)


        self.verticalLayout_6.addWidget(self.widget_3)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 100))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.frame_9)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(11, 0, 0, 0)
        self.label_104 = QLabel(self.widget_10)
        self.label_104.setObjectName(u"label_104")
        sizePolicy1.setHeightForWidth(self.label_104.sizePolicy().hasHeightForWidth())
        self.label_104.setSizePolicy(sizePolicy1)
        self.label_104.setMaximumSize(QSize(360, 16777215))
        self.label_104.setFont(font9)
        self.label_104.setStyleSheet(u"")
        self.label_104.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_104)

        self.remove_line_7 = QLineEdit(self.widget_10)
        self.remove_line_7.setObjectName(u"remove_line_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.remove_line_7.sizePolicy().hasHeightForWidth())
        self.remove_line_7.setSizePolicy(sizePolicy6)
        self.remove_line_7.setFont(font13)
        self.remove_line_7.setLayoutDirection(Qt.LeftToRight)
        self.remove_line_7.setStyleSheet(u"QLineEdit:focus {\n"
"     border-bottom: 2px solid rgb(185, 100, 100);\n"
"}")
        self.remove_line_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.remove_line_7)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_3)

        self.label_105 = QLabel(self.widget_10)
        self.label_105.setObjectName(u"label_105")
        sizePolicy1.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy1)
        self.label_105.setMaximumSize(QSize(360, 16777215))
        self.label_105.setFont(font9)
        self.label_105.setStyleSheet(u"")
        self.label_105.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_105)

        self.remove_line_8 = QLineEdit(self.widget_10)
        self.remove_line_8.setObjectName(u"remove_line_8")
        sizePolicy6.setHeightForWidth(self.remove_line_8.sizePolicy().hasHeightForWidth())
        self.remove_line_8.setSizePolicy(sizePolicy6)
        self.remove_line_8.setFont(font13)
        self.remove_line_8.setLayoutDirection(Qt.LeftToRight)
        self.remove_line_8.setStyleSheet(u"QLineEdit:focus {\n"
"     border-bottom: 2px solid rgb(185, 100, 100);\n"
"}")
        self.remove_line_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.remove_line_8)


        self.horizontalLayout_17.addWidget(self.widget_10, 0, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.frame_9)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.search_remove_2 = QPushButton(self.widget_9)
        self.search_remove_2.setObjectName(u"search_remove_2")
        self.search_remove_2.setMinimumSize(QSize(200, 0))
        self.search_remove_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 114, 43);\n"
"color: white;\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")

        self.horizontalLayout_18.addWidget(self.search_remove_2)

        self.search_remove_3 = QPushButton(self.widget_9)
        self.search_remove_3.setObjectName(u"search_remove_3")
        self.search_remove_3.setMinimumSize(QSize(200, 0))
        self.search_remove_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color:white;\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")

        self.horizontalLayout_18.addWidget(self.search_remove_3)


        self.horizontalLayout_9.addWidget(self.widget_9)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.frame_8)
        self.tabWidget.setObjectName(u"tabWidget")
        font14 = QFont()
        font14.setPointSize(10)
        self.tabWidget.setFont(font14)
        self.all_records = QWidget()
        self.all_records.setObjectName(u"all_records")
        self.horizontalLayout_8 = QHBoxLayout(self.all_records)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableWidget_exist_5 = QTableWidget(self.all_records)
        if (self.tableWidget_exist_5.columnCount() < 10):
            self.tableWidget_exist_5.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font7);
        self.tableWidget_exist_5.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font7);
        self.tableWidget_exist_5.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font7);
        self.tableWidget_exist_5.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font7);
        self.tableWidget_exist_5.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font7);
        self.tableWidget_exist_5.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font7);
        self.tableWidget_exist_5.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font7);
        self.tableWidget_exist_5.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font7);
        self.tableWidget_exist_5.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font7);
        self.tableWidget_exist_5.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font7);
        self.tableWidget_exist_5.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget_exist_5.setObjectName(u"tableWidget_exist_5")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tableWidget_exist_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_exist_5.setSizePolicy(sizePolicy7)
        self.tableWidget_exist_5.setFont(font7)
        self.tableWidget_exist_5.setMouseTracking(False)
        self.tableWidget_exist_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget_exist_5.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_exist_5.setStyleSheet(u"")
        self.tableWidget_exist_5.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_exist_5.setShowGrid(True)
        self.tableWidget_exist_5.setCornerButtonEnabled(True)
        self.tableWidget_exist_5.horizontalHeader().setDefaultSectionSize(165)

        self.horizontalLayout_8.addWidget(self.tableWidget_exist_5)

        self.tabWidget.addTab(self.all_records, "")
        self.Deposit_History = QWidget()
        self.Deposit_History.setObjectName(u"Deposit_History")
        self.verticalLayout_9 = QVBoxLayout(self.Deposit_History)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tableView = QTableView(self.Deposit_History)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font5)
        self.tableView.setStyleSheet(u"border:1px solid white;")
        self.tableView.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_9.addWidget(self.tableView)

        self.tabWidget.addTab(self.Deposit_History, "")

        self.verticalLayout_8.addWidget(self.tabWidget)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.removepage_2)
        self.depositpage_2 = QWidget()
        self.depositpage_2.setObjectName(u"depositpage_2")
        self.verticalLayout_23 = QVBoxLayout(self.depositpage_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_13 = QFrame(self.depositpage_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.frame_13)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_10 = QVBoxLayout(self.widget_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font11)
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.label_3)


        self.horizontalLayout_10.addWidget(self.widget_4)


        self.verticalLayout_23.addWidget(self.frame_13)

        self.frame_16 = QFrame(self.depositpage_2)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_17)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_5 = QWidget(self.frame_17)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_11.setSpacing(7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.widget_5)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy5.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy5)
        self.comboBox_2.setFont(font12)

        self.horizontalLayout_11.addWidget(self.comboBox_2)

        self.remove_line_4 = QLineEdit(self.widget_5)
        self.remove_line_4.setObjectName(u"remove_line_4")
        sizePolicy3.setHeightForWidth(self.remove_line_4.sizePolicy().hasHeightForWidth())
        self.remove_line_4.setSizePolicy(sizePolicy3)
        self.remove_line_4.setFont(font13)
        self.remove_line_4.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.horizontalLayout_11.addWidget(self.remove_line_4)

        self.search_remove_4 = QPushButton(self.widget_5)
        self.search_remove_4.setObjectName(u"search_remove_4")
        self.search_remove_4.setMinimumSize(QSize(200, 0))
        self.search_remove_4.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(37, 150, 190);\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")

        self.horizontalLayout_11.addWidget(self.search_remove_4)


        self.verticalLayout_19.addWidget(self.widget_5)


        self.verticalLayout_12.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 50))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.frame_18)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_102 = QLabel(self.widget_6)
        self.label_102.setObjectName(u"label_102")
        sizePolicy1.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy1)
        self.label_102.setMaximumSize(QSize(360, 16777215))
        self.label_102.setFont(font9)
        self.label_102.setStyleSheet(u"")
        self.label_102.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_102)

        self.remove_line_5 = QLineEdit(self.widget_6)
        self.remove_line_5.setObjectName(u"remove_line_5")
        sizePolicy6.setHeightForWidth(self.remove_line_5.sizePolicy().hasHeightForWidth())
        self.remove_line_5.setSizePolicy(sizePolicy6)
        self.remove_line_5.setFont(font13)
        self.remove_line_5.setLayoutDirection(Qt.LeftToRight)
        self.remove_line_5.setStyleSheet(u"QLineEdit:focus {\n"
"     border-bottom: 2px solid rgb(185, 100, 100);\n"
"}")
        self.remove_line_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.remove_line_5)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_2)

        self.label_103 = QLabel(self.widget_6)
        self.label_103.setObjectName(u"label_103")
        sizePolicy1.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy1)
        self.label_103.setMaximumSize(QSize(360, 16777215))
        self.label_103.setFont(font9)
        self.label_103.setStyleSheet(u"")
        self.label_103.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_103)

        self.remove_line_6 = QLineEdit(self.widget_6)
        self.remove_line_6.setObjectName(u"remove_line_6")
        sizePolicy6.setHeightForWidth(self.remove_line_6.sizePolicy().hasHeightForWidth())
        self.remove_line_6.setSizePolicy(sizePolicy6)
        self.remove_line_6.setFont(font13)
        self.remove_line_6.setLayoutDirection(Qt.LeftToRight)
        self.remove_line_6.setStyleSheet(u"QLineEdit:focus {\n"
"     border-bottom: 2px solid rgb(185, 100, 100);\n"
"}")
        self.remove_line_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.remove_line_6)


        self.horizontalLayout_12.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.frame_18)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.search_remove_5 = QPushButton(self.widget_7)
        self.search_remove_5.setObjectName(u"search_remove_5")
        self.search_remove_5.setMinimumSize(QSize(200, 0))
        self.search_remove_5.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 114, 43);\n"
"color:white;\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")

        self.horizontalLayout_14.addWidget(self.search_remove_5)


        self.horizontalLayout_12.addWidget(self.widget_7, 0, Qt.AlignRight)

        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_12.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_19)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.tabWidget_2 = QTabWidget(self.frame_20)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setFont(font14)
        self.all_records_2 = QWidget()
        self.all_records_2.setObjectName(u"all_records_2")
        self.horizontalLayout_13 = QHBoxLayout(self.all_records_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tableWidget_exist_6 = QTableWidget(self.all_records_2)
        if (self.tableWidget_exist_6.columnCount() < 10):
            self.tableWidget_exist_6.setColumnCount(10)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font7);
        self.tableWidget_exist_6.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font7);
        self.tableWidget_exist_6.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font7);
        self.tableWidget_exist_6.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font7);
        self.tableWidget_exist_6.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font7);
        self.tableWidget_exist_6.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font7);
        self.tableWidget_exist_6.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font7);
        self.tableWidget_exist_6.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font7);
        self.tableWidget_exist_6.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font7);
        self.tableWidget_exist_6.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font7);
        self.tableWidget_exist_6.setHorizontalHeaderItem(9, __qtablewidgetitem19)
        self.tableWidget_exist_6.setObjectName(u"tableWidget_exist_6")
        sizePolicy7.setHeightForWidth(self.tableWidget_exist_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_exist_6.setSizePolicy(sizePolicy7)
        self.tableWidget_exist_6.setFont(font7)
        self.tableWidget_exist_6.setMouseTracking(False)
        self.tableWidget_exist_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget_exist_6.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_exist_6.setStyleSheet(u"")
        self.tableWidget_exist_6.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_exist_6.setShowGrid(True)
        self.tableWidget_exist_6.setCornerButtonEnabled(True)
        self.tableWidget_exist_6.horizontalHeader().setDefaultSectionSize(165)

        self.horizontalLayout_13.addWidget(self.tableWidget_exist_6)

        self.tabWidget_2.addTab(self.all_records_2, "")
        self.Deposit_History_2 = QWidget()
        self.Deposit_History_2.setObjectName(u"Deposit_History_2")
        self.verticalLayout_22 = QVBoxLayout(self.Deposit_History_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.tableView_2 = QTableView(self.Deposit_History_2)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setFont(font3)
        self.tableView_2.setStyleSheet(u"")
        self.tableView_2.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_22.addWidget(self.tableView_2)

        self.tabWidget_2.addTab(self.Deposit_History_2, "")

        self.verticalLayout_21.addWidget(self.tabWidget_2)


        self.verticalLayout_20.addWidget(self.frame_20)


        self.verticalLayout_12.addWidget(self.frame_19)


        self.verticalLayout_23.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.depositpage_2)
        self.viewpage_2 = QWidget()
        self.viewpage_2.setObjectName(u"viewpage_2")
        self.verticalLayout_24 = QVBoxLayout(self.viewpage_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_10 = QFrame(self.viewpage_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_42 = QFrame(self.frame_10)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy8)
        self.frame_42.setStyleSheet(u"QPushButton:checked {\n"
"background-color: #2596be;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font-weight: bold;\n"
"}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.invesbtn_5 = QPushButton(self.frame_42)
        self.invesbtn_5.setObjectName(u"invesbtn_5")
        sizePolicy2.setHeightForWidth(self.invesbtn_5.sizePolicy().hasHeightForWidth())
        self.invesbtn_5.setSizePolicy(sizePolicy2)
        self.invesbtn_5.setMinimumSize(QSize(0, 40))
        self.invesbtn_5.setFont(font6)
        self.invesbtn_5.setIcon(icon4)
        self.invesbtn_5.setIconSize(QSize(24, 24))
        self.invesbtn_5.setCheckable(True)
        self.invesbtn_5.setChecked(True)
        self.invesbtn_5.setAutoExclusive(True)

        self.horizontalLayout_72.addWidget(self.invesbtn_5)

        self.returnbtn_5 = QPushButton(self.frame_42)
        self.returnbtn_5.setObjectName(u"returnbtn_5")
        sizePolicy3.setHeightForWidth(self.returnbtn_5.sizePolicy().hasHeightForWidth())
        self.returnbtn_5.setSizePolicy(sizePolicy3)
        self.returnbtn_5.setMinimumSize(QSize(0, 40))
        self.returnbtn_5.setFont(font7)
        icon17 = QIcon()
        icon17.addFile(u":/black icons/assets/icons/black/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.returnbtn_5.setIcon(icon17)
        self.returnbtn_5.setIconSize(QSize(24, 24))
        self.returnbtn_5.setCheckable(True)
        self.returnbtn_5.setAutoExclusive(True)

        self.horizontalLayout_72.addWidget(self.returnbtn_5)

        self.interestbtn_5 = QPushButton(self.frame_42)
        self.interestbtn_5.setObjectName(u"interestbtn_5")
        sizePolicy4.setHeightForWidth(self.interestbtn_5.sizePolicy().hasHeightForWidth())
        self.interestbtn_5.setSizePolicy(sizePolicy4)
        self.interestbtn_5.setMinimumSize(QSize(0, 40))
        self.interestbtn_5.setFont(font7)
        icon18 = QIcon()
        icon18.addFile(u":/black icons/assets/icons/black/rotate-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.interestbtn_5.setIcon(icon18)
        self.interestbtn_5.setCheckable(True)
        self.interestbtn_5.setAutoExclusive(True)

        self.horizontalLayout_72.addWidget(self.interestbtn_5)


        self.horizontalLayout_20.addWidget(self.frame_42)


        self.verticalLayout_24.addWidget(self.frame_10)

        self.frame_27 = QFrame(self.viewpage_2)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.stackedWidget_2 = QCustomQStackedWidget(self.frame_27)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_25 = QVBoxLayout(self.page)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_30 = QFrame(self.page)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_30)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_11 = QWidget(self.frame_30)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_22.setSpacing(7)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.comboBox_3 = QComboBox(self.widget_11)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy5.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy5)
        self.comboBox_3.setFont(font12)

        self.horizontalLayout_22.addWidget(self.comboBox_3)

        self.remove_line_9 = QLineEdit(self.widget_11)
        self.remove_line_9.setObjectName(u"remove_line_9")
        sizePolicy3.setHeightForWidth(self.remove_line_9.sizePolicy().hasHeightForWidth())
        self.remove_line_9.setSizePolicy(sizePolicy3)
        self.remove_line_9.setFont(font13)
        self.remove_line_9.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.horizontalLayout_22.addWidget(self.remove_line_9)

        self.search_remove_6 = QPushButton(self.widget_11)
        self.search_remove_6.setObjectName(u"search_remove_6")
        self.search_remove_6.setMinimumSize(QSize(200, 0))
        self.search_remove_6.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(37, 150, 190);\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")

        self.horizontalLayout_22.addWidget(self.search_remove_6)


        self.verticalLayout_26.addWidget(self.widget_11)


        self.verticalLayout_25.addWidget(self.frame_30)

        self.frame_29 = QFrame(self.page)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.tableWidget_exist_7 = QTableWidget(self.frame_29)
        if (self.tableWidget_exist_7.columnCount() < 10):
            self.tableWidget_exist_7.setColumnCount(10)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font7);
        self.tableWidget_exist_7.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font7);
        self.tableWidget_exist_7.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font7);
        self.tableWidget_exist_7.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font7);
        self.tableWidget_exist_7.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font7);
        self.tableWidget_exist_7.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font7);
        self.tableWidget_exist_7.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font7);
        self.tableWidget_exist_7.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font7);
        self.tableWidget_exist_7.setHorizontalHeaderItem(7, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font7);
        self.tableWidget_exist_7.setHorizontalHeaderItem(8, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font7);
        self.tableWidget_exist_7.setHorizontalHeaderItem(9, __qtablewidgetitem29)
        self.tableWidget_exist_7.setObjectName(u"tableWidget_exist_7")
        sizePolicy7.setHeightForWidth(self.tableWidget_exist_7.sizePolicy().hasHeightForWidth())
        self.tableWidget_exist_7.setSizePolicy(sizePolicy7)
        self.tableWidget_exist_7.setFont(font7)
        self.tableWidget_exist_7.setMouseTracking(False)
        self.tableWidget_exist_7.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget_exist_7.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_exist_7.setStyleSheet(u"")
        self.tableWidget_exist_7.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_exist_7.setShowGrid(True)
        self.tableWidget_exist_7.setCornerButtonEnabled(True)
        self.tableWidget_exist_7.horizontalHeader().setDefaultSectionSize(165)

        self.horizontalLayout_23.addWidget(self.tableWidget_exist_7)


        self.verticalLayout_25.addWidget(self.frame_29)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_28 = QVBoxLayout(self.page_2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_32 = QFrame(self.page_2)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_32)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_12 = QWidget(self.frame_32)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_25.setSpacing(7)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.comboBox_4 = QComboBox(self.widget_12)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy5.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy5)
        self.comboBox_4.setFont(font12)

        self.horizontalLayout_25.addWidget(self.comboBox_4)

        self.remove_line_10 = QLineEdit(self.widget_12)
        self.remove_line_10.setObjectName(u"remove_line_10")
        sizePolicy3.setHeightForWidth(self.remove_line_10.sizePolicy().hasHeightForWidth())
        self.remove_line_10.setSizePolicy(sizePolicy3)
        self.remove_line_10.setFont(font13)
        self.remove_line_10.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.horizontalLayout_25.addWidget(self.remove_line_10)

        self.search_remove_7 = QPushButton(self.widget_12)
        self.search_remove_7.setObjectName(u"search_remove_7")
        self.search_remove_7.setMinimumSize(QSize(200, 0))
        self.search_remove_7.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(37, 150, 190);\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")

        self.horizontalLayout_25.addWidget(self.search_remove_7)


        self.verticalLayout_27.addWidget(self.widget_12)


        self.verticalLayout_28.addWidget(self.frame_32)

        self.tableWidget_exist_8 = QTableWidget(self.page_2)
        if (self.tableWidget_exist_8.columnCount() < 10):
            self.tableWidget_exist_8.setColumnCount(10)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font7);
        self.tableWidget_exist_8.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font7);
        self.tableWidget_exist_8.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font7);
        self.tableWidget_exist_8.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font7);
        self.tableWidget_exist_8.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font7);
        self.tableWidget_exist_8.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font7);
        self.tableWidget_exist_8.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font7);
        self.tableWidget_exist_8.setHorizontalHeaderItem(6, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font7);
        self.tableWidget_exist_8.setHorizontalHeaderItem(7, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font7);
        self.tableWidget_exist_8.setHorizontalHeaderItem(8, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font7);
        self.tableWidget_exist_8.setHorizontalHeaderItem(9, __qtablewidgetitem39)
        self.tableWidget_exist_8.setObjectName(u"tableWidget_exist_8")
        sizePolicy7.setHeightForWidth(self.tableWidget_exist_8.sizePolicy().hasHeightForWidth())
        self.tableWidget_exist_8.setSizePolicy(sizePolicy7)
        self.tableWidget_exist_8.setFont(font7)
        self.tableWidget_exist_8.setMouseTracking(False)
        self.tableWidget_exist_8.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget_exist_8.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_exist_8.setStyleSheet(u"")
        self.tableWidget_exist_8.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_exist_8.setShowGrid(True)
        self.tableWidget_exist_8.setCornerButtonEnabled(True)
        self.tableWidget_exist_8.horizontalHeader().setDefaultSectionSize(165)

        self.verticalLayout_28.addWidget(self.tableWidget_exist_8)

        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_30 = QVBoxLayout(self.page_3)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_49 = QFrame(self.page_3)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 0))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.widget_17 = QWidget(self.frame_49)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.widget_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)

        self.horizontalLayout_24.addWidget(self.label_4, 0, Qt.AlignLeft)

        self.remove_line_11 = QLineEdit(self.widget_17)
        self.remove_line_11.setObjectName(u"remove_line_11")
        sizePolicy6.setHeightForWidth(self.remove_line_11.sizePolicy().hasHeightForWidth())
        self.remove_line_11.setSizePolicy(sizePolicy6)
        self.remove_line_11.setFont(font13)
        self.remove_line_11.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.horizontalLayout_24.addWidget(self.remove_line_11, 0, Qt.AlignLeft)

        self.search_remove_8 = QPushButton(self.widget_17)
        self.search_remove_8.setObjectName(u"search_remove_8")
        self.search_remove_8.setMinimumSize(QSize(200, 0))
        self.search_remove_8.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(37, 150, 190);\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")

        self.horizontalLayout_24.addWidget(self.search_remove_8)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_21.addWidget(self.widget_17)


        self.verticalLayout_30.addWidget(self.frame_49)

        self.widget_28 = QWidget(self.page_3)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy)
        self.widget_28.setStyleSheet(u"border-bottom: 2px solid black;\n"
"border-top: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-left: 2px solid black;\n"
"border-radius: 10px")
        self.verticalLayout_43 = QVBoxLayout(self.widget_28)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_28 = QFrame(self.widget_28)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"border:none;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame_51 = QFrame(self.frame_28)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"border:none;")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_51)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_120 = QLabel(self.frame_51)
        self.label_120.setObjectName(u"label_120")
        sizePolicy1.setHeightForWidth(self.label_120.sizePolicy().hasHeightForWidth())
        self.label_120.setSizePolicy(sizePolicy1)
        self.label_120.setMaximumSize(QSize(360, 16777215))
        self.label_120.setStyleSheet(u"QLabel{\n"
"border: 2px solid #2596be;\n"
"}")
        self.label_120.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_120, 0, 0, 1, 1)

        self.name_line_4 = QLineEdit(self.frame_51)
        self.name_line_4.setObjectName(u"name_line_4")
        self.name_line_4.setMaximumSize(QSize(378, 16777215))
        self.name_line_4.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid #2596be;\n"
"}")

        self.gridLayout_17.addWidget(self.name_line_4, 0, 1, 1, 1)

        self.label_121 = QLabel(self.frame_51)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMaximumSize(QSize(360, 16777215))
        self.label_121.setStyleSheet(u"QLabel{\n"
"border: 2px solid #2596be;\n"
"}")
        self.label_121.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_121, 1, 0, 1, 1)

        self.father_line_4 = QLineEdit(self.frame_51)
        self.father_line_4.setObjectName(u"father_line_4")
        self.father_line_4.setMaximumSize(QSize(378, 16777215))
        self.father_line_4.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid #2596be;\n"
"}")

        self.gridLayout_17.addWidget(self.father_line_4, 1, 1, 1, 1)


        self.horizontalLayout_26.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_28)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"border:none;")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_52)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_124 = QLabel(self.frame_52)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMaximumSize(QSize(360, 16777215))
        self.label_124.setStyleSheet(u"QLabel{\n"
"border: 2px solid #2596be;\n"
"}")
        self.label_124.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_124, 0, 0, 1, 1)

        self.location_line_4 = QLineEdit(self.frame_52)
        self.location_line_4.setObjectName(u"location_line_4")
        self.location_line_4.setMaximumSize(QSize(378, 16777215))
        self.location_line_4.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid #2596be;\n"
"}")

        self.gridLayout_19.addWidget(self.location_line_4, 0, 1, 1, 1)

        self.label_125 = QLabel(self.frame_52)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMaximumSize(QSize(360, 16777215))
        self.label_125.setStyleSheet(u"QLabel{\n"
"border: 2px solid #2596be;\n"
"}")
        self.label_125.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_125, 1, 0, 1, 1)

        self.amount_line_4 = QLineEdit(self.frame_52)
        self.amount_line_4.setObjectName(u"amount_line_4")
        self.amount_line_4.setMaximumSize(QSize(378, 16777215))
        self.amount_line_4.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid #2596be;\n"
"}")

        self.gridLayout_19.addWidget(self.amount_line_4, 1, 1, 1, 1)


        self.horizontalLayout_26.addWidget(self.frame_52)


        self.verticalLayout_43.addWidget(self.frame_28)

        self.frame_50 = QFrame(self.widget_28)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"border:none;")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_53 = QFrame(self.frame_50)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"border:none;")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_53)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_126 = QLabel(self.frame_53)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMaximumSize(QSize(360, 16777215))
        self.label_126.setStyleSheet(u"QLabel{\n"
"border: 2px solid #2596be;\n"
"}")
        self.label_126.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.label_126, 0, 0, 1, 1)

        self.jewellery_line_5 = QLineEdit(self.frame_53)
        self.jewellery_line_5.setObjectName(u"jewellery_line_5")
        self.jewellery_line_5.setMaximumSize(QSize(378, 16777215))
        self.jewellery_line_5.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid #2596be;\n"
"}")

        self.gridLayout_20.addWidget(self.jewellery_line_5, 0, 1, 1, 1)

        self.label_127 = QLabel(self.frame_53)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMaximumSize(QSize(360, 16777215))
        self.label_127.setStyleSheet(u"QLabel{\n"
"border: 2px solid #2596be;\n"
"}")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.label_127, 1, 0, 1, 1)

        self.date_line_5 = QLineEdit(self.frame_53)
        self.date_line_5.setObjectName(u"date_line_5")
        self.date_line_5.setMaximumSize(QSize(378, 16777215))
        self.date_line_5.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid #2596be;\n"
"}")

        self.gridLayout_20.addWidget(self.date_line_5, 1, 1, 1, 1)


        self.horizontalLayout_31.addWidget(self.frame_53)

        self.frame_62 = QFrame(self.frame_50)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setStyleSheet(u"border:none;")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_62)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.weight_line_4 = QLineEdit(self.frame_62)
        self.weight_line_4.setObjectName(u"weight_line_4")
        self.weight_line_4.setMaximumSize(QSize(378, 16777215))
        self.weight_line_4.setStyleSheet(u"QLineEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid #2596be;\n"
"}")

        self.gridLayout_21.addWidget(self.weight_line_4, 0, 1, 1, 1)

        self.label_128 = QLabel(self.frame_62)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMaximumSize(QSize(360, 16777215))
        self.label_128.setStyleSheet(u"QLabel{\n"
"border: 2px solid #2596be;\n"
"}")
        self.label_128.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_128, 0, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.frame_62)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(200, 0))
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 141, 84);\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 15px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")
        self.pushButton_17.setIcon(icon16)

        self.gridLayout_21.addWidget(self.pushButton_17, 1, 1, 1, 1)


        self.horizontalLayout_31.addWidget(self.frame_62)


        self.verticalLayout_43.addWidget(self.frame_50)


        self.verticalLayout_30.addWidget(self.widget_28)

        self.stackedWidget_2.addWidget(self.page_3)

        self.horizontalLayout_19.addWidget(self.stackedWidget_2)


        self.verticalLayout_24.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.viewpage_2)
        self.accountspage_2 = QWidget()
        self.accountspage_2.setObjectName(u"accountspage_2")
        self.horizontalLayout_79 = QHBoxLayout(self.accountspage_2)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.frame_54 = QFrame(self.accountspage_2)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_54)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.widget_19 = QWidget(self.frame_55)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_42 = QVBoxLayout(self.widget_19)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_10 = QLabel(self.widget_19)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font11)
        self.label_10.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_42.addWidget(self.label_10, 0, Qt.AlignTop)


        self.horizontalLayout_27.addWidget(self.widget_19)


        self.verticalLayout_29.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_54)
        self.frame_56.setObjectName(u"frame_56")
        sizePolicy.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy)
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_56)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.frame_59 = QFrame(self.frame_57)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.comboBox_5 = QComboBox(self.frame_59)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setFont(font12)
        self.comboBox_5.setStyleSheet(u"Qcombobox:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.horizontalLayout_28.addWidget(self.comboBox_5)

        self.dateEdit = QDateEdit(self.frame_59)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"QdateEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.horizontalLayout_28.addWidget(self.dateEdit)

        self.dateEdit_2 = QDateEdit(self.frame_59)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setStyleSheet(u"QdateEdit:focus {\n"
"     border: 2px solid rgb(185, 100, 100);\n"
"}")

        self.horizontalLayout_28.addWidget(self.dateEdit_2)

        self.search_remove_9 = QPushButton(self.frame_59)
        self.search_remove_9.setObjectName(u"search_remove_9")
        self.search_remove_9.setMinimumSize(QSize(100, 0))
        self.search_remove_9.setMaximumSize(QSize(250, 16777215))
        self.search_remove_9.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(37, 150, 190);\n"
"font: 20pt \"Segoe UI\";\n"
"border-radius: 10px}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75,75,75);\n"
"}")

        self.horizontalLayout_28.addWidget(self.search_remove_9)


        self.horizontalLayout_29.addWidget(self.frame_59, 0, Qt.AlignTop)


        self.verticalLayout_40.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_56)
        self.frame_58.setObjectName(u"frame_58")
        sizePolicy.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy)
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_58)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.tableView_3 = QTableView(self.frame_58)
        self.tableView_3.setObjectName(u"tableView_3")

        self.verticalLayout_41.addWidget(self.tableView_3)

        self.frame_61 = QFrame(self.frame_58)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setStyleSheet(u"")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_9 = QLabel(self.frame_61)
        self.label_9.setObjectName(u"label_9")
        font15 = QFont()
        font15.setFamilies([u"Segoe UI"])
        font15.setPointSize(18)
        font15.setBold(False)
        font15.setItalic(False)
        self.label_9.setFont(font15)
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_9)

        self.lineEdit_2 = QLineEdit(self.frame_61)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"")

        self.horizontalLayout_30.addWidget(self.lineEdit_2)

        self.horizontalLayout_30.setStretch(0, 3)
        self.horizontalLayout_30.setStretch(1, 1)

        self.verticalLayout_41.addWidget(self.frame_61)


        self.verticalLayout_40.addWidget(self.frame_58)

        self.frame_60 = QFrame(self.frame_56)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)

        self.verticalLayout_40.addWidget(self.frame_60)


        self.verticalLayout_29.addWidget(self.frame_56)


        self.horizontalLayout_79.addWidget(self.frame_54)

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

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_5.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LoanPro", None))
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
        self.generatebtn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.backupbtn.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add New Record", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u" Father Name ", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"     Jewellery    ", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"  Date  ", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"  Weight  ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Biometric", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.image_label_3.setText("")
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Add Record", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u" Add Fingerprint", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Remove Record", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Location", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Date", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Fingerprint", None))

        self.search_remove.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Date:-", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Total Interest:- ", None))
        self.search_remove_2.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.search_remove_3.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.search_remove_3.setShortcut("")
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem = self.tableWidget_exist_5.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"User id", None));
        ___qtablewidgetitem1 = self.tableWidget_exist_5.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Amt", None));
        ___qtablewidgetitem2 = self.tableWidget_exist_5.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidget_exist_5.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"F. Name", None));
        ___qtablewidgetitem4 = self.tableWidget_exist_5.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem5 = self.tableWidget_exist_5.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem6 = self.tableWidget_exist_5.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem7 = self.tableWidget_exist_5.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Weight", None));
        ___qtablewidgetitem8 = self.tableWidget_exist_5.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Deposit", None));
        ___qtablewidgetitem9 = self.tableWidget_exist_5.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Deposit Date", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.all_records), QCoreApplication.translate("MainWindow", u"All Records", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Deposit_History), QCoreApplication.translate("MainWindow", u"Deposit History", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Add Deposit", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Location", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Date", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Fingerprint", None))

        self.search_remove_4.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Deposit Date:- ", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Add Deposit", None))
        self.search_remove_5.setText(QCoreApplication.translate("MainWindow", u"Add Deposit", None))
#if QT_CONFIG(shortcut)
        self.search_remove_5.setShortcut("")
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem10 = self.tableWidget_exist_6.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"User id", None));
        ___qtablewidgetitem11 = self.tableWidget_exist_6.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Amt", None));
        ___qtablewidgetitem12 = self.tableWidget_exist_6.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem13 = self.tableWidget_exist_6.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"F. Name", None));
        ___qtablewidgetitem14 = self.tableWidget_exist_6.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem15 = self.tableWidget_exist_6.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem16 = self.tableWidget_exist_6.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem17 = self.tableWidget_exist_6.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Weight", None));
        ___qtablewidgetitem18 = self.tableWidget_exist_6.horizontalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Deposit", None));
        ___qtablewidgetitem19 = self.tableWidget_exist_6.horizontalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Deposit Date", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.all_records_2), QCoreApplication.translate("MainWindow", u"All Records", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Deposit_History_2), QCoreApplication.translate("MainWindow", u"Deposit History", None))
        self.invesbtn_5.setText(QCoreApplication.translate("MainWindow", u"View All Records", None))
        self.returnbtn_5.setText(QCoreApplication.translate("MainWindow", u"View Removed Records", None))
        self.interestbtn_5.setText(QCoreApplication.translate("MainWindow", u"Alter Record", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Location", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Date", None))

        self.search_remove_6.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem20 = self.tableWidget_exist_7.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"User id", None));
        ___qtablewidgetitem21 = self.tableWidget_exist_7.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Amt", None));
        ___qtablewidgetitem22 = self.tableWidget_exist_7.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem23 = self.tableWidget_exist_7.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"F. Name", None));
        ___qtablewidgetitem24 = self.tableWidget_exist_7.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem25 = self.tableWidget_exist_7.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem26 = self.tableWidget_exist_7.horizontalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem27 = self.tableWidget_exist_7.horizontalHeaderItem(7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Weight", None));
        ___qtablewidgetitem28 = self.tableWidget_exist_7.horizontalHeaderItem(8)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Deposit", None));
        ___qtablewidgetitem29 = self.tableWidget_exist_7.horizontalHeaderItem(9)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Deposit Date", None));
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Location", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Date", None))

        self.search_remove_7.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem30 = self.tableWidget_exist_8.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"User id", None));
        ___qtablewidgetitem31 = self.tableWidget_exist_8.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Amt", None));
        ___qtablewidgetitem32 = self.tableWidget_exist_8.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem33 = self.tableWidget_exist_8.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"F. Name", None));
        ___qtablewidgetitem34 = self.tableWidget_exist_8.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem35 = self.tableWidget_exist_8.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem36 = self.tableWidget_exist_8.horizontalHeaderItem(6)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Removed Date", None));
        ___qtablewidgetitem37 = self.tableWidget_exist_8.horizontalHeaderItem(7)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem38 = self.tableWidget_exist_8.horizontalHeaderItem(8)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Weight", None));
        ___qtablewidgetitem39 = self.tableWidget_exist_8.horizontalHeaderItem(9)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Interest", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enter User Id:-  ", None))
        self.search_remove_8.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u" Father Name ", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"     Jewellery    ", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"  Date  ", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"  Weight  ", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"View Accounts", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Investment", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Returns", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Interest", None))

        self.search_remove_9.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_9.setText("")
        self.lineEdit_2.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"alteration", None))
    # retranslateUi

