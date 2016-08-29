# -*- coding:utf-8
"""
行程了
"""
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

from util import create_db, initialize_model,delete,search_test

from calculate import Ui_Form


class CalculateForm(QWidget):
    def __init__(self, parent=None):
        # 这里全都是模板
        super(CalculateForm, self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show_view()
        self.ui.ping_action.clicked.connect(self.showDialog)  # 不能是函数
        self.ui.delete_view.clicked.connect(self.delete)
        self.ui.search_text.clicked.connect(self.search)

    def search(self):
        param=self.ui.input_text.toPlainText()
        sqlQueryModel=QSqlQueryModel()
        sqlQueryModel.setQuery("select * from test where value like '%test%' ")
        self.ui.show_data_table.setModel(sqlQueryModel)
        self.ui.show_data_table.show()

    def show_view(self):
        model = QSqlTableModel()
        initialize_model(model)
        self.ui.show_data_table.setModel(model)
        self.ui.show_data_table.show()

    def showDialog(self):
        create_db()
        # indexes=self.ui.show_data_table.selectionModel().selectedRows()
        # for index in indexes:
        #     print index.row()
        self.show_view()
        # print self.ui.show_data_table.selectedIndexes()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(u"检测成功")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

    def delete(self):
        indexes=self.ui.show_data_table.selectionModel().selectedRows()
        index=indexes[0].row()
        print index
        delete(index)
        self.show_view()


    def get_value(self):
        symbol = str(self.ui.symbol1.currentText())
        input1 = self.ui.input1.value()
        input2 = self.ui.input2.value()
        return eval(str(input1) + symbol + str(input2))

    @pyqtSlot(int)
    def on_input1_valueChanged(self, value):
        self.ui.output.setText(str(self.get_value()))

    @pyqtSlot(int)
    def on_input2_valueChanged(self, value):
        self.ui.output.setText(str(self.get_value()))

    @pyqtSlot(int)
    def on_symbol1_activated(self, value):
        self.ui.output.setText(str(self.get_value()))


if __name__ == '__main__':
    # excute()
    import sys

    app = QApplication(sys.argv)
    calculator = CalculateForm()
    calculator.show()
    sys.exit(app.exec_())
