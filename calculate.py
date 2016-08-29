# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculate.ui'
#
# Created: Sat Aug 27 20:36:13 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(625, 409)
        Form.setAcceptDrops(False)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 160, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.verticalLayout.addWidget(self.label1)
        self.input1 = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.input1.setObjectName(_fromUtf8("input1"))
        self.verticalLayout.addWidget(self.input1)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 20, 111, 81))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.symbol1_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.symbol1_2.setObjectName(_fromUtf8("symbol1_2"))
        self.verticalLayout_2.addWidget(self.symbol1_2)
        self.symbol1 = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.symbol1.setObjectName(_fromUtf8("symbol1"))
        self.symbol1.addItem(_fromUtf8(""))
        self.symbol1.addItem(_fromUtf8(""))
        self.symbol1.addItem(_fromUtf8(""))
        self.symbol1.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.symbol1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(450, 70, 21, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(300, 20, 141, 80))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.input2_2 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.input2_2.setObjectName(_fromUtf8("input2_2"))
        self.verticalLayout_3.addWidget(self.input2_2)
        self.input2 = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.input2.setObjectName(_fromUtf8("input2"))
        self.verticalLayout_3.addWidget(self.input2)
        self.verticalLayoutWidget_4 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(470, 20, 160, 80))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.output = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.output.setObjectName(_fromUtf8("output"))
        self.verticalLayout_4.addWidget(self.output)
        self.spinBox = QtGui.QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.verticalLayout_4.addWidget(self.spinBox)
        self.ping_action = QtGui.QPushButton(Form)
        self.ping_action.setGeometry(QtCore.QRect(490, 200, 98, 27))
        self.ping_action.setObjectName(_fromUtf8("ping_action"))
        self.show_data_table = QtGui.QTableView(Form)
        self.show_data_table.setGeometry(QtCore.QRect(30, 130, 231, 192))
        self.show_data_table.setObjectName(_fromUtf8("show_data_table"))
        self.delete_view = QtGui.QPushButton(Form)
        self.delete_view.setGeometry(QtCore.QRect(490, 270, 98, 27))
        self.delete_view.setObjectName(_fromUtf8("delete_view"))
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 120, 184, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.input_text = QtGui.QTextEdit(self.horizontalLayoutWidget)
        self.input_text.setObjectName(_fromUtf8("input_text"))
        self.horizontalLayout.addWidget(self.input_text)
        self.search_text = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.search_text.setObjectName(_fromUtf8("search_text"))
        self.horizontalLayout.addWidget(self.search_text)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label1.setText(_translate("Form", "              input1", None))
        self.symbol1_2.setText(_translate("Form", "symbol", None))
        self.symbol1.setItemText(0, _translate("Form", "+", None))
        self.symbol1.setItemText(1, _translate("Form", "-", None))
        self.symbol1.setItemText(2, _translate("Form", "*", None))
        self.symbol1.setItemText(3, _translate("Form", "/", None))
        self.label_2.setText(_translate("Form", "=", None))
        self.input2_2.setText(_translate("Form", "input2", None))
        self.output.setText(_translate("Form", "output", None))
        self.ping_action.setText(_translate("Form", "执行检测", None))
        self.delete_view.setText(_translate("Form", "删除记录", None))
        self.search_text.setText(_translate("Form", "搜索", None))

