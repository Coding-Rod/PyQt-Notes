from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow:
    field_1 = ''
    field_2 = ''
    result = ''
    
    def __init__(self, mainWindow):
        self.MainWindow = mainWindow
        
        with open(file='./css/pushbutton.css', mode='r') as file:
            self.pushButton_style = file.read()
        
        self.setupUi()
        
        
    def exit_message_button(self):
        msg = QMessageBox()
        msg.setWindowTitle("Exit")
        msg.setText("Are you sure you want to exit?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            sys.exit()
    
    def operation(self, operation: str):
        self.field_1 = self.lineEdit.text()
        self.field_2 = self.lineEdit_1.text()
        try:
            self.result = float(self.field_1) + float(self.field_2) if operation == '+' else float(self.field_1) - float(self.field_2)
        except ValueError:
            self.result = ''
        self.retranslateUi()
        
    def setupUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 120, 89, 25))
        self.pushButton.setStyleSheet(self.pushButton_style)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.operation('+'))
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 41)) # x, y, width, height
        self.label.setStyleSheet("color: #fff;\n"
        "background-color: rgb(114, 159, 207);\n"
        "padding-left: 10px;\n"
        "font-size: 16px;")
        self.label.setObjectName("label")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 120, 113, 25))
        self.lineEdit.setStyleSheet("border-radius: 6px;\n"
        "border 1px solid rgb(24,18,110);")
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(80, 170, 113, 25))
        self.lineEdit_1.setStyleSheet("border-radius: 6px;\n"
        "border 1px solid rgb(24,18,110);")
        self.lineEdit_1.setObjectName("lineEdit_1")
        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(80, 70, 92, 23))
        self.checkBox.setObjectName("checkBox")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 170, 89, 25))
        self.pushButton_2.setStyleSheet(self.pushButton_style)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.operation('-'))
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 180, 181, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 200, 89, 25))
        self.pushButton_3.setStyleSheet("background-color: rgb(188, 88, 88);\n"
        "color: #fff;\n"
        "border: 1px solid #eee;\n"
        "border-radius: 5px;\n"
        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.exit_message_button)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SUMA"))
        self.pushButton_2.setText(_translate("MainWindow", "RESTA"))
        self.pushButton_3.setText(_translate("MainWindow", "EXIT"))
        self.label.setText(_translate("MainWindow", "Calcula"))
        self.checkBox.setText(_translate("MainWindow", "Decimales"))
        try:
            self.label_2.setText("Resultado: "+str(self.result if self.checkBox.isChecked() else int(self.result)))
        except ValueError:
            self.label_2.setText("Resultado: ")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
