from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

# creating a GUI window class and passing object as an arg
class UiWindow(object):

    # defining a setup function which will create the GUI window and it's contents
    def SetupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(292, 439)
        Window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Window.setFocusPolicy(QtCore.Qt.StrongFocus)
        Window.setStyleSheet("background-color: rgb(0, 0, 0);")

        # initialize central widget and the style sheet for it
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setStyleSheet(
            # Number line display styles
            "QLineEdit#numberline\n"
            "{\n"
            "    border:none;\n"
            "    color: white;\n"
            "    font-family: Arial;\n"
            "    font-size: 45px;\n"
            "}\n"
            "\n"
            "QLineEdit#numberline_2\n"
            "{\n"
            "	border: none;\n"
            "	color: white;\n"
            "	font-family: Arial;\n"
            "	font-size: 18px;\n"
            "}\n"
            "\n"
            # Numbers and dot button styles
            "QPushButton#b0\n"
            "{\n"
            "    background-color:rgb(51, 51, 51);\n"
            "    color: rgb(255, 255, 255);\n"
            "    font-family: Arial;\n"
            "    font-size: 20px;\n"
            "    border-radius:25px;\n"
            "    font-weight: bold;\n"
            "    max-width:125px;\n"
            "    max-height:50px;\n"
            "    min-width:50px;\n"
            "    min-height:50px;\n"
            "}\n"
            "\n"
            "QPushButton#b1,#b2,#b3,#b4,#b5,#b6,#b7,#b8,#b9,#bdot\n"
            "{\n"
            "    background-color:rgb(51, 51, 51);\n"
            "    color: rgb(255, 255, 255);\n"
            "    font-family: Arial;\n"
            "    font-size: 20px;\n"
            "    border-radius:25px;\n"
            "    font-weight: bold;\n"
            "    max-width:50px;\n"
            "    max-height:50px;\n"
            "    min-width:50px;\n"
            "    min-height:50px;\n"
            "}\n"
            "\n"
            "QPushButton:hover#b0\n"
            "{\n"
            "    background-color:rgb(125, 125, 125)\n"
            "}\n"
            "\n"
            "QPushButton:hover#b1,:hover#b2,:hover#b3,:hover#b4,:hover#b4,:hover#b5,:hover#b6,:hover#b7,:hover#b8,:hover#b9,:hover#bdot\n"
            "{\n"
            "    background-color:rgb(125, 125, 125)\n"
            "}\n"
            "\n"
            
            # Operator button styles
            "QPushButton#bdivide,#btimes,#bminus,#bplus,#bequals\n"
            "{\n"
            "    background-color:rgb(254, 149, 4);\n"
            "    color: rgb(255, 255, 255);\n"
            "    font-family: Arial;\n"
            "    font-size: 20px;\n"
            "    border-radius:25px;\n"
            "    font-weight: bold;\n"
            "    max-width:50px;\n"
            "    max-height:50px;\n"
            "    min-width:50px;\n"
            "    min-height:50px;\n"
            "}\n"
            "\n"
            "QPushButton:hover#bdivide,:hover#btimes,:hover#bminus,:hover#bplus,:hover#bequals\n"
            "{\n"
            "    background-color:rgb(254, 183, 5);\n"
            "}\n"
            "\n"
            "\n"
            
            # Clear, clear entry and +/- button styles
            "QPushButton#bclear,#bclearentry,#bpandm\n"
            "{\n"
            "    background-color:rgb(165,165,165);\n"
            "    color: rgb(0, 0, 0);\n"
            "    font-family: Arial;\n"
            "    font-size: 20px;\n"
            "    border-radius:25px;\n"
            "    font-weight: bold;\n"
            "    max-width:50px;\n"
            "    max-height:50px;\n"
            "    min-width:50px;\n"
            "    min-height:50px;\n"
            "}\n"
            "\n"
            "QPushButton:hover#bclear,:hover#bclearentry,:hover#bpandm\n"
            "{\n"
            "    background-color:rgb(202, 202, 202);\n"
            "}\n"
            "")


        # creating all buttons and lineedits within the GUI
        self.centralwidget.setObjectName("centralwidget")

        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(30, 360, 111, 50))
        self.b0.setObjectName("b0")
        self.b0.clicked.connect(partial(self.clicked_number, "0"))

        self.bdot = QtWidgets.QPushButton(self.centralwidget)
        self.bdot.setGeometry(QtCore.QRect(150, 360, 50, 50))
        self.bdot.setObjectName("bdot")
        self.bdot.clicked.connect(partial(self.clicked_number, "."))

        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(30, 300, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(partial(self.clicked_number, "1"))

        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(90, 300, 50, 50))
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(partial(self.clicked_number, "2"))

        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(150, 300, 50, 50))
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(partial(self.clicked_number, "3"))

        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(30, 240, 50, 50))
        self.b4.setObjectName("b4")
        self.b4.clicked.connect(partial(self.clicked_number, "4"))

        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(90, 240, 50, 50))
        self.b5.setObjectName("b5")
        self.b5.clicked.connect(partial(self.clicked_number, "5"))

        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(150, 240, 50, 50))
        self.b6.setObjectName("b6")
        self.b6.clicked.connect(partial(self.clicked_number, "6"))

        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(30, 180, 50, 50))
        self.b7.setObjectName("b7")
        self.b7.clicked.connect(partial(self.clicked_number, "7"))

        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(90, 180, 50, 50))
        self.b8.setObjectName("b8")
        self.b8.clicked.connect(partial(self.clicked_number, "8"))

        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(150, 180, 50, 50))
        self.b9.setObjectName("b9")
        self.b9.clicked.connect(partial(self.clicked_number, "9"))

        self.bplus = QtWidgets.QPushButton(self.centralwidget)
        self.bplus.setGeometry(QtCore.QRect(210, 300, 50, 50))
        self.bplus.setObjectName("bplus")
        self.bplus.clicked.connect(partial(self.clicked_operator, "+"))

        self.bequals = QtWidgets.QPushButton(self.centralwidget)
        self.bequals.setGeometry(QtCore.QRect(210, 360, 50, 50))
        self.bequals.setObjectName("bequals")
        self.bequals.clicked.connect(self.clicked_equals)

        self.bminus = QtWidgets.QPushButton(self.centralwidget)
        self.bminus.setGeometry(QtCore.QRect(210, 240, 50, 50))
        self.bminus.setObjectName("bminus")
        self.bminus.clicked.connect(partial(self.clicked_operator, "-"))

        self.btimes = QtWidgets.QPushButton(self.centralwidget)
        self.btimes.setGeometry(QtCore.QRect(210, 180, 50, 50))
        self.btimes.setObjectName("btimes")
        self.btimes.clicked.connect(partial(self.clicked_operator, "×"))

        self.bdivide = QtWidgets.QPushButton(self.centralwidget)
        self.bdivide.setGeometry(QtCore.QRect(210, 120, 50, 50))
        self.bdivide.setObjectName("bdivide")
        self.bdivide.clicked.connect(partial(self.clicked_operator, "÷"))

        self.bclearentry = QtWidgets.QPushButton(self.centralwidget)
        self.bclearentry.setGeometry(QtCore.QRect(30, 120, 50, 50))
        self.bclearentry.setObjectName("bclearentry")
        self.bclearentry.clicked.connect(self.clicked_ce)

        self.bclear = QtWidgets.QPushButton(self.centralwidget)
        self.bclear.setGeometry(QtCore.QRect(90, 120, 50, 50))
        self.bclear.setObjectName("bclear")
        self.bclear.clicked.connect(self.clicked_clear)

        self.bpandm = QtWidgets.QPushButton(self.centralwidget)
        self.bpandm.setGeometry(QtCore.QRect(150, 120, 50, 50))
        self.bpandm.setObjectName("bpandm")
        self.bpandm.clicked.connect(self.clicked_pandm)

        self.numberline = QtWidgets.QLineEdit(self.centralwidget)
        self.numberline.setGeometry(QtCore.QRect(31, 50, 229, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.numberline.setFont(font)
        self.numberline.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.numberline.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.numberline.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numberline.setObjectName("numberline")
        self.numberline.setText("0")
        self.numberline.setMaxLength(9)

        self.numberline_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.numberline_2.setGeometry(QtCore.QRect(30, 25, 229, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.numberline_2.setFont(font)
        self.numberline_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.numberline_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.numberline_2.setText("")
        self.numberline_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.numberline_2.setObjectName("numberline_2")

        Window.setCentralWidget(self.centralwidget)

        self.RetranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)


    # sets the text on all buttons and gives the GUI window it's title
    def RetranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Calculator"))
        self.b0.setText(_translate("Window", "0"))
        self.bdot.setText(_translate("Window", "."))
        self.bequals.setText(_translate("Window", "="))
        self.b1.setText(_translate("Window", "1"))
        self.b2.setText(_translate("Window", "2"))
        self.b3.setText(_translate("Window", "3"))
        self.bplus.setText(_translate("Window", "+"))
        self.b4.setText(_translate("Window", "4"))
        self.b5.setText(_translate("Window", "5"))
        self.b6.setText(_translate("Window", "6"))
        self.bminus.setText(_translate("Window", "−"))
        self.b7.setText(_translate("Window", "7"))
        self.b8.setText(_translate("Window", "8"))
        self.b9.setText(_translate("Window", "9"))
        self.btimes.setText(_translate("Window", "×"))
        self.bdivide.setText(_translate("Window", "÷"))
        self.bclearentry.setText(_translate("Window", "CE"))
        self.bclear.setText(_translate("Window", "C"))
        self.bpandm.setText(_translate("Window", "+/-"))

    # this slot (function) is activated when a signal is emitted from one of the number buttons/dot
    # it displays the numbers/dot in the main number line
    def clicked_number(self, button_num):
        if self.numberline.text() == "0" and button_num == ".":
            pass
        elif self.numberline.text() == "0":
            self.numberline.setText("")
        elif self.numberline.text() == "ERROR":
            self.numberline.setText("")

        current_num = self.numberline.text()
        self.numberline.setText(current_num + button_num)


    # this slot is used for any operator buttons, it also takes the current expression and puts it
    # in the second number line above the first
    def clicked_operator(self, operator):
        if self.numberline.text() == "0" and operator == "-":
            self.numberline.setText("")
        elif self.numberline.text() == "ERROR":
            self.numberline.setText("")
        current_expr = self.numberline.text()
        self.numberline_2.setText(current_expr + " " + operator)
        self.numberline.setText("")


    # here is where the current expression is evaulated and presented as an answer
    # this function also handles any errors that occur
    def clicked_equals(self):
        try:
            total = self.numberline_2.text() + self.numberline.text()
            total = total.replace("×", "*").replace("÷", "/")
            total = eval(total)
            if total - int(total) == 0:
                total = int(total)
            self.numberline_2.setText(self.numberline_2.text() + " " + self.numberline.text() + " " + "=")
            self.numberline.setText(str(total))
        except:
            self.numberline.setText("ERROR")


    # clears both number lines
    def clicked_clear(self):
        self.numberline_2.setText("")
        self.numberline.setText("0")


    # clears only bottom/first numberline
    def clicked_ce(self):
        self.numberline.setText("")


    # converts any positive number into negative and vice versa
    def clicked_pandm(self):
        curr_num = int(self.numberline.text()) * -1
        self.numberline.setText(str(curr_num))


# creates instances and runs the program
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = UiWindow()
    ui.SetupUi(Window)
    Window.show()
    sys.exit(app.exec_())
