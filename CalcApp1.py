from PyQt5 import QtCore, QtGui, QtWidgets
from sympy import *
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1043, 834)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(320, 40, 401, 701))
        self.frame.setStyleSheet("border-image: url(Phone.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 480, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(360, 140, 321, 101))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("background-color: #292929;\n"
"color:white")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.lineEdit.insert('1'))
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 480, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:self.lineEdit.insert('2'))
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 480, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda:self.lineEdit.insert('3'))
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 520, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda:self.lineEdit.insert('4'))
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 520, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda:self.lineEdit.insert('5'))
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 560, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda:self.lineEdit.insert('7'))
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 560, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda:self.lineEdit.insert('8'))
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(470, 560, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda:self.lineEdit.insert('9'))
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(470, 520, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda:self.lineEdit.insert('6'))
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(370, 600, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda:self.lineEdit.insert('0'))
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(420, 600, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda:self.lineEdit.insert('.'))
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(470, 600, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(lambda:self.delete())
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(560, 520, 41, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color:#bdc3c3;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:#5c5c5c;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:#343434;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(lambda:self.lineEdit.insert('+'))
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(560, 600, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 0, 255);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 85, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(lambda:self.MathBrain())
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(560, 480, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color:#bdc3c3;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:#5c5c5c;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:#343434;\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(lambda:self.lineEdit.insert('-'))
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(610, 560, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color:#bdc3c3;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:#5c5c5c;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:#343434;\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(lambda:self.lineEdit.insert('/'))
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(610, 520, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color:#bdc3c3;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:#5c5c5c;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:#343434;\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(lambda:self.lineEdit.insert('*'))
        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(370, 430, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color:#bdc3c3;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:#5c5c5c;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:#343434;\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(lambda:self.lineEdit.insert('('))
        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(440, 430, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color:#bdc3c3;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:#5c5c5c;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:#343434;\n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(lambda:self.lineEdit.insert(')'))
        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(560, 430, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(self.lineEdit.clear)
        self.pushButton_21 = QtWidgets.QPushButton(Form)
        self.pushButton_21.setGeometry(QtCore.QRect(610, 430, 41, 31))
        font = QtGui.QFont()
        font.setFamily("font bottons music pro")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(85, 85, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(85, 85, 255);\n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.clicked.connect(lambda:self.OpenMusic())
        self.pushButton_22 = QtWidgets.QPushButton(Form)
        self.pushButton_22.setGeometry(QtCore.QRect(610, 480, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color:rgb(255, 170, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(255, 85, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(255, 0, 0);\n"
"}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(lambda:self.lineEdit.insert('x'))
        self.pushButton_23 = QtWidgets.QPushButton(Form)
        self.pushButton_23.setGeometry(QtCore.QRect(360, 370, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color:rgb(255, 170, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(255, 85, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(255, 0, 0);\n"
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(lambda:self.lineEdit.insert("integrate()"))
        self.pushButton_24 = QtWidgets.QPushButton(Form)
        self.pushButton_24.setGeometry(QtCore.QRect(540, 370, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color:rgb(255, 170, 127);\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(255, 85, 0);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(255, 0, 0);\n"
"}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.clicked.connect(lambda:self.lineEdit.insert("diff()"))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 300, 321, 41))
        self.label.setStyleSheet("color:#bdc3c3;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_25 = QtWidgets.QPushButton(Form)
        self.pushButton_25.setGeometry(QtCore.QRect(490, 670, 61, 61))
        self.pushButton_25.setStyleSheet("QPushButton{\n"
"border-radius:30px;\n"
"background-color:white;\n"
"border: 3px solid grey;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border: 4px solid grey;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border: 5px solid grey;\n"
"}\n"
"")
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_25.clicked.connect(lambda:self.close())
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 634, 351, 21))
        self.label_2.setStyleSheet("color:#bdc3c3;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(360, 250, 321, 51))
        self.textBrowser.setStyleSheet("background-color: #292929;\n"
"color:white")
        self.textBrowser.setObjectName("textBrowser") 

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "7"))
        self.pushButton_7.setText(_translate("Form", "8"))
        self.pushButton_8.setText(_translate("Form", "9"))
        self.pushButton_9.setText(_translate("Form", "6"))
        self.pushButton_10.setText(_translate("Form", "0"))
        self.pushButton_11.setText(_translate("Form", "."))
        self.pushButton_12.setText(_translate("Form", "C"))
        self.pushButton_13.setText(_translate("Form", "+"))
        self.pushButton_14.setText(_translate("Form", "="))
        self.pushButton_15.setText(_translate("Form", "-"))
        self.pushButton_16.setText(_translate("Form", "÷"))
        self.pushButton_17.setText(_translate("Form", "×"))
        self.pushButton_18.setText(_translate("Form", "("))
        self.pushButton_19.setText(_translate("Form", ")"))
        self.pushButton_20.setText(_translate("Form", "AC"))
        self.pushButton_21.setText(_translate("Form", "a"))
        self.pushButton_22.setText(_translate("Form", "X"))
        self.pushButton_23.setText(_translate("Form", "Integral"))
        self.pushButton_24.setText(_translate("Form", "Derivative"))
        self.label.setText(_translate("Form", "Easy-to-use integral and derivative calculator with audio playback"))
        self.label_2.setText(_translate("Form", "All right reserved. Jakub Kiełb 2022 ©"))
        self.lineEdit.setPlaceholderText(_translate("Form", "E.G log(x)+sin(x)+5*cos(2*x)+6*x"))
        self.textBrowser.setPlaceholderText(_translate("Form", "Output"))
    def MathBrain(self):
            import scipy.integrate
            from sympy import sin, cos,tan,sqrt, Function, diff, sqrt,log, pi ,acos ,asin ,atan,symbols
            from math import e
            x=symbols('x')
            line=self.lineEdit.text()
            try:
                DoMath=eval(line)
                self.textBrowser.setText(str(DoMath))
            except ZeroDivisionError:
                self.textBrowser.setText("Don't divide by zero!")

    def OpenMusic(self):
            import winsound
            winsound.PlaySound(r'Song1.wav', winsound.SND_ASYNC)
    def delete(self):
            line=self.lineEdit.text()
            LineList=list(line)
            LineList=LineList[:-1]
            self.lineEdit.setText(''.join(map(str, LineList)))
    def close(self):
        self.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())