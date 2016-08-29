QApplication 用来保存所有的主题
QWidget 用户界面
QDialog
QFrame

将 GUI 界面编译为代码
pyuic4 –x demo.ui –o demo.py

signal 和 slot 机制：

比如一个 button 被点击，是这样的：

QtCore.QObject.connect(button, QtCore.SIGNAL(“clicked()”), slot_function)

或者

button.clicked.connect(slot_function)

都可以

举例，通过：QObject.connect(b1,SIGNAL("clicked()"),b1_clicked) 的方式来连接点击

QWidget 的一些基本工具

QMessageBox 用的是 ButtonClicked