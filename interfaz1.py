# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 490)
        MainWindow.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"border-left-color: rgb(0, 0, 0);\n"
"\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(290, 90, 251, 341))
        self.listView.setStyleSheet("color: rgb(0,0,0);")
        self.listView.setObjectName("listView")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(590, 90, 256, 341))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 71, 501))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Label_Bienvenida = QtWidgets.QLabel(self.centralwidget)
        self.Label_Bienvenida.setGeometry(QtCore.QRect(90, 10, 341, 51))
        self.Label_Bienvenida.setObjectName("Label_Bienvenida")
        self.Registrarse = QtWidgets.QPushButton(self.centralwidget)
        self.Registrarse.setGeometry(QtCore.QRect(610, 390, 93, 28))
        self.Registrarse.setStyleSheet("background-color: rgb(80, 128, 142);\n"
"color: rgb(255,255,255);\n"
"border-radius:3px;")
        self.Registrarse.setObjectName("Registrarse")
        self.Entrar = QtWidgets.QPushButton(self.centralwidget)
        self.Entrar.setGeometry(QtCore.QRect(310, 390, 93, 28))
        self.Entrar.setStyleSheet("background-color: rgb(80, 128, 142);\n"
"color: rgb(255,255,255);\n"
"border-radius: 3px;")
        self.Entrar.setObjectName("Entrar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 100, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 100, 131, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 440, 31, 41))
        self.pushButton.setStyleSheet("border-image: url(:/Icons/7-removebg-preview.png);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 450, 141, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 130, 55, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(610, 150, 181, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 200, 71, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(310, 230, 181, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 130, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(610, 190, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(610, 250, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(610, 310, 71, 16))
        self.label_10.setObjectName("label_10")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(310, 150, 181, 31))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(610, 210, 181, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(610, 270, 181, 31))
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(610, 330, 181, 31))
        self.textEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_6.setObjectName("textEdit_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Label_Bienvenida.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; font-weight:600;\">TE DAMOS LA BIENVENIDA</span></p></body></html>"))
        self.Registrarse.setText(_translate("MainWindow", "Registrarse"))
        self.Entrar.setText(_translate("MainWindow", "Entrar"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">ENTRAR</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">REGISTRO</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">DESARROLLADO POR</span><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Usuario:"))
        self.label_6.setText(_translate("MainWindow", "Contrase??a:"))
        self.label_7.setText(_translate("MainWindow", "Nombre:"))
        self.label_8.setText(_translate("MainWindow", "Correo:"))
        self.label_9.setText(_translate("MainWindow", "Sucursal"))
        self.label_10.setText(_translate("MainWindow", "Contrase??a"))
from Icons import source

if __name__ == '__main__':
   import sys
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec())