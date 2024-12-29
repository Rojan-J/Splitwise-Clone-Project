from PyQt5 import QtCore, QtGui, QtWidgets

def toggle_edit_mode_NameProfile(ui, edited, name):
        
        if edited:
            ui.NameProfile.deleteLater()
            ui.horizontalLayout_51.removeWidget(ui.NameProfile)
            ui.NameLineEdit = QtWidgets.QLineEdit(ui.ProfileContainer)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.NameLineEdit.sizePolicy().hasHeightForWidth())
            ui.NameLineEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(20)
            ui.NameLineEdit.setFont(font)
            ui.NameLineEdit.setObjectName("NameLineEdit")
            ui.horizontalLayout_51.addWidget(ui.NameLineEdit)
            ui.NameLineEdit.setText(name)
            ui.EditProfileBtn.deleteLater()
            ui.EditProfileBtn = QtWidgets.QPushButton(ui.ProfileContainer)
            ui.EditProfileBtn.setText("")
            icon17 = QtGui.QIcon()
            icon17.addPixmap(QtGui.QPixmap("icons2/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ui.EditProfileBtn.setIcon(icon17)
            ui.EditProfileBtn.setIconSize(QtCore.QSize(32, 32))
            ui.EditProfileBtn.setObjectName("EditProfileBtn")
            ui.horizontalLayout_51.addWidget(ui.EditProfileBtn)
            edited = False
            ui.EditProfileBtn.clicked.connect(lambda: toggle_edit_mode_NameProfile(ui, edited, name))

        else:
            new_name = ui.NameLineEdit.text()
            name = " ".join(new_name.split()) if new_name.strip() else name  # Avoid empty names
            ui.NameLineEdit.deleteLater()
            ui.NameProfile = QtWidgets.QLabel(ui.ProfileContainer)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.NameProfile.sizePolicy().hasHeightForWidth())
            ui.NameProfile.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(20)
            ui.NameProfile.setFont(font)
            ui.NameProfile.setObjectName("NameProfile")
            ui.horizontalLayout_51.addWidget(ui.NameProfile)
            ui.NameProfile.setText(name)
            # Switch back to display mode
            ui.NameProfile.setText(name)
            ui.EditProfileBtn.deleteLater()
            ui.EditProfileBtn = QtWidgets.QPushButton(ui.ProfileContainer)
            ui.EditProfileBtn.setText("")
            icon17 = QtGui.QIcon()
            icon17.addPixmap(QtGui.QPixmap("icons2/edit-3.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ui.EditProfileBtn.setIcon(icon17)
            ui.EditProfileBtn.setIconSize(QtCore.QSize(32, 32))
            ui.EditProfileBtn.setObjectName("EditProfileBtn")
            ui.horizontalLayout_51.addWidget(ui.EditProfileBtn)


            edited = True
            ui.EditProfileBtn.clicked.connect(lambda: toggle_edit_mode_NameProfile(ui, edited, name))


def toggle_edit_Balance(ui, edited, balance):
        
        if edited:
            ui.BalanceProfile.deleteLater()
            ui.BalanceLineEdit = QtWidgets.QLineEdit(ui.frame_52)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(11)
            ui.BalanceLineEdit.setFont(font)
            ui.BalanceLineEdit.setObjectName("BalanceLineEdit")
            ui.verticalLayout_90.addWidget(ui.BalanceLineEdit)
            ui.BalanceLineEdit.setText(balance)

            ui.BalanceEditBtn.deleteLater()
            ui.BalanceEditBtn = QtWidgets.QPushButton(ui.ProfileeInformations)
            ui.BalanceEditBtn.setText("")
            icon18 = QtGui.QIcon()
            icon18.addPixmap(QtGui.QPixmap("icons2/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ui.BalanceEditBtn.setIcon(icon18)
            ui.BalanceEditBtn.setIconSize(QtCore.QSize(20, 20))
            ui.BalanceEditBtn.setObjectName("BalanceEditBtn")
            ui.gridLayout_15.addWidget(ui.BalanceEditBtn, 2, 2, 1, 1)
            edited = False
            ui.BalanceEditBtn.clicked.connect(lambda: toggle_edit_Balance(ui, edited, balance))

        else:
            balance_check = False
            new_balance = ui.BalanceLineEdit.text()
            if new_balance != "":
                try:
                    int_balance = int(new_balance)
                    balance_check = True
                except:
                    balance_check = False
                balance = new_balance if balance_check else balance

            ui.BalanceLineEdit.deleteLater()
            ui.BalanceProfile = QtWidgets.QLabel(ui.frame_52)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(11)
            ui.BalanceProfile.setFont(font)
            ui.BalanceProfile.setObjectName("BalanceProfile")
            ui.verticalLayout_90.addWidget(ui.BalanceProfile)
            ui.BalanceProfile.setText(balance)
            # Switch back to display mode
            ui.BalanceProfile.setText(balance)

            ui.BalanceEditBtn.deleteLater()
            ui.BalanceEditBtn = QtWidgets.QPushButton(ui.ProfileeInformations)
            ui.BalanceEditBtn.setText("")
            icon18 = QtGui.QIcon()
            icon18.addPixmap(QtGui.QPixmap("icons2/edit-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ui.BalanceEditBtn.setIcon(icon18)
            ui.BalanceEditBtn.setIconSize(QtCore.QSize(20, 20))
            ui.BalanceEditBtn.setObjectName("BalanceEditBtn")
            ui.gridLayout_15.addWidget(ui.BalanceEditBtn, 2, 2, 1, 1)


            edited = True
            ui.BalanceEditBtn.clicked.connect(lambda: toggle_edit_Balance(ui, edited, balance))


