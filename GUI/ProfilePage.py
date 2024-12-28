from PyQt5 import QtCore, QtGui, QtWidgets

def toggle_edit_mode_NameProfile(ui, edited):
        
        if edited:
            name = ui.NameProfile.text()
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
            ui.EditProfileBtn.clicked.connect(lambda: toggle_edit_mode_NameProfile(ui, edited))

        else:
            new_name = ui.NameLineEdit.text()
            name = new_name.strip() if new_name.strip() else name  # Avoid empty names
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
            ui.EditProfileBtn.clicked.connect(lambda: toggle_edit_mode_NameProfile(ui, edited))


