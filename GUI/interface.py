# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 786)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}\n"
"#centralwidget{\n"
"    background-color: #1f232a;\n"
"}\n"
"#LeftMenuSubcontainer{\n"
"    background-color: #16191d;\n"
"}\n"
"#LeftMenuSubcontainer QPushButton{\n"
"    text-align: left;\n"
"    padding: 5px 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"    background-color: #2c313c;\n"
"}\n"
"#frame_6, #frame_8, #popupNotificationSubContainer{\n"
"    background-color: #16191d;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer{\n"
"    background-color: #2c313c;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMinimumSize(QtCore.QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QtCore.QSize(45, 16777215))
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LeftMenuSubcontainer = QtWidgets.QWidget(self.leftMenuContainer)
        self.LeftMenuSubcontainer.setObjectName("LeftMenuSubcontainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LeftMenuSubcontainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.LeftMenuSubcontainer)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MenuBtn = QtWidgets.QPushButton(self.frame)
        self.MenuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons2/icons2/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuBtn.setIcon(icon)
        self.MenuBtn.setIconSize(QtCore.QSize(32, 32))
        self.MenuBtn.setObjectName("MenuBtn")
        self.horizontalLayout_2.addWidget(self.MenuBtn)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.LeftMenuSubcontainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.HomeBtn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.HomeBtn.setFont(font)
        self.HomeBtn.setStyleSheet("background-color: #1f232a")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons2/icons2/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeBtn.setIcon(icon1)
        self.HomeBtn.setIconSize(QtCore.QSize(24, 24))
        self.HomeBtn.setObjectName("HomeBtn")
        self.verticalLayout_5.addWidget(self.HomeBtn)
        self.DataBtn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.DataBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons2/icons2/activity.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DataBtn.setIcon(icon2)
        self.DataBtn.setIconSize(QtCore.QSize(24, 24))
        self.DataBtn.setObjectName("DataBtn")
        self.verticalLayout_5.addWidget(self.DataBtn)
        self.ReportsBtn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.ReportsBtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons2/icons2/archive.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ReportsBtn.setIcon(icon3)
        self.ReportsBtn.setIconSize(QtCore.QSize(24, 24))
        self.ReportsBtn.setObjectName("ReportsBtn")
        self.verticalLayout_5.addWidget(self.ReportsBtn)
        self.verticalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.LeftMenuSubcontainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SettingsBtn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.SettingsBtn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons2/icons2/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingsBtn.setIcon(icon4)
        self.SettingsBtn.setIconSize(QtCore.QSize(24, 24))
        self.SettingsBtn.setObjectName("SettingsBtn")
        self.verticalLayout_4.addWidget(self.SettingsBtn)
        self.InfoBtn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.InfoBtn.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons2/icons2/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.InfoBtn.setIcon(icon5)
        self.InfoBtn.setIconSize(QtCore.QSize(24, 24))
        self.InfoBtn.setObjectName("InfoBtn")
        self.verticalLayout_4.addWidget(self.InfoBtn)
        self.HelpBtn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.HelpBtn.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons2/icons2/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HelpBtn.setIcon(icon6)
        self.HelpBtn.setIconSize(QtCore.QSize(24, 24))
        self.HelpBtn.setObjectName("HelpBtn")
        self.verticalLayout_4.addWidget(self.HelpBtn)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.LeftMenuSubcontainer)
        self.horizontalLayout.addWidget(self.leftMenuContainer)
        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerMenuContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuContainer.setSizePolicy(sizePolicy)
        self.centerMenuContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.centerMenuContainer.setObjectName("centerMenuContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centerMenuContainer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.centerMenuSubContainer = QtWidgets.QWidget(self.centerMenuContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuSubContainer.setSizePolicy(sizePolicy)
        self.centerMenuSubContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.centerMenuSubContainer.setObjectName("centerMenuSubContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.centerMenuSubContainer)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.closeCenterMenuBtn = QtWidgets.QPushButton(self.frame_6)
        self.closeCenterMenuBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons2/icons2/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon7)
        self.closeCenterMenuBtn.setIconSize(QtCore.QSize(24, 24))
        self.closeCenterMenuBtn.setObjectName("closeCenterMenuBtn")
        self.horizontalLayout_4.addWidget(self.closeCenterMenuBtn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.centerMenupages = QCustomQStackedWidget(self.centerMenuSubContainer)
        self.centerMenupages.setObjectName("centerMenupages")
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settingsPage)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.centerMenupages.addWidget(self.settingsPage)
        self.informationPage = QtWidgets.QWidget()
        self.informationPage.setObjectName("informationPage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.informationPage)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.informationPage)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.centerMenupages.addWidget(self.informationPage)
        self.helpPage = QtWidgets.QWidget()
        self.helpPage.setObjectName("helpPage")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.helpPage)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.helpPage)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.centerMenupages.addWidget(self.helpPage)
        self.verticalLayout_3.addWidget(self.centerMenupages)
        self.horizontalLayout_3.addWidget(self.centerMenuSubContainer, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.centerMenuContainer)
        self.mainBodyContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet("")
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.headerContainer = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy)
        self.headerContainer.setObjectName("headerContainer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.headerContainer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setMinimumSize(QtCore.QSize(24, 24))
        self.label_5.setMaximumSize(QtCore.QSize(24, 24))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/images/logo2.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_5.addWidget(self.frame_4, 0, QtCore.Qt.AlignLeft)
        self.frame_5 = QtWidgets.QFrame(self.headerContainer)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.NotificationBtn = QtWidgets.QPushButton(self.frame_5)
        self.NotificationBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons2/icons2/bell.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NotificationBtn.setIcon(icon8)
        self.NotificationBtn.setIconSize(QtCore.QSize(24, 24))
        self.NotificationBtn.setObjectName("NotificationBtn")
        self.horizontalLayout_8.addWidget(self.NotificationBtn)
        self.RightMenuBtn = QtWidgets.QPushButton(self.frame_5)
        self.RightMenuBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons2/icons2/more-horizontal.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RightMenuBtn.setIcon(icon9)
        self.RightMenuBtn.setIconSize(QtCore.QSize(24, 24))
        self.RightMenuBtn.setObjectName("RightMenuBtn")
        self.horizontalLayout_8.addWidget(self.RightMenuBtn)
        self.ProfileMenuBtn = QtWidgets.QPushButton(self.frame_5)
        self.ProfileMenuBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons2/icons2/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ProfileMenuBtn.setIcon(icon10)
        self.ProfileMenuBtn.setIconSize(QtCore.QSize(24, 24))
        self.ProfileMenuBtn.setObjectName("ProfileMenuBtn")
        self.horizontalLayout_8.addWidget(self.ProfileMenuBtn)
        self.horizontalLayout_5.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.headerContainer)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.minimizeBtn = QtWidgets.QPushButton(self.frame_7)
        self.minimizeBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons2/icons2/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeBtn.setIcon(icon11)
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_6.addWidget(self.minimizeBtn)
        self.restoreBtn = QtWidgets.QPushButton(self.frame_7)
        self.restoreBtn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons2/icons2/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreBtn.setIcon(icon12)
        self.restoreBtn.setObjectName("restoreBtn")
        self.horizontalLayout_6.addWidget(self.restoreBtn)
        self.closeBtn = QtWidgets.QPushButton(self.frame_7)
        self.closeBtn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons2/icons2/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon13)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_6.addWidget(self.closeBtn)
        self.horizontalLayout_5.addWidget(self.frame_7, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_9.addWidget(self.headerContainer)
        self.mainBodyContent = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.mainBodyContent.setObjectName("mainBodyContent")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.mainContentContainer = QtWidgets.QWidget(self.mainBodyContent)
        self.mainContentContainer.setObjectName("mainContentContainer")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.mainContentContainer)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.mainPages = QCustomQStackedWidget(self.mainContentContainer)
        self.mainPages.setObjectName("mainPages")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.homePage)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_10 = QtWidgets.QLabel(self.homePage)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_15.addWidget(self.label_10)
        self.mainPages.addWidget(self.homePage)
        self.dataPage = QtWidgets.QWidget()
        self.dataPage.setObjectName("dataPage")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.dataPage)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_11 = QtWidgets.QLabel(self.dataPage)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_16.addWidget(self.label_11)
        self.mainPages.addWidget(self.dataPage)
        self.reportPage = QtWidgets.QWidget()
        self.reportPage.setObjectName("reportPage")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.reportPage)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_12 = QtWidgets.QLabel(self.reportPage)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_17.addWidget(self.label_12)
        self.mainPages.addWidget(self.reportPage)
        self.verticalLayout_14.addWidget(self.mainPages)
        self.horizontalLayout_9.addWidget(self.mainContentContainer)
        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.rightMenuContainer.setObjectName("rightMenuContainer")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.rightMenuSubContainer = QtWidgets.QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.rightMenuSubContainer.setObjectName("rightMenuSubContainer")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_8 = QtWidgets.QFrame(self.rightMenuSubContainer)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.CloseRightMenuBtn = QtWidgets.QPushButton(self.frame_8)
        self.CloseRightMenuBtn.setText("")
        self.CloseRightMenuBtn.setIcon(icon7)
        self.CloseRightMenuBtn.setIconSize(QtCore.QSize(32, 32))
        self.CloseRightMenuBtn.setObjectName("CloseRightMenuBtn")
        self.horizontalLayout_10.addWidget(self.CloseRightMenuBtn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_11.addWidget(self.frame_8)
        self.rightMenuPages = QCustomQStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName("rightMenuPages")
        self.profilePage = QtWidgets.QWidget()
        self.profilePage.setObjectName("profilePage")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.profilePage)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.profilePage)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_12.addWidget(self.label_8)
        self.rightMenuPages.addWidget(self.profilePage)
        self.morePage = QtWidgets.QWidget()
        self.morePage.setObjectName("morePage")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.morePage)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.morePage)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.rightMenuPages.addWidget(self.morePage)
        self.verticalLayout_11.addWidget(self.rightMenuPages)
        self.verticalLayout_10.addWidget(self.rightMenuSubContainer)
        self.horizontalLayout_9.addWidget(self.rightMenuContainer, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_9.addWidget(self.mainBodyContent)
        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName("popupNotificationContainer")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.popupNotificationSubContainer = QtWidgets.QWidget(self.popupNotificationContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupNotificationSubContainer.sizePolicy().hasHeightForWidth())
        self.popupNotificationSubContainer.setSizePolicy(sizePolicy)
        self.popupNotificationSubContainer.setObjectName("popupNotificationSubContainer")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_19.setContentsMargins(9, 9, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_14 = QtWidgets.QLabel(self.popupNotificationSubContainer)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_19.addWidget(self.label_14)
        self.frame_9 = QtWidgets.QFrame(self.popupNotificationSubContainer)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13, 0, QtCore.Qt.AlignTop)
        self.ClosePopUpBtn = QtWidgets.QPushButton(self.frame_9)
        self.ClosePopUpBtn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons2/icons2/x-octagon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClosePopUpBtn.setIcon(icon14)
        self.ClosePopUpBtn.setIconSize(QtCore.QSize(24, 24))
        self.ClosePopUpBtn.setObjectName("ClosePopUpBtn")
        self.horizontalLayout_11.addWidget(self.ClosePopUpBtn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_19.addWidget(self.frame_9)
        self.verticalLayout_18.addWidget(self.popupNotificationSubContainer)
        self.verticalLayout_9.addWidget(self.popupNotificationContainer)
        self.footerContainer = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footerContainer.sizePolicy().hasHeightForWidth())
        self.footerContainer.setSizePolicy(sizePolicy)
        self.footerContainer.setObjectName("footerContainer")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.footerContainer)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_10 = QtWidgets.QFrame(self.footerContainer)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_15 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.horizontalLayout_12.addWidget(self.frame_10)
        self.sizeGrip = QtWidgets.QFrame(self.footerContainer)
        self.sizeGrip.setMinimumSize(QtCore.QSize(10, 10))
        self.sizeGrip.setMaximumSize(QtCore.QSize(40, 40))
        self.sizeGrip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sizeGrip.setObjectName("sizeGrip")
        self.horizontalLayout_12.addWidget(self.sizeGrip)
        self.verticalLayout_9.addWidget(self.footerContainer)
        self.horizontalLayout.addWidget(self.mainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.rightMenuPages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MenuBtn.setToolTip(_translate("MainWindow", "Menu"))
        self.HomeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.HomeBtn.setText(_translate("MainWindow", "Home"))
        self.DataBtn.setToolTip(_translate("MainWindow", "Data Analysis"))
        self.DataBtn.setText(_translate("MainWindow", "Data Analysis"))
        self.ReportsBtn.setToolTip(_translate("MainWindow", "Reports"))
        self.ReportsBtn.setText(_translate("MainWindow", "Reports"))
        self.SettingsBtn.setToolTip(_translate("MainWindow", "Settings"))
        self.SettingsBtn.setText(_translate("MainWindow", "Settings"))
        self.InfoBtn.setToolTip(_translate("MainWindow", "Information"))
        self.InfoBtn.setText(_translate("MainWindow", "Info"))
        self.HelpBtn.setToolTip(_translate("MainWindow", "Help"))
        self.HelpBtn.setText(_translate("MainWindow", "Help"))
        self.label_2.setText(_translate("MainWindow", "More Menu"))
        self.closeCenterMenuBtn.setToolTip(_translate("MainWindow", "Close Menu"))
        self.label.setText(_translate("MainWindow", "Settings"))
        self.label_3.setText(_translate("MainWindow", "Information"))
        self.label_4.setText(_translate("MainWindow", "Help"))
        self.label_6.setText(_translate("MainWindow", "RONIL-Split-Wise"))
        self.RightMenuBtn.setToolTip(_translate("MainWindow", "More"))
        self.ProfileMenuBtn.setToolTip(_translate("MainWindow", "Profile"))
        self.minimizeBtn.setToolTip(_translate("MainWindow", "Minimize Window"))
        self.restoreBtn.setToolTip(_translate("MainWindow", "Restore Window"))
        self.closeBtn.setToolTip(_translate("MainWindow", "Close Window"))
        self.label_10.setText(_translate("MainWindow", "Home"))
        self.label_11.setText(_translate("MainWindow", "Data Analysis"))
        self.label_12.setText(_translate("MainWindow", "Reports"))
        self.label_7.setText(_translate("MainWindow", "Right Menu"))
        self.CloseRightMenuBtn.setToolTip(_translate("MainWindow", "Close Menu"))
        self.label_8.setText(_translate("MainWindow", "Profile"))
        self.label_9.setText(_translate("MainWindow", "More..."))
        self.label_14.setText(_translate("MainWindow", "Notification"))
        self.label_13.setText(_translate("MainWindow", "Notification Messages"))
        self.ClosePopUpBtn.setToolTip(_translate("MainWindow", "Close Notifications"))
        self.label_15.setText(_translate("MainWindow", "Copyright RONIL"))
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import images_rc
import resource2_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
