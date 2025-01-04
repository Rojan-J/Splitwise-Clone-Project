# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget

import images_rc
import resource2_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1341, 1150)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: rgba(0, 0, 0, 180);\n"
"    color: white; \n"
"}\n"
"\n"
"QTextBrowser {\n"
"	background-color:#2c313c;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#LeftMenuSubcontainer{\n"
"	background-color: #16191d;\n"
"}\n"
"#LeftMenuSubcontainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#frame_6, #frame_8, #popupNotificationSubContainer, #GrpHeaderSubContainer, #FriendsHeader, #FriendFrame, #ReportsHeader, #ReportSubContainer, #ProfileContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#FriendsFra"
                        "me1, #VisualizeHeader{\n"
"	background-color: #2c313c;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: blue;  /* Change text color for the entire table */\n"
"	background-color: rgba(0, 0, 0, 180);\n"
"}\n"
"QHeaderView::section {\n"
"    color: white;              /* Text color */\n"
"    background-color: black;   /* Background color */\n"
"    font: bold 12px;           /* Font style */\n"
"}\n"
"QCalendarWidget {\n"
"                background-color: red;  /* Background color */\n"
"                border: 1px solid gray;       /* Border color */\n"
"            }\n"
"QCalendarWidget QAbstractItemView {\n"
"                background-color: #16191d;     /* Calendar grid background */\n"
"            }\n"
"QCalendarWidget QToolButton::pressed {\n"
"                background-color: gray;      /* Navigation buttons pressed color */\n"
"            }\n"
"QCalendarWidget QToolButton:hover {\n"
"                background-color: darkgray;  /* Navigation buttons hover color */\n"
"         "
                        "   }\n"
"#DebtGraphBtn, #ExpenseGraphBtn, #FriendsExpenseGraphBtn, #CategoryReportBtn, #GrpReportBtn, #FriendReportBtn, #MonthlyReportBtn, #TotalReportBtn{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_44 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuSubcontainer = QWidget(self.leftMenuContainer)
        self.LeftMenuSubcontainer.setObjectName(u"LeftMenuSubcontainer")
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuSubcontainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuSubcontainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MenuBtn = QPushButton(self.frame)
        self.MenuBtn.setObjectName(u"MenuBtn")
        icon = QIcon()
        icon.addFile(u":/icons2/icons2/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuBtn.setIcon(icon)
        self.MenuBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.MenuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.LeftMenuSubcontainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 20)
        self.HomeBtn = QPushButton(self.frame_2)
        self.HomeBtn.setObjectName(u"HomeBtn")
        font = QFont()
        font.setFamily(u"Swis721 Blk BT")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.HomeBtn.setFont(font)
        self.HomeBtn.setStyleSheet(u"background-color: #1f232a")
        icon1 = QIcon()
        icon1.addFile(u":/icons2/icons2/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeBtn.setIcon(icon1)
        self.HomeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.HomeBtn)

        self.DebtsBtn = QPushButton(self.frame_2)
        self.DebtsBtn.setObjectName(u"DebtsBtn")
        font1 = QFont()
        font1.setFamily(u"Swis721 Blk BT")
        font1.setPointSize(10)
        self.DebtsBtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons2/icons2/credit-card.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.DebtsBtn.setIcon(icon2)
        self.DebtsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.DebtsBtn)

        self.ProfileBtn = QPushButton(self.frame_2)
        self.ProfileBtn.setObjectName(u"ProfileBtn")
        self.ProfileBtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons2/icons2/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ProfileBtn.setIcon(icon3)
        self.ProfileBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.ProfileBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.LeftMenuSubcontainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 20)
        self.InfoBtn = QPushButton(self.frame_3)
        self.InfoBtn.setObjectName(u"InfoBtn")
        self.InfoBtn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons2/icons2/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.InfoBtn.setIcon(icon4)
        self.InfoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.InfoBtn)

        self.LogOutBtn_3 = QPushButton(self.frame_3)
        self.LogOutBtn_3.setObjectName(u"LogOutBtn_3")
        icon5 = QIcon()
        icon5.addFile(u":/icons2/icons2/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.LogOutBtn_3.setIcon(icon5)
        self.LogOutBtn_3.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.LogOutBtn_3)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.LeftMenuSubcontainer)


        self.horizontalLayout_44.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centerMenuContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuContainer.setSizePolicy(sizePolicy1)
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.centerMenuContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.centerMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuSubContainer.setSizePolicy(sizePolicy2)
        self.centerMenuSubContainer.setMinimumSize(QSize(250, 0))
        self.verticalLayout_3 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.frame_6 = QFrame(self.centerMenuSubContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.closeCenterMenuBtn = QPushButton(self.frame_6)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons2/icons2/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon6)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.centerMenupages = QCustomQStackedWidget(self.centerMenuSubContainer)
        self.centerMenupages.setObjectName(u"centerMenupages")
        self.DebtsPage = QWidget()
        self.DebtsPage.setObjectName(u"DebtsPage")
        self.verticalLayout_6 = QVBoxLayout(self.DebtsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_23 = QScrollArea(self.DebtsPage)
        self.scrollArea_23.setObjectName(u"scrollArea_23")
        self.scrollArea_23.setWidgetResizable(True)
        self.scrollAreaWidgetContents_35 = QWidget()
        self.scrollAreaWidgetContents_35.setObjectName(u"scrollAreaWidgetContents_35")
        self.scrollAreaWidgetContents_35.setGeometry(QRect(0, 0, 218, 1045))
        self.verticalLayout_175 = QVBoxLayout(self.scrollAreaWidgetContents_35)
        self.verticalLayout_175.setObjectName(u"verticalLayout_175")
        self.widget_23 = QWidget(self.scrollAreaWidgetContents_35)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy3)
        self.verticalLayout_176 = QVBoxLayout(self.widget_23)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.label_85 = QLabel(self.widget_23)
        self.label_85.setObjectName(u"label_85")
        font2 = QFont()
        font2.setFamily(u"Swis721 Blk BT")
        font2.setPointSize(11)
        self.label_85.setFont(font2)

        self.verticalLayout_176.addWidget(self.label_85, 0, Qt.AlignLeft)

        self.frame_109 = QFrame(self.widget_23)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_177 = QVBoxLayout(self.frame_109)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.radioButton_49 = QRadioButton(self.frame_109)
        self.radioButton_49.setObjectName(u"radioButton_49")
        font3 = QFont()
        font3.setFamily(u"Swis721 Blk BT")
        self.radioButton_49.setFont(font3)

        self.verticalLayout_177.addWidget(self.radioButton_49)

        self.radioButton_50 = QRadioButton(self.frame_109)
        self.radioButton_50.setObjectName(u"radioButton_50")
        self.radioButton_50.setFont(font3)

        self.verticalLayout_177.addWidget(self.radioButton_50)

        self.radioButton_51 = QRadioButton(self.frame_109)
        self.radioButton_51.setObjectName(u"radioButton_51")
        self.radioButton_51.setFont(font3)

        self.verticalLayout_177.addWidget(self.radioButton_51)


        self.verticalLayout_176.addWidget(self.frame_109, 0, Qt.AlignHCenter)


        self.verticalLayout_175.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.scrollAreaWidgetContents_35)
        self.widget_24.setObjectName(u"widget_24")

        self.verticalLayout_175.addWidget(self.widget_24)

        self.scrollArea_23.setWidget(self.scrollAreaWidgetContents_35)

        self.verticalLayout_6.addWidget(self.scrollArea_23)

        self.centerMenupages.addWidget(self.DebtsPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.verticalLayout_7 = QVBoxLayout(self.informationPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.informationPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.centerMenupages.addWidget(self.informationPage)

        self.verticalLayout_3.addWidget(self.centerMenupages)


        self.horizontalLayout_3.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout_44.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy4)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy5)
        self.headerContainer.setFont(font1)
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.headerContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(24, 24))
        self.label_5.setMaximumSize(QSize(24, 24))
        self.label_5.setPixmap(QPixmap(u":/images/logo2.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        font4 = QFont()
        font4.setFamily(u"Swis721 Blk BT")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setUnderline(False)
        font4.setWeight(50)
        font4.setStrikeOut(False)
        font4.setKerning(False)
        self.label_6.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.NotificationBtn = QPushButton(self.frame_5)
        self.NotificationBtn.setObjectName(u"NotificationBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons2/icons2/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.NotificationBtn.setIcon(icon7)
        self.NotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.NotificationBtn)

        self.SearchBtn = QPushButton(self.frame_5)
        self.SearchBtn.setObjectName(u"SearchBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons2/icons2/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SearchBtn.setIcon(icon8)
        self.SearchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.SearchBtn)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons2/icons2/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons2/icons2/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons2/icons2/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon11)

        self.horizontalLayout_6.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy6)
        self.horizontalLayout_9 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.mainContentContainer = QWidget(self.mainBodyContent)
        self.mainContentContainer.setObjectName(u"mainContentContainer")
        sizePolicy4.setHeightForWidth(self.mainContentContainer.sizePolicy().hasHeightForWidth())
        self.mainContentContainer.setSizePolicy(sizePolicy4)
        self.verticalLayout_14 = QVBoxLayout(self.mainContentContainer)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.mainPages = QCustomQStackedWidget(self.mainContentContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_15 = QVBoxLayout(self.homePage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_11 = QFrame(self.homePage)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_22 = QFrame(self.frame_11)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_22)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.FriendsIcon = QPushButton(self.frame_22)
        self.FriendsIcon.setObjectName(u"FriendsIcon")
        icon12 = QIcon()
        icon12.addFile(u":/images/Layer 0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.FriendsIcon.setIcon(icon12)
        self.FriendsIcon.setIconSize(QSize(200, 200))

        self.verticalLayout_40.addWidget(self.FriendsIcon)

        self.FriendsBtn = QPushButton(self.frame_22)
        self.FriendsBtn.setObjectName(u"FriendsBtn")
        font5 = QFont()
        font5.setFamily(u"Swis721 Blk BT")
        font5.setPointSize(16)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.FriendsBtn.setFont(font5)

        self.verticalLayout_40.addWidget(self.FriendsBtn)


        self.gridLayout.addWidget(self.frame_22, 0, 1, 1, 1, Qt.AlignHCenter)

        self.frame_24 = QFrame(self.frame_11)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_24)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.ReportsIcon = QPushButton(self.frame_24)
        self.ReportsIcon.setObjectName(u"ReportsIcon")
        icon13 = QIcon()
        icon13.addFile(u":/images/2235790.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ReportsIcon.setIcon(icon13)
        self.ReportsIcon.setIconSize(QSize(200, 200))

        self.verticalLayout_42.addWidget(self.ReportsIcon)

        self.reportsBtn = QPushButton(self.frame_24)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setFont(font5)

        self.verticalLayout_42.addWidget(self.reportsBtn)


        self.gridLayout.addWidget(self.frame_24, 1, 1, 1, 1, Qt.AlignHCenter)

        self.frame_23 = QFrame(self.frame_11)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_23)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.ConversionIcon = QPushButton(self.frame_23)
        self.ConversionIcon.setObjectName(u"ConversionIcon")
        icon14 = QIcon()
        icon14.addFile(u":/images/10826388.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ConversionIcon.setIcon(icon14)
        self.ConversionIcon.setIconSize(QSize(200, 200))

        self.verticalLayout_41.addWidget(self.ConversionIcon)

        self.ConversionBtn = QPushButton(self.frame_23)
        self.ConversionBtn.setObjectName(u"ConversionBtn")
        font6 = QFont()
        font6.setFamily(u"Swis721 Blk BT")
        font6.setPointSize(14)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.ConversionBtn.setFont(font6)

        self.verticalLayout_41.addWidget(self.ConversionBtn)


        self.gridLayout.addWidget(self.frame_23, 1, 0, 1, 1, Qt.AlignHCenter)

        self.frame_21 = QFrame(self.frame_11)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_21)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.GroupIcon = QPushButton(self.frame_21)
        self.GroupIcon.setObjectName(u"GroupIcon")
        icon15 = QIcon()
        icon15.addFile(u":/images/718339.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GroupIcon.setIcon(icon15)
        self.GroupIcon.setIconSize(QSize(200, 200))

        self.verticalLayout_39.addWidget(self.GroupIcon)

        self.GroupBtn = QPushButton(self.frame_21)
        self.GroupBtn.setObjectName(u"GroupBtn")
        font7 = QFont()
        font7.setFamily(u"Swis721 Blk BT")
        font7.setPointSize(16)
        self.GroupBtn.setFont(font7)

        self.verticalLayout_39.addWidget(self.GroupBtn)


        self.gridLayout.addWidget(self.frame_21, 0, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_11)

        self.mainPages.addWidget(self.homePage)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.verticalLayout_73 = QVBoxLayout(self.ProfilePage)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.scrollArea_9 = QScrollArea(self.ProfilePage)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_15 = QWidget()
        self.scrollAreaWidgetContents_15.setObjectName(u"scrollAreaWidgetContents_15")
        self.scrollAreaWidgetContents_15.setGeometry(QRect(0, 0, 484, 850))
        self.horizontalLayout_50 = QHBoxLayout(self.scrollAreaWidgetContents_15)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.widget_9 = QWidget(self.scrollAreaWidgetContents_15)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_74 = QVBoxLayout(self.widget_9)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.ProfileContainer = QFrame(self.widget_9)
        self.ProfileContainer.setObjectName(u"ProfileContainer")
        self.ProfileContainer.setFrameShape(QFrame.StyledPanel)
        self.ProfileContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.ProfileContainer)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.PicProfile = QPushButton(self.ProfileContainer)
        self.PicProfile.setObjectName(u"PicProfile")
        icon16 = QIcon()
        icon16.addFile(u":/images/3135823.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PicProfile.setIcon(icon16)
        self.PicProfile.setIconSize(QSize(90, 90))

        self.horizontalLayout_51.addWidget(self.PicProfile, 0, Qt.AlignLeft)

        self.NameProfile = QLabel(self.ProfileContainer)
        self.NameProfile.setObjectName(u"NameProfile")
        sizePolicy5.setHeightForWidth(self.NameProfile.sizePolicy().hasHeightForWidth())
        self.NameProfile.setSizePolicy(sizePolicy5)
        font8 = QFont()
        font8.setFamily(u"Swis721 Blk BT")
        font8.setPointSize(20)
        self.NameProfile.setFont(font8)

        self.horizontalLayout_51.addWidget(self.NameProfile)

        self.EditProfileBtn = QPushButton(self.ProfileContainer)
        self.EditProfileBtn.setObjectName(u"EditProfileBtn")
        icon17 = QIcon()
        icon17.addFile(u":/icons2/icons2/edit-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.EditProfileBtn.setIcon(icon17)
        self.EditProfileBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_51.addWidget(self.EditProfileBtn)


        self.verticalLayout_74.addWidget(self.ProfileContainer, 0, Qt.AlignTop)

        self.ProfileeInformations = QFrame(self.widget_9)
        self.ProfileeInformations.setObjectName(u"ProfileeInformations")
        sizePolicy6.setHeightForWidth(self.ProfileeInformations.sizePolicy().hasHeightForWidth())
        self.ProfileeInformations.setSizePolicy(sizePolicy6)
        self.ProfileeInformations.setMinimumSize(QSize(0, 42))
        self.ProfileeInformations.setFrameShape(QFrame.StyledPanel)
        self.ProfileeInformations.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.ProfileeInformations)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(15)
        self.frame_45 = QFrame(self.ProfileeInformations)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy3.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy3)
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_45)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.label_37 = QLabel(self.frame_45)
        self.label_37.setObjectName(u"label_37")
        sizePolicy6.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy6)
        font9 = QFont()
        font9.setFamily(u"Swis721 Blk BT")
        font9.setPointSize(14)
        self.label_37.setFont(font9)

        self.verticalLayout_76.addWidget(self.label_37, 0, Qt.AlignLeft)


        self.gridLayout_15.addWidget(self.frame_45, 0, 0, 1, 1)

        self.frame_46 = QFrame(self.ProfileeInformations)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy)
        self.frame_46.setMaximumSize(QSize(16777215, 16777215))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_46)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.UsernameProfile = QLabel(self.frame_46)
        self.UsernameProfile.setObjectName(u"UsernameProfile")
        sizePolicy.setHeightForWidth(self.UsernameProfile.sizePolicy().hasHeightForWidth())
        self.UsernameProfile.setSizePolicy(sizePolicy)
        self.UsernameProfile.setMinimumSize(QSize(0, 0))
        self.UsernameProfile.setFont(font2)

        self.verticalLayout_78.addWidget(self.UsernameProfile)


        self.gridLayout_15.addWidget(self.frame_46, 0, 1, 1, 1)

        self.frame_48 = QFrame(self.ProfileeInformations)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy3.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy3)
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_48)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.label_39 = QLabel(self.frame_48)
        self.label_39.setObjectName(u"label_39")
        sizePolicy6.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy6)
        self.label_39.setFont(font9)

        self.verticalLayout_77.addWidget(self.label_39)


        self.gridLayout_15.addWidget(self.frame_48, 1, 0, 1, 1)

        self.frame_51 = QFrame(self.ProfileeInformations)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy6.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy6)
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_51)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.label_41 = QLabel(self.frame_51)
        self.label_41.setObjectName(u"label_41")
        sizePolicy6.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy6)
        self.label_41.setFont(font9)

        self.verticalLayout_81.addWidget(self.label_41)


        self.gridLayout_15.addWidget(self.frame_51, 2, 0, 1, 1)

        self.frame_49 = QFrame(self.ProfileeInformations)
        self.frame_49.setObjectName(u"frame_49")
        sizePolicy6.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy6)
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_49)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.EmailProfile = QLabel(self.frame_49)
        self.EmailProfile.setObjectName(u"EmailProfile")
        self.EmailProfile.setFont(font1)

        self.verticalLayout_89.addWidget(self.EmailProfile)


        self.gridLayout_15.addWidget(self.frame_49, 1, 1, 1, 1)

        self.frame_52 = QFrame(self.ProfileeInformations)
        self.frame_52.setObjectName(u"frame_52")
        sizePolicy6.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy6)
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_52)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.BalanceProfile = QLabel(self.frame_52)
        self.BalanceProfile.setObjectName(u"BalanceProfile")
        self.BalanceProfile.setFont(font2)

        self.verticalLayout_90.addWidget(self.BalanceProfile)


        self.gridLayout_15.addWidget(self.frame_52, 2, 1, 1, 1)

        self.BalanceEditBtn = QPushButton(self.ProfileeInformations)
        self.BalanceEditBtn.setObjectName(u"BalanceEditBtn")
        icon18 = QIcon()
        icon18.addFile(u":/icons2/icons2/edit-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BalanceEditBtn.setIcon(icon18)
        self.BalanceEditBtn.setIconSize(QSize(20, 20))

        self.gridLayout_15.addWidget(self.BalanceEditBtn, 2, 2, 1, 1)


        self.verticalLayout_74.addWidget(self.ProfileeInformations)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy6.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy6)
        self.horizontalLayout_52 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.tableWidget_2 = QTableWidget(self.widget_10)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setShowGrid(True)

        self.horizontalLayout_52.addWidget(self.tableWidget_2)


        self.verticalLayout_74.addWidget(self.widget_10)

        self.frame_44 = QFrame(self.widget_9)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFont(font7)
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.AddRExpenseBtn = QPushButton(self.frame_44)
        self.AddRExpenseBtn.setObjectName(u"AddRExpenseBtn")
        font10 = QFont()
        font10.setFamily(u"Swis721 Blk BT")
        font10.setPointSize(12)
        self.AddRExpenseBtn.setFont(font10)
        icon19 = QIcon()
        icon19.addFile(u":/icons2/icons2/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AddRExpenseBtn.setIcon(icon19)
        self.AddRExpenseBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_53.addWidget(self.AddRExpenseBtn, 0, Qt.AlignLeft)

        self.LogOutProfileBtn = QPushButton(self.frame_44)
        self.LogOutProfileBtn.setObjectName(u"LogOutProfileBtn")
        sizePolicy4.setHeightForWidth(self.LogOutProfileBtn.sizePolicy().hasHeightForWidth())
        self.LogOutProfileBtn.setSizePolicy(sizePolicy4)
        self.LogOutProfileBtn.setFont(font10)
        self.LogOutProfileBtn.setIcon(icon5)
        self.LogOutProfileBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_53.addWidget(self.LogOutProfileBtn, 0, Qt.AlignRight)


        self.verticalLayout_74.addWidget(self.frame_44)


        self.horizontalLayout_50.addWidget(self.widget_9)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_15)

        self.verticalLayout_73.addWidget(self.scrollArea_9)

        self.mainPages.addWidget(self.ProfilePage)
        self.GroupsPage = QWidget()
        self.GroupsPage.setObjectName(u"GroupsPage")
        self.verticalLayout_16 = QVBoxLayout(self.GroupsPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget = QWidget(self.GroupsPage)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 462, 745))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.GroupsGrid = QWidget(self.scrollAreaWidgetContents)
        self.GroupsGrid.setObjectName(u"GroupsGrid")
        sizePolicy6.setHeightForWidth(self.GroupsGrid.sizePolicy().hasHeightForWidth())
        self.GroupsGrid.setSizePolicy(sizePolicy6)
        self.GroupsGrid.setMinimumSize(QSize(0, 0))
        self.verticalLayout_20 = QVBoxLayout(self.GroupsGrid)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")

        self.verticalLayout_13.addWidget(self.GroupsGrid)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.widget_11 = QWidget(self.widget)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout = QHBoxLayout(self.widget_11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addGrpBtn = QPushButton(self.widget_11)
        self.addGrpBtn.setObjectName(u"addGrpBtn")
        icon20 = QIcon()
        icon20.addFile(u":/icons2/icons2/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addGrpBtn.setIcon(icon20)
        self.addGrpBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.addGrpBtn, 0, Qt.AlignLeft)

        self.frame_12 = QFrame(self.widget_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_12)


        self.verticalLayout_8.addWidget(self.widget_11)


        self.verticalLayout_16.addWidget(self.widget)

        self.mainPages.addWidget(self.GroupsPage)
        self.reportPage = QWidget()
        self.reportPage.setObjectName(u"reportPage")
        self.verticalLayout_17 = QVBoxLayout(self.reportPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.scrollArea_8 = QScrollArea(self.reportPage)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.scrollArea_8.sizePolicy().hasHeightForWidth())
        self.scrollArea_8.setSizePolicy(sizePolicy7)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 463, 995))
        self.horizontalLayout_45 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.widget_3 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_58 = QVBoxLayout(self.widget_3)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.ReportsHeader = QWidget(self.widget_3)
        self.ReportsHeader.setObjectName(u"ReportsHeader")
        self.verticalLayout_59 = QVBoxLayout(self.ReportsHeader)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(9, -1, -1, -1)
        self.label_12 = QLabel(self.ReportsHeader)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font8)

        self.verticalLayout_59.addWidget(self.label_12, 0, Qt.AlignTop)


        self.verticalLayout_58.addWidget(self.ReportsHeader, 0, Qt.AlignTop)

        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy6.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy6)
        self.verticalLayout_60 = QVBoxLayout(self.widget_8)
        self.verticalLayout_60.setSpacing(16)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_24 = QLabel(self.widget_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)

        self.verticalLayout_60.addWidget(self.label_24)

        self.label_25 = QLabel(self.widget_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.verticalLayout_60.addWidget(self.label_25)

        self.label_26 = QLabel(self.widget_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.verticalLayout_60.addWidget(self.label_26)

        self.label_27 = QLabel(self.widget_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.verticalLayout_60.addWidget(self.label_27)

        self.label_28 = QLabel(self.widget_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.verticalLayout_60.addWidget(self.label_28)

        self.label_29 = QLabel(self.widget_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.verticalLayout_60.addWidget(self.label_29)


        self.verticalLayout_58.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_63 = QVBoxLayout(self.widget_7)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.VisualizeHeader = QFrame(self.widget_7)
        self.VisualizeHeader.setObjectName(u"VisualizeHeader")
        self.VisualizeHeader.setFrameShape(QFrame.StyledPanel)
        self.VisualizeHeader.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.VisualizeHeader)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.label_31 = QLabel(self.VisualizeHeader)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font7)

        self.verticalLayout_64.addWidget(self.label_31)


        self.verticalLayout_63.addWidget(self.VisualizeHeader, 0, Qt.AlignLeft)


        self.verticalLayout_58.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy6.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy6)
        font11 = QFont()
        font11.setBold(False)
        font11.setWeight(50)
        self.widget_6.setFont(font11)
        self.verticalLayout_61 = QVBoxLayout(self.widget_6)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.frame_33 = QFrame(self.widget_6)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy4.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy4)
        self.frame_33.setMaximumSize(QSize(16777215, 16777215))
        self.frame_33.setLayoutDirection(Qt.LeftToRight)
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_33)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.frame_37 = QFrame(self.frame_33)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_37)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_32 = QLabel(self.frame_37)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)

        self.verticalLayout_66.addWidget(self.label_32)


        self.verticalLayout_65.addWidget(self.frame_37)

        self.frame_36 = QFrame(self.frame_33)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_46.setSpacing(40)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.MonthlyReportBtn = QRadioButton(self.frame_36)
        self.MonthlyReportBtn.setObjectName(u"MonthlyReportBtn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.MonthlyReportBtn.sizePolicy().hasHeightForWidth())
        self.MonthlyReportBtn.setSizePolicy(sizePolicy8)
        self.MonthlyReportBtn.setMinimumSize(QSize(85, 40))
        self.MonthlyReportBtn.setMaximumSize(QSize(85, 40))
        self.MonthlyReportBtn.setFont(font1)

        self.horizontalLayout_46.addWidget(self.MonthlyReportBtn)

        self.TotalReportBtn = QRadioButton(self.frame_36)
        self.TotalReportBtn.setObjectName(u"TotalReportBtn")
        sizePolicy8.setHeightForWidth(self.TotalReportBtn.sizePolicy().hasHeightForWidth())
        self.TotalReportBtn.setSizePolicy(sizePolicy8)
        self.TotalReportBtn.setMinimumSize(QSize(70, 40))
        self.TotalReportBtn.setMaximumSize(QSize(70, 40))
        self.TotalReportBtn.setFont(font1)

        self.horizontalLayout_46.addWidget(self.TotalReportBtn)


        self.verticalLayout_65.addWidget(self.frame_36)


        self.verticalLayout_61.addWidget(self.frame_33)

        self.frame_38 = QFrame(self.widget_6)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy6.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy6)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_38)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_39)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_48.setSpacing(30)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_33 = QLabel(self.frame_40)
        self.label_33.setObjectName(u"label_33")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy9)
        self.label_33.setFont(font1)

        self.horizontalLayout_48.addWidget(self.label_33, 0, Qt.AlignHCenter)

        self.label_34 = QLabel(self.frame_40)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)

        self.horizontalLayout_48.addWidget(self.label_34, 0, Qt.AlignHCenter)


        self.verticalLayout_69.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_39)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_49.setSpacing(30)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.dateEdit = QDateEdit(self.frame_41)
        self.dateEdit.setObjectName(u"dateEdit")
        font12 = QFont()
        font12.setFamily(u"Swis721 BlkEx BT")
        font12.setPointSize(10)
        font12.setBold(False)
        font12.setUnderline(False)
        font12.setWeight(50)
        self.dateEdit.setFont(font12)

        self.horizontalLayout_49.addWidget(self.dateEdit, 0, Qt.AlignHCenter)

        self.dateEdit_2 = QDateEdit(self.frame_41)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        font13 = QFont()
        font13.setFamily(u"Swis721 BlkEx BT")
        font13.setPointSize(10)
        font13.setBold(False)
        font13.setWeight(50)
        self.dateEdit_2.setFont(font13)

        self.horizontalLayout_49.addWidget(self.dateEdit_2, 0, Qt.AlignHCenter)


        self.verticalLayout_69.addWidget(self.frame_41)


        self.verticalLayout_68.addWidget(self.frame_39)


        self.verticalLayout_61.addWidget(self.frame_38)

        self.frame_32 = QFrame(self.widget_6)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy6.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy6)
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_32)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_34)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_30 = QLabel(self.frame_34)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.verticalLayout_62.addWidget(self.label_30)


        self.verticalLayout_67.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy5.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy5)
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_47.setSpacing(30)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.CategoryReportBtn = QRadioButton(self.frame_35)
        self.CategoryReportBtn.setObjectName(u"CategoryReportBtn")
        sizePolicy8.setHeightForWidth(self.CategoryReportBtn.sizePolicy().hasHeightForWidth())
        self.CategoryReportBtn.setSizePolicy(sizePolicy8)
        self.CategoryReportBtn.setMinimumSize(QSize(105, 40))
        self.CategoryReportBtn.setMaximumSize(QSize(100, 40))
        self.CategoryReportBtn.setFont(font1)

        self.horizontalLayout_47.addWidget(self.CategoryReportBtn)

        self.GrpReportBtn = QRadioButton(self.frame_35)
        self.GrpReportBtn.setObjectName(u"GrpReportBtn")
        sizePolicy8.setHeightForWidth(self.GrpReportBtn.sizePolicy().hasHeightForWidth())
        self.GrpReportBtn.setSizePolicy(sizePolicy8)
        self.GrpReportBtn.setMinimumSize(QSize(80, 40))
        self.GrpReportBtn.setMaximumSize(QSize(80, 40))
        self.GrpReportBtn.setFont(font1)

        self.horizontalLayout_47.addWidget(self.GrpReportBtn)

        self.FriendReportBtn = QRadioButton(self.frame_35)
        self.FriendReportBtn.setObjectName(u"FriendReportBtn")
        sizePolicy8.setHeightForWidth(self.FriendReportBtn.sizePolicy().hasHeightForWidth())
        self.FriendReportBtn.setSizePolicy(sizePolicy8)
        self.FriendReportBtn.setMinimumSize(QSize(80, 40))
        self.FriendReportBtn.setMaximumSize(QSize(80, 40))
        self.FriendReportBtn.setFont(font1)

        self.horizontalLayout_47.addWidget(self.FriendReportBtn)


        self.verticalLayout_67.addWidget(self.frame_35)


        self.verticalLayout_61.addWidget(self.frame_32)


        self.verticalLayout_58.addWidget(self.widget_6)

        self.ReportContainer = QWidget(self.widget_3)
        self.ReportContainer.setObjectName(u"ReportContainer")
        sizePolicy6.setHeightForWidth(self.ReportContainer.sizePolicy().hasHeightForWidth())
        self.ReportContainer.setSizePolicy(sizePolicy6)
        self.verticalLayout_70 = QVBoxLayout(self.ReportContainer)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.ReportSubContainer = QWidget(self.ReportContainer)
        self.ReportSubContainer.setObjectName(u"ReportSubContainer")
        sizePolicy6.setHeightForWidth(self.ReportSubContainer.sizePolicy().hasHeightForWidth())
        self.ReportSubContainer.setSizePolicy(sizePolicy6)
        self.verticalLayout_71 = QVBoxLayout(self.ReportSubContainer)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_35 = QLabel(self.ReportSubContainer)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.verticalLayout_71.addWidget(self.label_35)

        self.frame_42 = QFrame(self.ReportSubContainer)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_42)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)

        self.verticalLayout_72.addWidget(self.frame_43)


        self.verticalLayout_71.addWidget(self.frame_42)


        self.verticalLayout_70.addWidget(self.ReportSubContainer)


        self.verticalLayout_58.addWidget(self.ReportContainer)


        self.horizontalLayout_45.addWidget(self.widget_3)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_17.addWidget(self.scrollArea_8)

        self.mainPages.addWidget(self.reportPage)
        self.FriendsPage = QWidget()
        self.FriendsPage.setObjectName(u"FriendsPage")
        self.verticalLayout_84 = QVBoxLayout(self.FriendsPage)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.scrollArea_19 = QScrollArea(self.FriendsPage)
        self.scrollArea_19.setObjectName(u"scrollArea_19")
        self.scrollArea_19.setWidgetResizable(True)
        self.scrollAreaWidgetContents_20 = QWidget()
        self.scrollAreaWidgetContents_20.setObjectName(u"scrollAreaWidgetContents_20")
        self.scrollAreaWidgetContents_20.setGeometry(QRect(0, 0, 266, 622))
        self.verticalLayout_85 = QVBoxLayout(self.scrollAreaWidgetContents_20)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.widget_5 = QWidget(self.scrollAreaWidgetContents_20)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QSize(0, 600))
        self.gridLayout_7 = QGridLayout(self.widget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_63 = QFrame(self.widget_5)
        self.frame_63.setObjectName(u"frame_63")
        sizePolicy6.setHeightForWidth(self.frame_63.sizePolicy().hasHeightForWidth())
        self.frame_63.setSizePolicy(sizePolicy6)
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_63)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")

        self.gridLayout_7.addWidget(self.frame_63, 1, 0, 1, 1)

        self.FriendsHeader = QFrame(self.widget_5)
        self.FriendsHeader.setObjectName(u"FriendsHeader")
        self.FriendsHeader.setFrameShape(QFrame.StyledPanel)
        self.FriendsHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.FriendsHeader)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.frame_67 = QFrame(self.FriendsHeader)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_67)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.FriendsTitle = QLabel(self.frame_67)
        self.FriendsTitle.setObjectName(u"FriendsTitle")
        font14 = QFont()
        font14.setFamily(u"Swis721 Blk BT")
        font14.setPointSize(22)
        self.FriendsTitle.setFont(font14)

        self.verticalLayout_88.addWidget(self.FriendsTitle)

        self.FriendsNetBalance = QLabel(self.frame_67)
        self.FriendsNetBalance.setObjectName(u"FriendsNetBalance")
        self.FriendsNetBalance.setFont(font10)

        self.verticalLayout_88.addWidget(self.FriendsNetBalance)


        self.horizontalLayout_59.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.FriendsHeader)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.AddFriendsBtn = QPushButton(self.frame_68)
        self.AddFriendsBtn.setObjectName(u"AddFriendsBtn")
        icon21 = QIcon()
        icon21.addFile(u":/icons2/icons2/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AddFriendsBtn.setIcon(icon21)
        self.AddFriendsBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_60.addWidget(self.AddFriendsBtn)


        self.horizontalLayout_59.addWidget(self.frame_68, 0, Qt.AlignRight)


        self.gridLayout_7.addWidget(self.FriendsHeader, 0, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_85.addWidget(self.widget_5)

        self.scrollArea_19.setWidget(self.scrollAreaWidgetContents_20)

        self.verticalLayout_84.addWidget(self.scrollArea_19)

        self.mainPages.addWidget(self.FriendsPage)
        self.FriendPage = QWidget()
        self.FriendPage.setObjectName(u"FriendPage")
        self.verticalLayout_50 = QVBoxLayout(self.FriendPage)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.FriendFrame = QWidget(self.FriendPage)
        self.FriendFrame.setObjectName(u"FriendFrame")
        self.horizontalLayout_35 = QHBoxLayout(self.FriendFrame)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.FriendProfile = QPushButton(self.FriendFrame)
        self.FriendProfile.setObjectName(u"FriendProfile")
        icon22 = QIcon()
        icon22.addFile(u":/images/219969.png", QSize(), QIcon.Normal, QIcon.Off)
        self.FriendProfile.setIcon(icon22)
        self.FriendProfile.setIconSize(QSize(70, 70))

        self.horizontalLayout_35.addWidget(self.FriendProfile, 0, Qt.AlignLeft)

        self.FriendName = QLabel(self.FriendFrame)
        self.FriendName.setObjectName(u"FriendName")
        sizePolicy5.setHeightForWidth(self.FriendName.sizePolicy().hasHeightForWidth())
        self.FriendName.setSizePolicy(sizePolicy5)
        font15 = QFont()
        font15.setFamily(u"Swis721 Blk BT")
        font15.setPointSize(18)
        self.FriendName.setFont(font15)

        self.horizontalLayout_35.addWidget(self.FriendName)

        self.EditFriendBtn = QPushButton(self.FriendFrame)
        self.EditFriendBtn.setObjectName(u"EditFriendBtn")
        self.EditFriendBtn.setIcon(icon18)
        self.EditFriendBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_35.addWidget(self.EditFriendBtn)

        self.AddFriendExpenseBtn = QPushButton(self.FriendFrame)
        self.AddFriendExpenseBtn.setObjectName(u"AddFriendExpenseBtn")
        self.AddFriendExpenseBtn.setIcon(icon20)
        self.AddFriendExpenseBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_35.addWidget(self.AddFriendExpenseBtn)


        self.verticalLayout_50.addWidget(self.FriendFrame, 0, Qt.AlignTop)

        self.widget_4 = QWidget(self.FriendPage)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy6.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy6)
        self.verticalLayout_51 = QVBoxLayout(self.widget_4)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.ListOfExpensesTable = QLabel(self.widget_4)
        self.ListOfExpensesTable.setObjectName(u"ListOfExpensesTable")
        self.ListOfExpensesTable.setFont(font7)

        self.verticalLayout_51.addWidget(self.ListOfExpensesTable, 0, Qt.AlignTop)

        self.frame_27 = QFrame(self.widget_4)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_27)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.TableOfExpenses = QTableWidget(self.frame_27)
        if (self.TableOfExpenses.columnCount() < 8):
            self.TableOfExpenses.setColumnCount(8)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TableOfExpenses.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableOfExpenses.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TableOfExpenses.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TableOfExpenses.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TableOfExpenses.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TableOfExpenses.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.TableOfExpenses.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.TableOfExpenses.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        self.TableOfExpenses.setObjectName(u"TableOfExpenses")
        sizePolicy5.setHeightForWidth(self.TableOfExpenses.sizePolicy().hasHeightForWidth())
        self.TableOfExpenses.setSizePolicy(sizePolicy5)

        self.verticalLayout_52.addWidget(self.TableOfExpenses)


        self.verticalLayout_51.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.widget_4)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy6.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy6)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_28)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.FriendsExpenseGraphBtn = QPushButton(self.frame_28)
        self.FriendsExpenseGraphBtn.setObjectName(u"FriendsExpenseGraphBtn")
        sizePolicy8.setHeightForWidth(self.FriendsExpenseGraphBtn.sizePolicy().hasHeightForWidth())
        self.FriendsExpenseGraphBtn.setSizePolicy(sizePolicy8)
        self.FriendsExpenseGraphBtn.setMinimumSize(QSize(300, 50))
        self.FriendsExpenseGraphBtn.setMaximumSize(QSize(300, 50))
        self.FriendsExpenseGraphBtn.setFont(font2)
        icon23 = QIcon()
        icon23.addFile(u":/icons2/icons2/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.FriendsExpenseGraphBtn.setIcon(icon23)
        self.FriendsExpenseGraphBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_53.addWidget(self.FriendsExpenseGraphBtn, 0, Qt.AlignHCenter)

        self.FriendExpenseGraph = QLabel(self.frame_28)
        self.FriendExpenseGraph.setObjectName(u"FriendExpenseGraph")

        self.verticalLayout_53.addWidget(self.FriendExpenseGraph)


        self.verticalLayout_51.addWidget(self.frame_28)


        self.verticalLayout_50.addWidget(self.widget_4)

        self.mainPages.addWidget(self.FriendPage)
        self.GrpPage = QWidget()
        self.GrpPage.setObjectName(u"GrpPage")
        self.verticalLayout_31 = QVBoxLayout(self.GrpPage)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.scrollArea_2 = QScrollArea(self.GrpPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(-10, -360, 473, 1222))
        self.verticalLayout_45 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 1200))
        self.verticalLayout_32 = QVBoxLayout(self.widget_2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.GrpHeader = QWidget(self.widget_2)
        self.GrpHeader.setObjectName(u"GrpHeader")
        sizePolicy3.setHeightForWidth(self.GrpHeader.sizePolicy().hasHeightForWidth())
        self.GrpHeader.setSizePolicy(sizePolicy3)
        self.GrpHeader.setMinimumSize(QSize(0, 100))
        self.verticalLayout_33 = QVBoxLayout(self.GrpHeader)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.GrpHeaderSubContainer = QFrame(self.GrpHeader)
        self.GrpHeaderSubContainer.setObjectName(u"GrpHeaderSubContainer")
        self.GrpHeaderSubContainer.setFrameShape(QFrame.StyledPanel)
        self.GrpHeaderSubContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.GrpHeaderSubContainer)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_13 = QFrame(self.GrpHeaderSubContainer)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_13)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.GrpName = QLabel(self.frame_13)
        self.GrpName.setObjectName(u"GrpName")
        sizePolicy3.setHeightForWidth(self.GrpName.sizePolicy().hasHeightForWidth())
        self.GrpName.setSizePolicy(sizePolicy3)
        self.GrpName.setMinimumSize(QSize(0, 40))
        self.GrpName.setFont(font15)

        self.verticalLayout_38.addWidget(self.GrpName)

        self.grp_owner = QLabel(self.frame_13)
        self.grp_owner.setObjectName(u"grp_owner")
        self.grp_owner.setFont(font10)

        self.verticalLayout_38.addWidget(self.grp_owner)

        self.GrpTotalExpense = QLabel(self.frame_13)
        self.GrpTotalExpense.setObjectName(u"GrpTotalExpense")
        self.GrpTotalExpense.setFont(font10)

        self.verticalLayout_38.addWidget(self.GrpTotalExpense)


        self.horizontalLayout_25.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.GrpHeaderSubContainer)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.AddMembersBtn_7 = QPushButton(self.frame_15)
        self.AddMembersBtn_7.setObjectName(u"AddMembersBtn_7")
        self.AddMembersBtn_7.setIcon(icon21)
        self.AddMembersBtn_7.setIconSize(QSize(32, 32))

        self.horizontalLayout_26.addWidget(self.AddMembersBtn_7)

        self.AddExpensesBtn = QPushButton(self.frame_15)
        self.AddExpensesBtn.setObjectName(u"AddExpensesBtn")
        self.AddExpensesBtn.setIcon(icon20)
        self.AddExpensesBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_26.addWidget(self.AddExpensesBtn)

        self.EditGrpBtn = QPushButton(self.frame_15)
        self.EditGrpBtn.setObjectName(u"EditGrpBtn")
        self.EditGrpBtn.setIcon(icon18)
        self.EditGrpBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_26.addWidget(self.EditGrpBtn)


        self.horizontalLayout_27.addWidget(self.frame_15, 0, Qt.AlignRight)


        self.horizontalLayout_25.addWidget(self.frame_14)


        self.verticalLayout_33.addWidget(self.GrpHeaderSubContainer)


        self.verticalLayout_32.addWidget(self.GrpHeader)

        self.Tables = QWidget(self.widget_2)
        self.Tables.setObjectName(u"Tables")
        self.verticalLayout_36 = QVBoxLayout(self.Tables)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_22 = QLabel(self.Tables)
        self.label_22.setObjectName(u"label_22")
        font16 = QFont()
        font16.setFamily(u"Swis721 Blk BT")
        font16.setPointSize(13)
        self.label_22.setFont(font16)

        self.verticalLayout_36.addWidget(self.label_22)

        self.scrollArea_4 = QScrollArea(self.Tables)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 407, 214))
        self.verticalLayout_37 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents_6)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_37.addWidget(self.tableWidget)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_36.addWidget(self.scrollArea_4)

        self.label_23 = QLabel(self.Tables)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font16)

        self.verticalLayout_36.addWidget(self.label_23)

        self.scrollArea_3 = QScrollArea(self.Tables)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 407, 214))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.ExpensesTable = QTableWidget(self.scrollAreaWidgetContents_4)
        if (self.ExpensesTable.columnCount() < 8):
            self.ExpensesTable.setColumnCount(8)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.ExpensesTable.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ExpensesTable.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.ExpensesTable.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font1);
        self.ExpensesTable.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font1);
        __qtablewidgetitem16.setBackground(QColor(255, 255, 255));
        self.ExpensesTable.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.ExpensesTable.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.ExpensesTable.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font1);
        __qtablewidgetitem19.setBackground(QColor(0, 0, 0, 180));
        __qtablewidgetitem19.setForeground(brush);
        self.ExpensesTable.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        self.ExpensesTable.setObjectName(u"ExpensesTable")
        sizePolicy.setHeightForWidth(self.ExpensesTable.sizePolicy().hasHeightForWidth())
        self.ExpensesTable.setSizePolicy(sizePolicy)

        self.verticalLayout_35.addWidget(self.ExpensesTable)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_36.addWidget(self.scrollArea_3)


        self.verticalLayout_32.addWidget(self.Tables)

        self.Graphs = QWidget(self.widget_2)
        self.Graphs.setObjectName(u"Graphs")
        sizePolicy6.setHeightForWidth(self.Graphs.sizePolicy().hasHeightForWidth())
        self.Graphs.setSizePolicy(sizePolicy6)
        self.verticalLayout_46 = QVBoxLayout(self.Graphs)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_18 = QFrame(self.Graphs)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFont(font7)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.ExpenseGraphBtn = QPushButton(self.frame_18)
        self.ExpenseGraphBtn.setObjectName(u"ExpenseGraphBtn")
        self.ExpenseGraphBtn.setFont(font2)
        self.ExpenseGraphBtn.setIcon(icon23)
        self.ExpenseGraphBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_24.addWidget(self.ExpenseGraphBtn)

        self.DebtGraphBtn = QPushButton(self.frame_18)
        self.DebtGraphBtn.setObjectName(u"DebtGraphBtn")
        self.DebtGraphBtn.setFont(font2)
        icon24 = QIcon()
        icon24.addFile(u":/icons2/icons2/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.DebtGraphBtn.setIcon(icon24)
        self.DebtGraphBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_24.addWidget(self.DebtGraphBtn)


        self.verticalLayout_46.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_19 = QFrame(self.Graphs)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy6.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy6)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_19)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.closeGraphBtn = QPushButton(self.frame_20)
        self.closeGraphBtn.setObjectName(u"closeGraphBtn")
        self.closeGraphBtn.setIcon(icon6)
        self.closeGraphBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.closeGraphBtn, 0, Qt.AlignRight)


        self.verticalLayout_47.addWidget(self.frame_20, 0, Qt.AlignTop)

        self.frame_25 = QFrame(self.frame_19)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy6.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy6)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_25)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.GraphTitle = QLabel(self.frame_25)
        self.GraphTitle.setObjectName(u"GraphTitle")
        self.GraphTitle.setFont(font9)

        self.verticalLayout_82.addWidget(self.GraphTitle, 0, Qt.AlignTop)

        self.Graph = QLabel(self.frame_25)
        self.Graph.setObjectName(u"Graph")
        sizePolicy6.setHeightForWidth(self.Graph.sizePolicy().hasHeightForWidth())
        self.Graph.setSizePolicy(sizePolicy6)

        self.verticalLayout_82.addWidget(self.Graph)


        self.verticalLayout_47.addWidget(self.frame_25)


        self.verticalLayout_46.addWidget(self.frame_19)


        self.verticalLayout_32.addWidget(self.Graphs)


        self.verticalLayout_45.addWidget(self.widget_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_31.addWidget(self.scrollArea_2)

        self.mainPages.addWidget(self.GrpPage)

        self.verticalLayout_14.addWidget(self.mainPages)


        self.horizontalLayout_9.addWidget(self.mainContentContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(450, 0))
        self.verticalLayout_10 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.CloseRightMenuBtn = QPushButton(self.frame_8)
        self.CloseRightMenuBtn.setObjectName(u"CloseRightMenuBtn")
        self.CloseRightMenuBtn.setIcon(icon6)
        self.CloseRightMenuBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.CloseRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        sizePolicy6.setHeightForWidth(self.rightMenuPages.sizePolicy().hasHeightForWidth())
        self.rightMenuPages.setSizePolicy(sizePolicy6)
        self.AddNewMemberPage = QWidget()
        self.AddNewMemberPage.setObjectName(u"AddNewMemberPage")
        self.verticalLayout_12 = QVBoxLayout(self.AddNewMemberPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_17 = QScrollArea(self.AddNewMemberPage)
        self.scrollArea_17.setObjectName(u"scrollArea_17")
        self.scrollArea_17.setWidgetResizable(True)
        self.scrollAreaWidgetContents_18 = QWidget()
        self.scrollAreaWidgetContents_18.setObjectName(u"scrollAreaWidgetContents_18")
        self.scrollAreaWidgetContents_18.setGeometry(QRect(0, 0, 434, 767))
        self.horizontalLayout_56 = QHBoxLayout(self.scrollAreaWidgetContents_18)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.AddNewMemberBox = QGroupBox(self.scrollAreaWidgetContents_18)
        self.AddNewMemberBox.setObjectName(u"AddNewMemberBox")
        sizePolicy.setHeightForWidth(self.AddNewMemberBox.sizePolicy().hasHeightForWidth())
        self.AddNewMemberBox.setSizePolicy(sizePolicy)
        self.AddNewMemberBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_83 = QVBoxLayout(self.AddNewMemberBox)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.NewMemberLabel = QLabel(self.AddNewMemberBox)
        self.NewMemberLabel.setObjectName(u"NewMemberLabel")
        self.NewMemberLabel.setFont(font1)

        self.verticalLayout_83.addWidget(self.NewMemberLabel)

        self.ErrorLabel3 = QTextBrowser(self.AddNewMemberBox)
        self.ErrorLabel3.setObjectName(u"ErrorLabel3")
        self.ErrorLabel3.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.ErrorLabel3.sizePolicy().hasHeightForWidth())
        self.ErrorLabel3.setSizePolicy(sizePolicy4)
        self.ErrorLabel3.setMaximumSize(QSize(16777215, 16777152))
        self.ErrorLabel3.viewport().setProperty("cursor", QCursor(Qt.BusyCursor))
        self.ErrorLabel3.setToolTipDuration(-5)
        self.ErrorLabel3.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_83.addWidget(self.ErrorLabel3)

        self.NewMemberInput = QLineEdit(self.AddNewMemberBox)
        self.NewMemberInput.setObjectName(u"NewMemberInput")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.NewMemberInput.sizePolicy().hasHeightForWidth())
        self.NewMemberInput.setSizePolicy(sizePolicy10)
        self.NewMemberInput.setMinimumSize(QSize(0, 37))
        self.NewMemberInput.setMaximumSize(QSize(16777215, 59))

        self.verticalLayout_83.addWidget(self.NewMemberInput)

        self.ExpensesLabel = QLabel(self.AddNewMemberBox)
        self.ExpensesLabel.setObjectName(u"ExpensesLabel")
        self.ExpensesLabel.setFont(font1)

        self.verticalLayout_83.addWidget(self.ExpensesLabel)

        self.ExpensesInput = QScrollArea(self.AddNewMemberBox)
        self.ExpensesInput.setObjectName(u"ExpensesInput")
        self.ExpensesInput.setWidgetResizable(True)
        self.scrollAreaWidgetContents_19 = QWidget()
        self.scrollAreaWidgetContents_19.setObjectName(u"scrollAreaWidgetContents_19")
        self.scrollAreaWidgetContents_19.setGeometry(QRect(0, 0, 390, 312))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_19)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents_19)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_5.addWidget(self.checkBox_5, 2, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.scrollAreaWidgetContents_19)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_5.addWidget(self.checkBox_6, 1, 1, 1, 1)

        self.checkBox_7 = QCheckBox(self.scrollAreaWidgetContents_19)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_5.addWidget(self.checkBox_7, 1, 2, 1, 1)

        self.checkBox_8 = QCheckBox(self.scrollAreaWidgetContents_19)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_5.addWidget(self.checkBox_8, 2, 2, 1, 1)

        self.ExpensesInput.setWidget(self.scrollAreaWidgetContents_19)

        self.verticalLayout_83.addWidget(self.ExpensesInput)

        self.FinalAddMemberBtn = QPushButton(self.AddNewMemberBox)
        self.FinalAddMemberBtn.setObjectName(u"FinalAddMemberBtn")
        self.FinalAddMemberBtn.setFont(font1)
        self.FinalAddMemberBtn.setIcon(icon21)
        self.FinalAddMemberBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_83.addWidget(self.FinalAddMemberBtn)


        self.horizontalLayout_56.addWidget(self.AddNewMemberBox)

        self.scrollArea_17.setWidget(self.scrollAreaWidgetContents_18)

        self.verticalLayout_12.addWidget(self.scrollArea_17)

        self.rightMenuPages.addWidget(self.AddNewMemberPage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.rightMenuPages.addWidget(self.page)
        self.AddNewFriendPage = QWidget()
        self.AddNewFriendPage.setObjectName(u"AddNewFriendPage")
        self.verticalLayout_48 = QVBoxLayout(self.AddNewFriendPage)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.scrollArea_5 = QScrollArea(self.AddNewFriendPage)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 414, 767))
        self.horizontalLayout_33 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.AddNewFriendBox = QGroupBox(self.scrollAreaWidgetContents_2)
        self.AddNewFriendBox.setObjectName(u"AddNewFriendBox")
        self.verticalLayout_49 = QVBoxLayout(self.AddNewFriendBox)
        self.verticalLayout_49.setSpacing(18)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.NameLabel = QLabel(self.AddNewFriendBox)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setFont(font2)

        self.verticalLayout_49.addWidget(self.NameLabel, 0, Qt.AlignTop)

        self.NameInput = QLineEdit(self.AddNewFriendBox)
        self.NameInput.setObjectName(u"NameInput")

        self.verticalLayout_49.addWidget(self.NameInput, 0, Qt.AlignTop)

        self.EmailLabel = QLabel(self.AddNewFriendBox)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setFont(font2)

        self.verticalLayout_49.addWidget(self.EmailLabel)

        self.EmaiIInput = QLineEdit(self.AddNewFriendBox)
        self.EmaiIInput.setObjectName(u"EmaiIInput")

        self.verticalLayout_49.addWidget(self.EmaiIInput)

        self.verticalSpacer_2 = QSpacerItem(10, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_49.addItem(self.verticalSpacer_2)

        self.ProfileLabel = QLabel(self.AddNewFriendBox)
        self.ProfileLabel.setObjectName(u"ProfileLabel")
        self.ProfileLabel.setFont(font2)

        self.verticalLayout_49.addWidget(self.ProfileLabel)

        self.frame_26 = QFrame(self.AddNewFriendBox)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy6.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy6)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.LadyProfileBtn = QPushButton(self.frame_26)
        self.LadyProfileBtn.setObjectName(u"LadyProfileBtn")
        self.LadyProfileBtn.setIcon(icon22)
        self.LadyProfileBtn.setIconSize(QSize(70, 70))

        self.horizontalLayout_34.addWidget(self.LadyProfileBtn, 0, Qt.AlignTop)

        self.MaleProfileBtn = QPushButton(self.frame_26)
        self.MaleProfileBtn.setObjectName(u"MaleProfileBtn")
        icon25 = QIcon()
        icon25.addFile(u":/images/219986.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MaleProfileBtn.setIcon(icon25)
        self.MaleProfileBtn.setIconSize(QSize(70, 70))

        self.horizontalLayout_34.addWidget(self.MaleProfileBtn, 0, Qt.AlignTop)


        self.verticalLayout_49.addWidget(self.frame_26)

        self.AddFriendBtn = QPushButton(self.AddNewFriendBox)
        self.AddFriendBtn.setObjectName(u"AddFriendBtn")
        self.AddFriendBtn.setFont(font2)
        self.AddFriendBtn.setIcon(icon21)
        self.AddFriendBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_49.addWidget(self.AddFriendBtn)


        self.horizontalLayout_33.addWidget(self.AddNewFriendBox)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_48.addWidget(self.scrollArea_5)

        self.rightMenuPages.addWidget(self.AddNewFriendPage)
        self.AddGrpPage = QWidget()
        self.AddGrpPage.setObjectName(u"AddGrpPage")
        self.verticalLayout_34 = QVBoxLayout(self.AddGrpPage)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.groupBox_10 = QGroupBox(self.AddGrpPage)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy11)
        self.groupBox_10.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_30.setSpacing(23)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.GrpNameLabel = QLabel(self.groupBox_10)
        self.GrpNameLabel.setObjectName(u"GrpNameLabel")
        self.GrpNameLabel.setFont(font1)

        self.verticalLayout_30.addWidget(self.GrpNameLabel)

        self.GrpNameInput = QLineEdit(self.groupBox_10)
        self.GrpNameInput.setObjectName(u"GrpNameInput")
        sizePolicy.setHeightForWidth(self.GrpNameInput.sizePolicy().hasHeightForWidth())
        self.GrpNameInput.setSizePolicy(sizePolicy)
        self.GrpNameInput.setMinimumSize(QSize(0, 37))
        self.GrpNameInput.setMaximumSize(QSize(16777215, 59))
        self.GrpNameInput.setFont(font1)

        self.verticalLayout_30.addWidget(self.GrpNameInput, 0, Qt.AlignVCenter)

        self.NoMembersLabel = QLabel(self.groupBox_10)
        self.NoMembersLabel.setObjectName(u"NoMembersLabel")
        self.NoMembersLabel.setFont(font1)

        self.verticalLayout_30.addWidget(self.NoMembersLabel)

        self.NoMembersInput = QSpinBox(self.groupBox_10)
        self.NoMembersInput.setObjectName(u"NoMembersInput")

        self.verticalLayout_30.addWidget(self.NoMembersInput)

        self.GrpMembersLabel = QLabel(self.groupBox_10)
        self.GrpMembersLabel.setObjectName(u"GrpMembersLabel")
        self.GrpMembersLabel.setFont(font1)

        self.verticalLayout_30.addWidget(self.GrpMembersLabel)

        self.GrpMembersInput = QTextEdit(self.groupBox_10)
        self.GrpMembersInput.setObjectName(u"GrpMembersInput")
        self.GrpMembersInput.setFont(font1)

        self.verticalLayout_30.addWidget(self.GrpMembersInput)

        self.DefaultSplitLabel = QLabel(self.groupBox_10)
        self.DefaultSplitLabel.setObjectName(u"DefaultSplitLabel")
        self.DefaultSplitLabel.setFont(font1)

        self.verticalLayout_30.addWidget(self.DefaultSplitLabel)

        self.Equal = QRadioButton(self.groupBox_10)
        self.Equal.setObjectName(u"Equal")
        self.Equal.setFont(font3)

        self.verticalLayout_30.addWidget(self.Equal)

        self.share = QRadioButton(self.groupBox_10)
        self.share.setObjectName(u"share")
        self.share.setFont(font3)

        self.verticalLayout_30.addWidget(self.share)

        self.percentage = QRadioButton(self.groupBox_10)
        self.percentage.setObjectName(u"percentage")
        self.percentage.setFont(font3)

        self.verticalLayout_30.addWidget(self.percentage)

        self.frame_47 = QFrame(self.groupBox_10)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_47)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.scrollArea_11 = QScrollArea(self.frame_47)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 390, 85))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_26.addWidget(self.scrollArea_11)

        self.ErrorLabel = QTextBrowser(self.frame_47)
        self.ErrorLabel.setObjectName(u"ErrorLabel")
        sizePolicy4.setHeightForWidth(self.ErrorLabel.sizePolicy().hasHeightForWidth())
        self.ErrorLabel.setSizePolicy(sizePolicy4)
        self.ErrorLabel.setFont(font10)
        self.ErrorLabel.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_26.addWidget(self.ErrorLabel)


        self.verticalLayout_30.addWidget(self.frame_47)

        self.FinalAddGrpBtn = QPushButton(self.groupBox_10)
        self.FinalAddGrpBtn.setObjectName(u"FinalAddGrpBtn")
        self.FinalAddGrpBtn.setFont(font1)
        icon26 = QIcon()
        icon26.addFile(u":/icons2/icons2/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.FinalAddGrpBtn.setIcon(icon26)
        self.FinalAddGrpBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_30.addWidget(self.FinalAddGrpBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_34.addWidget(self.groupBox_10)

        self.rightMenuPages.addWidget(self.AddGrpPage)
        self.AddRecurrentExpense = QWidget()
        self.AddRecurrentExpense.setObjectName(u"AddRecurrentExpense")
        self.verticalLayout_91 = QVBoxLayout(self.AddRecurrentExpense)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.AddExpenseBox_4 = QGroupBox(self.AddRecurrentExpense)
        self.AddExpenseBox_4.setObjectName(u"AddExpenseBox_4")
        sizePolicy.setHeightForWidth(self.AddExpenseBox_4.sizePolicy().hasHeightForWidth())
        self.AddExpenseBox_4.setSizePolicy(sizePolicy)
        self.AddExpenseBox_4.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_75 = QVBoxLayout(self.AddExpenseBox_4)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.LabelLabel = QLabel(self.AddExpenseBox_4)
        self.LabelLabel.setObjectName(u"LabelLabel")
        self.LabelLabel.setFont(font1)

        self.verticalLayout_75.addWidget(self.LabelLabel)

        self.LabelInput = QLineEdit(self.AddExpenseBox_4)
        self.LabelInput.setObjectName(u"LabelInput")
        sizePolicy.setHeightForWidth(self.LabelInput.sizePolicy().hasHeightForWidth())
        self.LabelInput.setSizePolicy(sizePolicy)
        self.LabelInput.setMinimumSize(QSize(0, 37))
        self.LabelInput.setMaximumSize(QSize(16777215, 59))

        self.verticalLayout_75.addWidget(self.LabelInput)

        self.AmountRExpenseLabel = QLabel(self.AddExpenseBox_4)
        self.AmountRExpenseLabel.setObjectName(u"AmountRExpenseLabel")
        self.AmountRExpenseLabel.setFont(font1)

        self.verticalLayout_75.addWidget(self.AmountRExpenseLabel)

        self.AmountRExpenseInput = QLineEdit(self.AddExpenseBox_4)
        self.AmountRExpenseInput.setObjectName(u"AmountRExpenseInput")
        sizePolicy.setHeightForWidth(self.AmountRExpenseInput.sizePolicy().hasHeightForWidth())
        self.AmountRExpenseInput.setSizePolicy(sizePolicy)
        self.AmountRExpenseInput.setMinimumSize(QSize(0, 37))
        self.AmountRExpenseInput.setMaximumSize(QSize(16777215, 59))

        self.verticalLayout_75.addWidget(self.AmountRExpenseInput)

        self.DaysLabel = QLabel(self.AddExpenseBox_4)
        self.DaysLabel.setObjectName(u"DaysLabel")
        self.DaysLabel.setFont(font1)

        self.verticalLayout_75.addWidget(self.DaysLabel)

        self.DaysOfExpense = QScrollArea(self.AddExpenseBox_4)
        self.DaysOfExpense.setObjectName(u"DaysOfExpense")
        self.DaysOfExpense.setWidgetResizable(True)
        self.scrollAreaWidgetContents_16 = QWidget()
        self.scrollAreaWidgetContents_16.setObjectName(u"scrollAreaWidgetContents_16")
        self.scrollAreaWidgetContents_16.setGeometry(QRect(0, 0, 412, 241))
        self.gridLayout_16 = QGridLayout(self.scrollAreaWidgetContents_16)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.day27 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day27.setObjectName(u"day27")
        font17 = QFont()
        font17.setFamily(u"Swis721 BlkEx BT")
        self.day27.setFont(font17)

        self.gridLayout_16.addWidget(self.day27, 4, 5, 1, 1)

        self.day28 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day28.setObjectName(u"day28")
        self.day28.setFont(font17)

        self.gridLayout_16.addWidget(self.day28, 4, 6, 1, 1)

        self.day1 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day1.setObjectName(u"day1")
        self.day1.setFont(font17)

        self.gridLayout_16.addWidget(self.day1, 0, 0, 1, 1)

        self.day1_2 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day1_2.setObjectName(u"day1_2")
        self.day1_2.setFont(font17)

        self.gridLayout_16.addWidget(self.day1_2, 0, 1, 1, 1)

        self.day10 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day10.setObjectName(u"day10")
        self.day10.setFont(font17)

        self.gridLayout_16.addWidget(self.day10, 2, 2, 1, 1)

        self.day9 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day9.setObjectName(u"day9")
        self.day9.setFont(font17)

        self.gridLayout_16.addWidget(self.day9, 2, 1, 1, 1)

        self.day6 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day6.setObjectName(u"day6")
        self.day6.setFont(font17)

        self.gridLayout_16.addWidget(self.day6, 0, 5, 1, 1)

        self.day3 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day3.setObjectName(u"day3")
        self.day3.setFont(font17)

        self.gridLayout_16.addWidget(self.day3, 0, 2, 1, 1)

        self.day4 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day4.setObjectName(u"day4")
        self.day4.setFont(font17)

        self.gridLayout_16.addWidget(self.day4, 0, 3, 1, 1)

        self.day5 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day5.setObjectName(u"day5")
        self.day5.setFont(font17)

        self.gridLayout_16.addWidget(self.day5, 0, 4, 1, 1)

        self.day16 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day16.setObjectName(u"day16")
        self.day16.setFont(font17)

        self.gridLayout_16.addWidget(self.day16, 3, 1, 1, 1)

        self.day18 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day18.setObjectName(u"day18")
        self.day18.setFont(font17)

        self.gridLayout_16.addWidget(self.day18, 3, 3, 1, 1)

        self.day17 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day17.setObjectName(u"day17")
        self.day17.setFont(font17)

        self.gridLayout_16.addWidget(self.day17, 3, 2, 1, 1)

        self.day20 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day20.setObjectName(u"day20")
        self.day20.setFont(font17)

        self.gridLayout_16.addWidget(self.day20, 3, 5, 1, 1)

        self.day19 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day19.setObjectName(u"day19")
        self.day19.setFont(font17)

        self.gridLayout_16.addWidget(self.day19, 3, 4, 1, 1)

        self.day22 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day22.setObjectName(u"day22")
        self.day22.setFont(font17)

        self.gridLayout_16.addWidget(self.day22, 4, 0, 1, 1)

        self.day21 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day21.setObjectName(u"day21")
        self.day21.setFont(font17)

        self.gridLayout_16.addWidget(self.day21, 3, 6, 1, 1)

        self.day24 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day24.setObjectName(u"day24")
        self.day24.setFont(font17)

        self.gridLayout_16.addWidget(self.day24, 4, 2, 1, 1)

        self.day25 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day25.setObjectName(u"day25")
        self.day25.setFont(font17)

        self.gridLayout_16.addWidget(self.day25, 4, 3, 1, 1)

        self.day26 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day26.setObjectName(u"day26")
        self.day26.setFont(font17)

        self.gridLayout_16.addWidget(self.day26, 4, 4, 1, 1)

        self.day7 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day7.setObjectName(u"day7")
        self.day7.setFont(font17)

        self.gridLayout_16.addWidget(self.day7, 0, 6, 1, 1)

        self.day14 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day14.setObjectName(u"day14")
        self.day14.setFont(font17)

        self.gridLayout_16.addWidget(self.day14, 2, 6, 1, 1)

        self.day8 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day8.setObjectName(u"day8")
        self.day8.setFont(font17)

        self.gridLayout_16.addWidget(self.day8, 2, 0, 1, 1)

        self.day11 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day11.setObjectName(u"day11")
        self.day11.setFont(font17)

        self.gridLayout_16.addWidget(self.day11, 2, 3, 1, 1)

        self.day12 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day12.setObjectName(u"day12")
        self.day12.setFont(font17)

        self.gridLayout_16.addWidget(self.day12, 2, 4, 1, 1)

        self.day15 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day15.setObjectName(u"day15")
        self.day15.setFont(font17)

        self.gridLayout_16.addWidget(self.day15, 3, 0, 1, 1)

        self.day13 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day13.setObjectName(u"day13")
        self.day13.setFont(font17)

        self.gridLayout_16.addWidget(self.day13, 2, 5, 1, 1)

        self.day23 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day23.setObjectName(u"day23")
        self.day23.setFont(font17)

        self.gridLayout_16.addWidget(self.day23, 4, 1, 1, 1)

        self.day29 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day29.setObjectName(u"day29")
        self.day29.setFont(font17)

        self.gridLayout_16.addWidget(self.day29, 5, 0, 1, 1)

        self.day30 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day30.setObjectName(u"day30")
        self.day30.setFont(font17)

        self.gridLayout_16.addWidget(self.day30, 5, 1, 1, 1)

        self.day31 = QCheckBox(self.scrollAreaWidgetContents_16)
        self.day31.setObjectName(u"day31")
        self.day31.setFont(font17)

        self.gridLayout_16.addWidget(self.day31, 5, 2, 1, 1)

        self.DaysOfExpense.setWidget(self.scrollAreaWidgetContents_16)

        self.verticalLayout_75.addWidget(self.DaysOfExpense)

        self.DateInput_5 = QWidget(self.AddExpenseBox_4)
        self.DateInput_5.setObjectName(u"DateInput_5")
        self.horizontalLayout_54 = QHBoxLayout(self.DateInput_5)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")

        self.verticalLayout_75.addWidget(self.DateInput_5)

        self.CategoryLabel_5 = QLabel(self.AddExpenseBox_4)
        self.CategoryLabel_5.setObjectName(u"CategoryLabel_5")
        self.CategoryLabel_5.setFont(font1)

        self.verticalLayout_75.addWidget(self.CategoryLabel_5)

        self.CategoryGrid_5 = QFrame(self.AddExpenseBox_4)
        self.CategoryGrid_5.setObjectName(u"CategoryGrid_5")
        sizePolicy6.setHeightForWidth(self.CategoryGrid_5.sizePolicy().hasHeightForWidth())
        self.CategoryGrid_5.setSizePolicy(sizePolicy6)
        self.CategoryGrid_5.setFrameShape(QFrame.StyledPanel)
        self.CategoryGrid_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.CategoryGrid_5)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.radioButton_25 = QRadioButton(self.CategoryGrid_5)
        self.radioButton_25.setObjectName(u"radioButton_25")
        self.radioButton_25.setFont(font3)

        self.gridLayout_17.addWidget(self.radioButton_25, 0, 1, 1, 1)

        self.radioButton_26 = QRadioButton(self.CategoryGrid_5)
        self.radioButton_26.setObjectName(u"radioButton_26")
        self.radioButton_26.setFont(font3)

        self.gridLayout_17.addWidget(self.radioButton_26, 1, 1, 1, 1)

        self.radioButton_27 = QRadioButton(self.CategoryGrid_5)
        self.radioButton_27.setObjectName(u"radioButton_27")
        self.radioButton_27.setFont(font3)

        self.gridLayout_17.addWidget(self.radioButton_27, 1, 2, 1, 1)

        self.radioButton_28 = QRadioButton(self.CategoryGrid_5)
        self.radioButton_28.setObjectName(u"radioButton_28")
        self.radioButton_28.setFont(font3)

        self.gridLayout_17.addWidget(self.radioButton_28, 0, 2, 1, 1)

        self.radioButton_29 = QRadioButton(self.CategoryGrid_5)
        self.radioButton_29.setObjectName(u"radioButton_29")
        self.radioButton_29.setFont(font3)

        self.gridLayout_17.addWidget(self.radioButton_29, 1, 0, 1, 1)

        self.radioButton_30 = QRadioButton(self.CategoryGrid_5)
        self.radioButton_30.setObjectName(u"radioButton_30")
        self.radioButton_30.setFont(font3)

        self.gridLayout_17.addWidget(self.radioButton_30, 0, 0, 1, 1)


        self.verticalLayout_75.addWidget(self.CategoryGrid_5)

        self.FinalAddRecurrentExpenseBtn = QPushButton(self.AddExpenseBox_4)
        self.FinalAddRecurrentExpenseBtn.setObjectName(u"FinalAddRecurrentExpenseBtn")
        self.FinalAddRecurrentExpenseBtn.setFont(font1)
        self.FinalAddRecurrentExpenseBtn.setIcon(icon26)
        self.FinalAddRecurrentExpenseBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_75.addWidget(self.FinalAddRecurrentExpenseBtn)


        self.verticalLayout_91.addWidget(self.AddExpenseBox_4)

        self.rightMenuPages.addWidget(self.AddRecurrentExpense)
        self.AddExpensePage = QWidget()
        self.AddExpensePage.setObjectName(u"AddExpensePage")
        self.verticalLayout_44 = QVBoxLayout(self.AddExpensePage)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.scrollArea_6 = QScrollArea(self.AddExpensePage)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 480, 1277))
        self.horizontalLayout_23 = QHBoxLayout(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.AddExpenseBox = QGroupBox(self.scrollAreaWidgetContents_8)
        self.AddExpenseBox.setObjectName(u"AddExpenseBox")
        sizePolicy.setHeightForWidth(self.AddExpenseBox.sizePolicy().hasHeightForWidth())
        self.AddExpenseBox.setSizePolicy(sizePolicy)
        self.AddExpenseBox.setMaximumSize(QSize(16777215, 16777215))
        self.AddExpenseBox.setFont(font1)
        self.verticalLayout_43 = QVBoxLayout(self.AddExpenseBox)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.GrpExpenseLabelLabel = QLabel(self.AddExpenseBox)
        self.GrpExpenseLabelLabel.setObjectName(u"GrpExpenseLabelLabel")
        self.GrpExpenseLabelLabel.setFont(font1)

        self.verticalLayout_43.addWidget(self.GrpExpenseLabelLabel)

        self.GrpExpenseLabelInput = QLineEdit(self.AddExpenseBox)
        self.GrpExpenseLabelInput.setObjectName(u"GrpExpenseLabelInput")
        sizePolicy.setHeightForWidth(self.GrpExpenseLabelInput.sizePolicy().hasHeightForWidth())
        self.GrpExpenseLabelInput.setSizePolicy(sizePolicy)
        self.GrpExpenseLabelInput.setMinimumSize(QSize(0, 37))
        self.GrpExpenseLabelInput.setFont(font1)

        self.verticalLayout_43.addWidget(self.GrpExpenseLabelInput)

        self.AmountLabel = QLabel(self.AddExpenseBox)
        self.AmountLabel.setObjectName(u"AmountLabel")
        self.AmountLabel.setFont(font1)

        self.verticalLayout_43.addWidget(self.AmountLabel)

        self.AmountInput = QLineEdit(self.AddExpenseBox)
        self.AmountInput.setObjectName(u"AmountInput")
        sizePolicy.setHeightForWidth(self.AmountInput.sizePolicy().hasHeightForWidth())
        self.AmountInput.setSizePolicy(sizePolicy)
        self.AmountInput.setMinimumSize(QSize(0, 37))
        self.AmountInput.setMaximumSize(QSize(16777215, 59))
        self.AmountInput.setFont(font1)

        self.verticalLayout_43.addWidget(self.AmountInput)

        self.PayerLabel = QLabel(self.AddExpenseBox)
        self.PayerLabel.setObjectName(u"PayerLabel")
        self.PayerLabel.setFont(font1)

        self.verticalLayout_43.addWidget(self.PayerLabel)

        self.PayerInput = QLineEdit(self.AddExpenseBox)
        self.PayerInput.setObjectName(u"PayerInput")
        sizePolicy.setHeightForWidth(self.PayerInput.sizePolicy().hasHeightForWidth())
        self.PayerInput.setSizePolicy(sizePolicy)
        self.PayerInput.setMinimumSize(QSize(0, 37))
        self.PayerInput.setMaximumSize(QSize(16777215, 59))
        self.PayerInput.setFont(font1)

        self.verticalLayout_43.addWidget(self.PayerInput)

        self.ContributersLabel = QLabel(self.AddExpenseBox)
        self.ContributersLabel.setObjectName(u"ContributersLabel")
        self.ContributersLabel.setFont(font1)

        self.verticalLayout_43.addWidget(self.ContributersLabel)

        self.ContributersInput = QScrollArea(self.AddExpenseBox)
        self.ContributersInput.setObjectName(u"ContributersInput")
        self.ContributersInput.setFont(font1)
        self.ContributersInput.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 436, 85))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.ContributersInput.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_43.addWidget(self.ContributersInput)

        self.DateLabel = QLabel(self.AddExpenseBox)
        self.DateLabel.setObjectName(u"DateLabel")
        self.DateLabel.setFont(font1)

        self.verticalLayout_43.addWidget(self.DateLabel)

        self.DateInput = QWidget(self.AddExpenseBox)
        self.DateInput.setObjectName(u"DateInput")
        self.horizontalLayout_30 = QHBoxLayout(self.DateInput)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_16 = QFrame(self.DateInput)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.calendarWidget = QCalendarWidget(self.frame_16)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.horizontalLayout_31.addWidget(self.calendarWidget)


        self.horizontalLayout_30.addWidget(self.frame_16)


        self.verticalLayout_43.addWidget(self.DateInput)

        self.CategoryLabel = QLabel(self.AddExpenseBox)
        self.CategoryLabel.setObjectName(u"CategoryLabel")
        self.CategoryLabel.setFont(font1)

        self.verticalLayout_43.addWidget(self.CategoryLabel)

        self.CategoryGrid = QFrame(self.AddExpenseBox)
        self.CategoryGrid.setObjectName(u"CategoryGrid")
        sizePolicy6.setHeightForWidth(self.CategoryGrid.sizePolicy().hasHeightForWidth())
        self.CategoryGrid.setSizePolicy(sizePolicy6)
        self.CategoryGrid.setFrameShape(QFrame.StyledPanel)
        self.CategoryGrid.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.CategoryGrid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_2 = QRadioButton(self.CategoryGrid)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font3)

        self.gridLayout_2.addWidget(self.radioButton_2, 0, 1, 1, 1)

        self.radioButton_5 = QRadioButton(self.CategoryGrid)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setFont(font3)

        self.gridLayout_2.addWidget(self.radioButton_5, 1, 1, 1, 1)

        self.radioButton_6 = QRadioButton(self.CategoryGrid)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setFont(font3)

        self.gridLayout_2.addWidget(self.radioButton_6, 1, 2, 1, 1)

        self.radioButton_3 = QRadioButton(self.CategoryGrid)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font3)

        self.gridLayout_2.addWidget(self.radioButton_3, 0, 2, 1, 1)

        self.radioButton_4 = QRadioButton(self.CategoryGrid)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font3)

        self.gridLayout_2.addWidget(self.radioButton_4, 1, 0, 1, 1)

        self.radioButton = QRadioButton(self.CategoryGrid)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font3)

        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)


        self.verticalLayout_43.addWidget(self.CategoryGrid)

        self.SplitLabel = QLabel(self.AddExpenseBox)
        self.SplitLabel.setObjectName(u"SplitLabel")
        self.SplitLabel.setFont(font1)

        self.verticalLayout_43.addWidget(self.SplitLabel)

        self.frame_29 = QFrame(self.AddExpenseBox)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_29)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.radioButton_10 = QRadioButton(self.frame_29)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setFont(font3)

        self.verticalLayout_22.addWidget(self.radioButton_10)

        self.radioButton_7 = QRadioButton(self.frame_29)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setFont(font3)

        self.verticalLayout_22.addWidget(self.radioButton_7)

        self.ShareSplit = QRadioButton(self.frame_29)
        self.ShareSplit.setObjectName(u"ShareSplit")
        self.ShareSplit.setFont(font3)

        self.verticalLayout_22.addWidget(self.ShareSplit)

        self.PercentageSplit = QRadioButton(self.frame_29)
        self.PercentageSplit.setObjectName(u"PercentageSplit")
        self.PercentageSplit.setFont(font3)

        self.verticalLayout_22.addWidget(self.PercentageSplit)


        self.verticalLayout_43.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.AddExpenseBox)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_30)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.scrollArea_10 = QScrollArea(self.frame_30)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 414, 85))
        self.verticalLayout_25 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_24.addWidget(self.scrollArea_10)


        self.verticalLayout_43.addWidget(self.frame_30)

        self.DiscriptionLabel = QLabel(self.AddExpenseBox)
        self.DiscriptionLabel.setObjectName(u"DiscriptionLabel")
        self.DiscriptionLabel.setFont(font1)

        self.verticalLayout_43.addWidget(self.DiscriptionLabel)

        self.DiscriptionInput = QTextEdit(self.AddExpenseBox)
        self.DiscriptionInput.setObjectName(u"DiscriptionInput")
        self.DiscriptionInput.setFont(font1)

        self.verticalLayout_43.addWidget(self.DiscriptionInput)

        self.ErrorLabel2 = QTextBrowser(self.AddExpenseBox)
        self.ErrorLabel2.setObjectName(u"ErrorLabel2")
        sizePolicy4.setHeightForWidth(self.ErrorLabel2.sizePolicy().hasHeightForWidth())
        self.ErrorLabel2.setSizePolicy(sizePolicy4)
        self.ErrorLabel2.setFont(font10)

        self.verticalLayout_43.addWidget(self.ErrorLabel2)

        self.FinalAddExpenseBtn = QPushButton(self.AddExpenseBox)
        self.FinalAddExpenseBtn.setObjectName(u"FinalAddExpenseBtn")
        self.FinalAddExpenseBtn.setFont(font1)
        self.FinalAddExpenseBtn.setIcon(icon26)
        self.FinalAddExpenseBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_43.addWidget(self.FinalAddExpenseBtn)


        self.horizontalLayout_23.addWidget(self.AddExpenseBox)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_44.addWidget(self.scrollArea_6)

        self.rightMenuPages.addWidget(self.AddExpensePage)
        self.AddFriendExpensePage = QWidget()
        self.AddFriendExpensePage.setObjectName(u"AddFriendExpensePage")
        self.verticalLayout_57 = QVBoxLayout(self.AddFriendExpensePage)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.scrollArea_7 = QScrollArea(self.AddFriendExpensePage)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 480, 857))
        self.horizontalLayout_41 = QHBoxLayout(self.scrollAreaWidgetContents_13)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.AddFriendExpenseBox = QGroupBox(self.scrollAreaWidgetContents_13)
        self.AddFriendExpenseBox.setObjectName(u"AddFriendExpenseBox")
        sizePolicy.setHeightForWidth(self.AddFriendExpenseBox.sizePolicy().hasHeightForWidth())
        self.AddFriendExpenseBox.setSizePolicy(sizePolicy)
        self.AddFriendExpenseBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_56 = QVBoxLayout(self.AddFriendExpenseBox)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.AmountLabel_4 = QLabel(self.AddFriendExpenseBox)
        self.AmountLabel_4.setObjectName(u"AmountLabel_4")
        self.AmountLabel_4.setFont(font1)

        self.verticalLayout_56.addWidget(self.AmountLabel_4)

        self.AmountInput_4 = QLineEdit(self.AddFriendExpenseBox)
        self.AmountInput_4.setObjectName(u"AmountInput_4")
        sizePolicy.setHeightForWidth(self.AmountInput_4.sizePolicy().hasHeightForWidth())
        self.AmountInput_4.setSizePolicy(sizePolicy)
        self.AmountInput_4.setMinimumSize(QSize(0, 37))
        self.AmountInput_4.setMaximumSize(QSize(16777215, 59))

        self.verticalLayout_56.addWidget(self.AmountInput_4)

        self.PayerLabel_4 = QLabel(self.AddFriendExpenseBox)
        self.PayerLabel_4.setObjectName(u"PayerLabel_4")
        self.PayerLabel_4.setFont(font1)

        self.verticalLayout_56.addWidget(self.PayerLabel_4)

        self.PayerInput_4 = QLineEdit(self.AddFriendExpenseBox)
        self.PayerInput_4.setObjectName(u"PayerInput_4")
        sizePolicy.setHeightForWidth(self.PayerInput_4.sizePolicy().hasHeightForWidth())
        self.PayerInput_4.setSizePolicy(sizePolicy)
        self.PayerInput_4.setMinimumSize(QSize(0, 37))
        self.PayerInput_4.setMaximumSize(QSize(16777215, 59))

        self.verticalLayout_56.addWidget(self.PayerInput_4)

        self.ContributersLabel_4 = QLabel(self.AddFriendExpenseBox)
        self.ContributersLabel_4.setObjectName(u"ContributersLabel_4")
        self.ContributersLabel_4.setFont(font1)

        self.verticalLayout_56.addWidget(self.ContributersLabel_4)

        self.ContributersInput_4 = QScrollArea(self.AddFriendExpenseBox)
        self.ContributersInput_4.setObjectName(u"ContributersInput_4")
        self.ContributersInput_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setObjectName(u"scrollAreaWidgetContents_14")
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 436, 85))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents_14)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.checkBox_21 = QCheckBox(self.scrollAreaWidgetContents_14)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.gridLayout_12.addWidget(self.checkBox_21, 1, 1, 1, 1)

        self.checkBox_22 = QCheckBox(self.scrollAreaWidgetContents_14)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.gridLayout_12.addWidget(self.checkBox_22, 1, 2, 1, 1)

        self.ContributersInput_4.setWidget(self.scrollAreaWidgetContents_14)

        self.verticalLayout_56.addWidget(self.ContributersInput_4)

        self.DateLabel_4 = QLabel(self.AddFriendExpenseBox)
        self.DateLabel_4.setObjectName(u"DateLabel_4")
        self.DateLabel_4.setFont(font1)

        self.verticalLayout_56.addWidget(self.DateLabel_4)

        self.DateInput_4 = QWidget(self.AddFriendExpenseBox)
        self.DateInput_4.setObjectName(u"DateInput_4")
        self.horizontalLayout_42 = QHBoxLayout(self.DateInput_4)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.frame_31 = QFrame(self.DateInput_4)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.calendarWidget_4 = QCalendarWidget(self.frame_31)
        self.calendarWidget_4.setObjectName(u"calendarWidget_4")

        self.horizontalLayout_43.addWidget(self.calendarWidget_4)


        self.horizontalLayout_42.addWidget(self.frame_31)


        self.verticalLayout_56.addWidget(self.DateInput_4)

        self.CategoryLabel_4 = QLabel(self.AddFriendExpenseBox)
        self.CategoryLabel_4.setObjectName(u"CategoryLabel_4")
        self.CategoryLabel_4.setFont(font1)

        self.verticalLayout_56.addWidget(self.CategoryLabel_4)

        self.CategoryGrid_4 = QFrame(self.AddFriendExpenseBox)
        self.CategoryGrid_4.setObjectName(u"CategoryGrid_4")
        sizePolicy6.setHeightForWidth(self.CategoryGrid_4.sizePolicy().hasHeightForWidth())
        self.CategoryGrid_4.setSizePolicy(sizePolicy6)
        self.CategoryGrid_4.setFrameShape(QFrame.StyledPanel)
        self.CategoryGrid_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.CategoryGrid_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.radioButton_19 = QRadioButton(self.CategoryGrid_4)
        self.radioButton_19.setObjectName(u"radioButton_19")

        self.gridLayout_13.addWidget(self.radioButton_19, 0, 1, 1, 1)

        self.radioButton_20 = QRadioButton(self.CategoryGrid_4)
        self.radioButton_20.setObjectName(u"radioButton_20")

        self.gridLayout_13.addWidget(self.radioButton_20, 1, 1, 1, 1)

        self.radioButton_21 = QRadioButton(self.CategoryGrid_4)
        self.radioButton_21.setObjectName(u"radioButton_21")

        self.gridLayout_13.addWidget(self.radioButton_21, 1, 2, 1, 1)

        self.radioButton_22 = QRadioButton(self.CategoryGrid_4)
        self.radioButton_22.setObjectName(u"radioButton_22")

        self.gridLayout_13.addWidget(self.radioButton_22, 0, 2, 1, 1)

        self.radioButton_23 = QRadioButton(self.CategoryGrid_4)
        self.radioButton_23.setObjectName(u"radioButton_23")

        self.gridLayout_13.addWidget(self.radioButton_23, 1, 0, 1, 1)

        self.radioButton_24 = QRadioButton(self.CategoryGrid_4)
        self.radioButton_24.setObjectName(u"radioButton_24")

        self.gridLayout_13.addWidget(self.radioButton_24, 0, 0, 1, 1)


        self.verticalLayout_56.addWidget(self.CategoryGrid_4)

        self.DiscriptionLabel_4 = QLabel(self.AddFriendExpenseBox)
        self.DiscriptionLabel_4.setObjectName(u"DiscriptionLabel_4")
        self.DiscriptionLabel_4.setFont(font1)

        self.verticalLayout_56.addWidget(self.DiscriptionLabel_4)

        self.DiscriptionInput_4 = QTextEdit(self.AddFriendExpenseBox)
        self.DiscriptionInput_4.setObjectName(u"DiscriptionInput_4")

        self.verticalLayout_56.addWidget(self.DiscriptionInput_4)

        self.FinalAddFriendExpenseBtn = QPushButton(self.AddFriendExpenseBox)
        self.FinalAddFriendExpenseBtn.setObjectName(u"FinalAddFriendExpenseBtn")
        self.FinalAddFriendExpenseBtn.setFont(font1)
        self.FinalAddFriendExpenseBtn.setIcon(icon26)
        self.FinalAddFriendExpenseBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_56.addWidget(self.FinalAddFriendExpenseBtn)


        self.horizontalLayout_41.addWidget(self.AddFriendExpenseBox)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_13)

        self.verticalLayout_57.addWidget(self.scrollArea_7)

        self.rightMenuPages.addWidget(self.AddFriendExpensePage)

        self.verticalLayout_11.addWidget(self.rightMenuPages)


        self.verticalLayout_10.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_9.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_18 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        sizePolicy5.setHeightForWidth(self.popupNotificationSubContainer.sizePolicy().hasHeightForWidth())
        self.popupNotificationSubContainer.setSizePolicy(sizePolicy5)
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, 0, 0)
        self.label_14 = QLabel(self.popupNotificationSubContainer)
        self.label_14.setObjectName(u"label_14")
        font18 = QFont()
        font18.setFamily(u"Swis721 Blk BT")
        font18.setPointSize(12)
        font18.setBold(True)
        font18.setWeight(75)
        self.label_14.setFont(font18)

        self.verticalLayout_19.addWidget(self.label_14)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy5.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_13, 0, Qt.AlignTop)

        self.ClosePopUpBtn = QPushButton(self.frame_9)
        self.ClosePopUpBtn.setObjectName(u"ClosePopUpBtn")
        icon27 = QIcon()
        icon27.addFile(u":/icons2/icons2/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ClosePopUpBtn.setIcon(icon27)
        self.ClosePopUpBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.ClosePopUpBtn, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_9)


        self.verticalLayout_18.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_9.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        sizePolicy5.setHeightForWidth(self.footerContainer.sizePolicy().hasHeightForWidth())
        self.footerContainer.setSizePolicy(sizePolicy5)
        self.horizontalLayout_12 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_15)


        self.horizontalLayout_12.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(40, 40))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.sizeGrip)


        self.verticalLayout_9.addWidget(self.footerContainer)


        self.horizontalLayout_44.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenupages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(3)
        self.rightMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.MenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.MenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.HomeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.HomeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.DebtsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.DebtsBtn.setText(QCoreApplication.translate("MainWindow", u"Debts", None))
#if QT_CONFIG(tooltip)
        self.ProfileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.ProfileBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.InfoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.InfoBtn.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.LogOutBtn_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"You owe 5$ to Niloo", None))
        self.radioButton_49.setText(QCoreApplication.translate("MainWindow", u"Paid from this account", None))
        self.radioButton_50.setText(QCoreApplication.translate("MainWindow", u"Paid on cash", None))
        self.radioButton_51.setText(QCoreApplication.translate("MainWindow", u"Not Paid", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"RONIL-Split-Wise", None))
#if QT_CONFIG(tooltip)
        self.NotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.NotificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.SearchBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Search", None))
#endif // QT_CONFIG(tooltip)
        self.SearchBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.mainContentContainer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.FriendsIcon.setText("")
        self.FriendsBtn.setText(QCoreApplication.translate("MainWindow", u"Friends", None))
        self.ReportsIcon.setText("")
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.ConversionIcon.setText("")
        self.ConversionBtn.setText(QCoreApplication.translate("MainWindow", u"Currency Conversion", None))
        self.GroupIcon.setText("")
        self.GroupBtn.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.PicProfile.setText("")
        self.NameProfile.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.EditProfileBtn.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.UsernameProfile.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Balance:", None))
        self.EmailProfile.setText(QCoreApplication.translate("MainWindow", u"niloofar.torki1381@gmail.com", None))
        self.BalanceProfile.setText(QCoreApplication.translate("MainWindow", u"x $", None))
        self.BalanceEditBtn.setText("")
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Days of month", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        self.AddRExpenseBtn.setText(QCoreApplication.translate("MainWindow", u"Add Recurrent Expense", None))
        self.LogOutProfileBtn.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.addGrpBtn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Total Expenses:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Total Expenses in groups:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Total expenses with friends:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Total expenses in this month:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"How much you owe:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"How much you are owed:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Visulaize the reports:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.MonthlyReportBtn.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.TotalReportBtn.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Show reports in:", None))
        self.CategoryReportBtn.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.GrpReportBtn.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.FriendReportBtn.setText(QCoreApplication.translate("MainWindow", u"Friends", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.FriendsTitle.setText(QCoreApplication.translate("MainWindow", u"Friends", None))
        self.FriendsNetBalance.setText(QCoreApplication.translate("MainWindow", u"Net Balance:", None))
#if QT_CONFIG(tooltip)
        self.AddFriendsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Add Friends", None))
#endif // QT_CONFIG(tooltip)
        self.AddFriendsBtn.setText("")
        self.FriendProfile.setText("")
        self.FriendName.setText(QCoreApplication.translate("MainWindow", u"Name", None))
#if QT_CONFIG(tooltip)
        self.EditFriendBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Edit Friend's Information", None))
#endif // QT_CONFIG(tooltip)
        self.EditFriendBtn.setText("")
#if QT_CONFIG(tooltip)
        self.AddFriendExpenseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Add Expense", None))
#endif // QT_CONFIG(tooltip)
        self.AddFriendExpenseBtn.setText("")
        self.ListOfExpensesTable.setText(QCoreApplication.translate("MainWindow", u"List of Expenses:", None))
        ___qtablewidgetitem4 = self.TableOfExpenses.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem5 = self.TableOfExpenses.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Payer", None));
        ___qtablewidgetitem6 = self.TableOfExpenses.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem7 = self.TableOfExpenses.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Contributers", None));
        ___qtablewidgetitem8 = self.TableOfExpenses.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem9 = self.TableOfExpenses.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem10 = self.TableOfExpenses.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Split", None));
        ___qtablewidgetitem11 = self.TableOfExpenses.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.FriendsExpenseGraphBtn.setText(QCoreApplication.translate("MainWindow", u"Show Expenses Graph", None))
        self.FriendExpenseGraph.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GrpName.setText(QCoreApplication.translate("MainWindow", u"Group Name", None))
        self.grp_owner.setText(QCoreApplication.translate("MainWindow", u"Owner: ", None))
        self.GrpTotalExpense.setText(QCoreApplication.translate("MainWindow", u"Total expenses: ", None))
#if QT_CONFIG(tooltip)
        self.AddMembersBtn_7.setToolTip(QCoreApplication.translate("MainWindow", u"Add Members", None))
#endif // QT_CONFIG(tooltip)
        self.AddMembersBtn_7.setText("")
#if QT_CONFIG(tooltip)
        self.AddExpensesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Add Expenses", None))
#endif // QT_CONFIG(tooltip)
        self.AddExpensesBtn.setText("")
#if QT_CONFIG(tooltip)
        self.EditGrpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Edit Group Information", None))
#endif // QT_CONFIG(tooltip)
        self.EditGrpBtn.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Members Debt Table:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Expenses Table:", None))
        ___qtablewidgetitem12 = self.ExpensesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem13 = self.ExpensesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Payer", None));
        ___qtablewidgetitem14 = self.ExpensesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem15 = self.ExpensesTable.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Contributers", None));
        ___qtablewidgetitem16 = self.ExpensesTable.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem17 = self.ExpensesTable.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem18 = self.ExpensesTable.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Split type", None));
        ___qtablewidgetitem19 = self.ExpensesTable.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.ExpenseGraphBtn.setText(QCoreApplication.translate("MainWindow", u"Show Expenses Graph", None))
        self.DebtGraphBtn.setText(QCoreApplication.translate("MainWindow", u"Show Debt Graph", None))
        self.closeGraphBtn.setText("")
        self.GraphTitle.setText(QCoreApplication.translate("MainWindow", u"Original Graph", None))
        self.Graph.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.CloseRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.CloseRightMenuBtn.setText("")
        self.AddNewMemberBox.setTitle("")
        self.NewMemberLabel.setText(QCoreApplication.translate("MainWindow", u"New Member's Name", None))
        self.ExpensesLabel.setText(QCoreApplication.translate("MainWindow", u"Which expenses she/he was in?", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Me", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.FinalAddMemberBtn.setText(QCoreApplication.translate("MainWindow", u"Add New Member", None))
        self.AddNewFriendBox.setTitle("")
        self.NameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.EmailLabel.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.ProfileLabel.setText(QCoreApplication.translate("MainWindow", u"Choose a profile:", None))
        self.LadyProfileBtn.setText("")
        self.MaleProfileBtn.setText("")
        self.AddFriendBtn.setText(QCoreApplication.translate("MainWindow", u"Add Friend", None))
        self.groupBox_10.setTitle("")
        self.GrpNameLabel.setText(QCoreApplication.translate("MainWindow", u"Group Name", None))
        self.NoMembersLabel.setText(QCoreApplication.translate("MainWindow", u"Number of members", None))
        self.GrpMembersLabel.setText(QCoreApplication.translate("MainWindow", u"Group Members", None))
        self.DefaultSplitLabel.setText(QCoreApplication.translate("MainWindow", u"DefaultSplit", None))
        self.Equal.setText(QCoreApplication.translate("MainWindow", u"equally", None))
        self.share.setText(QCoreApplication.translate("MainWindow", u"share", None))
        self.percentage.setText(QCoreApplication.translate("MainWindow", u"percentage", None))
        self.FinalAddGrpBtn.setText(QCoreApplication.translate("MainWindow", u"Add Group", None))
        self.AddExpenseBox_4.setTitle("")
        self.LabelLabel.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.AmountRExpenseLabel.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.DaysLabel.setText(QCoreApplication.translate("MainWindow", u"Check the days when this expense happens:", None))
        self.day27.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.day28.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.day1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.day1_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.day10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.day9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.day6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.day3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.day4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.day5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.day16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.day18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.day17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.day20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.day19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.day22.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.day21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.day24.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.day25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.day26.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.day7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.day14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.day8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.day11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.day12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.day15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.day13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.day23.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.day29.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.day30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.day31.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.CategoryLabel_5.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.radioButton_25.setText(QCoreApplication.translate("MainWindow", u"Health", None))
        self.radioButton_26.setText(QCoreApplication.translate("MainWindow", u"Transport", None))
        self.radioButton_27.setText(QCoreApplication.translate("MainWindow", u"etc.", None))
        self.radioButton_28.setText(QCoreApplication.translate("MainWindow", u"Housing", None))
        self.radioButton_29.setText(QCoreApplication.translate("MainWindow", u"Education/Entertainment", None))
        self.radioButton_30.setText(QCoreApplication.translate("MainWindow", u"Food", None))
        self.FinalAddRecurrentExpenseBtn.setText(QCoreApplication.translate("MainWindow", u"Add Recurrent Expense", None))
        self.AddExpenseBox.setTitle("")
        self.GrpExpenseLabelLabel.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.AmountLabel.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.PayerLabel.setText(QCoreApplication.translate("MainWindow", u"Who Paid?", None))
        self.ContributersLabel.setText(QCoreApplication.translate("MainWindow", u"Who are in?", None))
        self.DateLabel.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.CategoryLabel.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Health", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Transport", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"etc.", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Housing", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Education/Entertainment", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Food", None))
        self.SplitLabel.setText(QCoreApplication.translate("MainWindow", u"Split:", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"default split", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"equally", None))
        self.ShareSplit.setText(QCoreApplication.translate("MainWindow", u"share", None))
        self.PercentageSplit.setText(QCoreApplication.translate("MainWindow", u"percentage", None))
        self.DiscriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Discription(Optional):", None))
        self.FinalAddExpenseBtn.setText(QCoreApplication.translate("MainWindow", u"Add Expense", None))
        self.AddFriendExpenseBox.setTitle("")
        self.AmountLabel_4.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.PayerLabel_4.setText(QCoreApplication.translate("MainWindow", u"Who Paid?", None))
        self.ContributersLabel_4.setText(QCoreApplication.translate("MainWindow", u"Who are in?", None))
        self.checkBox_21.setText(QCoreApplication.translate("MainWindow", u"Me", None))
        self.checkBox_22.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.DateLabel_4.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.CategoryLabel_4.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_20.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_22.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_23.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_24.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.DiscriptionLabel_4.setText(QCoreApplication.translate("MainWindow", u"Discription(Optional):", None))
        self.FinalAddFriendExpenseBtn.setText(QCoreApplication.translate("MainWindow", u"Add Expense", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification Messages", None))
#if QT_CONFIG(tooltip)
        self.ClosePopUpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.ClosePopUpBtn.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Copyright RONIL", None))
    # retranslateUi

