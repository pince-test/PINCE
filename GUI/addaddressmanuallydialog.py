# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addaddressmanuallydialog.ui'
#
# Created: Sat May 14 01:13:46 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(374, 222)
        Dialog.setMaximumSize(QtCore.QSize(374, 222))
        Dialog.setWindowTitle("")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_address = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.horizontalLayout.addWidget(self.lineEdit_address)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_valueofaddress = QtWidgets.QLabel(Dialog)
        self.label_valueofaddress.setObjectName("label_valueofaddress")
        self.horizontalLayout.addWidget(self.label_valueofaddress)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_description = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_description.setObjectName("lineEdit_description")
        self.verticalLayout.addWidget(self.lineEdit_description)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_ValueType = QtWidgets.QComboBox(Dialog)
        self.comboBox_ValueType.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_ValueType.setObjectName("comboBox_ValueType")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_ValueType)
        self.label_length = QtWidgets.QLabel(Dialog)
        self.label_length.setObjectName("label_length")
        self.horizontalLayout_2.addWidget(self.label_length)
        self.lineEdit_length = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_length.sizePolicy().hasHeightForWidth())
        self.lineEdit_length.setSizePolicy(sizePolicy)
        self.lineEdit_length.setInputMask("")
        self.lineEdit_length.setObjectName("lineEdit_length")
        self.horizontalLayout_2.addWidget(self.lineEdit_length)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_zeroterminate = QtWidgets.QCheckBox(Dialog)
        self.checkBox_zeroterminate.setChecked(True)
        self.checkBox_zeroterminate.setObjectName("checkBox_zeroterminate")
        self.verticalLayout_3.addWidget(self.checkBox_zeroterminate)
        self.checkBox_Unicode = QtWidgets.QCheckBox(Dialog)
        self.checkBox_Unicode.setObjectName("checkBox_Unicode")
        self.verticalLayout_3.addWidget(self.checkBox_Unicode)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.comboBox_ValueType.setCurrentIndex(2)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "Address:"))
        self.lineEdit_address.setText(_translate("Dialog", "0x"))
        self.label_2.setText(_translate("Dialog", "="))
        self.label_valueofaddress.setText(_translate("Dialog", "??"))
        self.label_4.setText(_translate("Dialog", "Description:"))
        self.lineEdit_description.setText(_translate("Dialog", "No Description"))
        self.label_5.setText(_translate("Dialog", "Type:"))
        self.comboBox_ValueType.setItemText(0, _translate("Dialog", "Byte"))
        self.comboBox_ValueType.setItemText(1, _translate("Dialog", "2 Bytes"))
        self.comboBox_ValueType.setItemText(2, _translate("Dialog", "4 Bytes"))
        self.comboBox_ValueType.setItemText(3, _translate("Dialog", "8 Bytes"))
        self.comboBox_ValueType.setItemText(4, _translate("Dialog", "Float"))
        self.comboBox_ValueType.setItemText(5, _translate("Dialog", "Double"))
        self.comboBox_ValueType.setItemText(6, _translate("Dialog", "String"))
        self.comboBox_ValueType.setItemText(7, _translate("Dialog", "Array of bytes"))
        self.label_length.setText(_translate("Dialog", "Length"))
        self.lineEdit_length.setText(_translate("Dialog", "10"))
        self.checkBox_zeroterminate.setText(_translate("Dialog", "Zero-Terminated"))
        self.checkBox_Unicode.setText(_translate("Dialog", "Unicode"))

