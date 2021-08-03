from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from functools import partial
from random import sample
import sys,RandomNumber

#"作者个人Github地址-点击跳转"按钮2
def click_success2():
    QDesktopServices.openUrl(QUrl("https://github.com/YCYAX"))

#"点击获取抽取结果↓"按钮1
def click_success(ui):
    MinNumber = ui.lineEdit.text()
    MaxNumber = ui.lineEdit_2.text()
    PeopleNmuber = ui.lineEdit_3.text()
    try:
        result = sample(range(int(MinNumber), int(MaxNumber)), int(PeopleNmuber))
        ui.lineEdit_4.setText("结果为"+str(result))
    except:
        ui.lineEdit_4.setText('前三个数值有不是整数的数值')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = RandomNumber.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton_2.clicked.connect(click_success2)
    ui.pushButton.clicked.connect(partial(click_success,ui))
    sys.exit(app.exec_())