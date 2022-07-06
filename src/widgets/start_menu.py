# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 157, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.texts_button = QtWidgets.QPushButton(Form)
        self.texts_button.setMinimumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.texts_button.setFont(font)
        self.texts_button.setObjectName("texts_button")
        self.horizontalLayout_2.addWidget(self.texts_button)
        self.run_button = QtWidgets.QPushButton(Form)
        self.run_button.setMinimumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.run_button.setFont(font)
        self.run_button.setObjectName("run_button")
        self.horizontalLayout_2.addWidget(self.run_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.credits_button = QtWidgets.QPushButton(Form)
        self.credits_button.setMinimumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.credits_button.setFont(font)
        self.credits_button.setObjectName("credits_button")
        self.horizontalLayout.addWidget(self.credits_button)
        self.settings_button = QtWidgets.QPushButton(Form)
        self.settings_button.setMinimumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.horizontalLayout.addWidget(self.settings_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 157, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.texts_button.setText(_translate("Form", "Texts"))
        self.run_button.setText(_translate("Form", "Run"))
        self.credits_button.setText(_translate("Form", "Credits"))
        self.settings_button.setText(_translate("Form", "Setting"))
