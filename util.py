# -*- coding:utf-8

from PyQt4 import QtSql,QtGui,QtCore

db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('test_sq.db')


def create_db():
    if not db.open():
        print 'not open'
    query = QtSql.QSqlQuery()
    query.exec_("insert into test values(112,'test')")
    print 'connect success'

def insert_to(key,value):
    query.exec_("insert into test values(%d,%s)"%(key,value))

def initialize_model(model):
    model.setTable('test')
    model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "index")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "value")

def show_selected(id):
    pass

def delete(id):
    query = QtSql.QSqlQuery()
    query.exec_("delete from test where value='test'")

def search_test(id):
    query = QtSql.QSqlQuery()
    query.exec_("select * from test where value like '%test%'")
