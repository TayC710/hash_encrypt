import sys
from functools import partial

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PyQt5 import QtCore

import Fail
import FileEncoder
import Success
import Inter

class myFailDialog(QDialog, Fail.Ui_FailDialog):
    def __init__(self,parent=None):
        super(myFailDialog,self).__init__(parent)
        self.setupUi(self)

    def handle_click(self):
        if not self.isVisible():
            self.show()

class mySucDialog(QDialog, Success.Ui_SuccessDialog):
    def __init__(self,parent=None):
        super(mySucDialog,self).__init__(parent)
        self.setupUi(self)

    def handle_click(self):
        if not self.isVisible():
            self.show()


class myMainWindow(QMainWindow, FileEncoder.Ui_MainWindow):

    def __init__(self,parent=None):
        super(myMainWindow,self).__init__(parent)
        self.setupUi(self)

        #获取需要加密文件的路径
        file_path = self.pushButton.clicked.connect(self.chooseFile)
        #获取加密后文件的保存路径
        encode_path = self.pushButton_3.clicked.connect(self.chooseEncodePath)
        #调用加密算法
        self.pushButton_2.clicked.connect(self.encodeFile)
        #self.pushButton_2.clicked.connect(partial(self.encodeFile,filename_path = self.lineEdit.text(),encode_path = self.lineEdit_3.text()))
        #self.pushButton_2.clicked.connect(lambda : self.encodeFile(file_path,encode_path))


    # 获取需要加密文件的路径
    def chooseFile(self):
        file_path,ok=QFileDialog.getOpenFileName(self,
                                                         "选取单个文件",
                                                         ":\\",
                                                         "All Files (*);;Text Files(*.txt)")

        if ok:
            self.lineEdit.setText(str(file_path))
            print(str(file_path))
            return str(file_path)



    # 获取加密后文件的保存路径
    def chooseEncodePath(self):
        encode_path = QFileDialog.getExistingDirectory(self,
                                                           "选取指定文件夹",
                                                           ":\\")

        self.lineEdit_3.setText(str(encode_path))
        print(str(encode_path))
        return str(encode_path)

    # 调用加密算法
    def encodeFile(self):
        filename_path = self.lineEdit.text()
        encode_path = self.lineEdit_3.text()
        print("four parameters:")
        print("filename_path:",str(filename_path))
        print("encode_path:", str(encode_path))
        # 获得输入密钥
        oriKey = self.lineEdit_2.text()
        print("用户输入的密钥:",oriKey)

        # 获得选择的hash算法
        oriHash = str(self.comboBox.currentText())
        if (oriHash == 'SM3'):
            Hash = 0
        elif (oriHash == 'SHA-3'):
            Hash = 1
        elif (oriHash == 'MD5'):
            Hash = 2
        print("调用的Hash算法:",Hash)

        #--------------------调用函数-------------------
        #result =

        result = Inter.main(filename_path,encode_path,oriKey,Hash)
        print("encode file result is :",result)
        if (result == 1):
            FailDialog.handle_click()
        elif (result == 0):
            SucDialog.handle_click()
        print("结果：",result)




    def popFailDialog(self):
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

        app = QApplication(sys.argv)
        FailDialog = myFailDialog()

        #MainWindow.resize(720, 360)
        #MainWindow.setFixedSize(720, 360)

        FailDialog.show()
        print("Show了")
        # ui.pushButton.clicked.connect(choose_file(MainWindow))

        sys.exit(app.exec_())

    def popSucDialog(self):
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        app = QApplication(sys.argv)
        SucDialog = QDialog()

        # SucDialog.resize(320, 270)
        # SucDialog.setFixedSize(320, 270)

        ui = Success.Ui_SuccessDialog()
        ui.setupUi(SucDialog)
        SucDialog.show()
        sys.exit(app.exec_())
        #-----------把四个参数传入加密函数-----------












if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    MainWindow = myMainWindow()
    MainWindow.resize(720, 360)
    MainWindow.setFixedSize(720, 360)

    FailDialog = myFailDialog()
    SucDialog = mySucDialog()

    MainWindow.show()
    #ui.pushButton.clicked.connect(choose_file(MainWindow))
    sys.exit(app.exec_())

