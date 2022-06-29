from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt, ceil, floor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.StringLabel = QtWidgets.QLabel(self.centralwidget)
        self.StringLabel.setGeometry(QtCore.QRect(10, 10, 440, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StringLabel.setFont(font)
        self.StringLabel.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.StringLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.StringLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StringLabel.setText("")
        self.StringLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.StringLabel.setObjectName("StringLabel")
        
        self.EnterLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterLabel.setGeometry(QtCore.QRect(10, 70, 440, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.EnterLabel.setFont(font)
        self.EnterLabel.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.EnterLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.EnterLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EnterLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EnterLabel.setObjectName("EnterLabel")
        
        self.percent_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.percent())
        self.percent_button.setGeometry(QtCore.QRect(10, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.percent_button.setFont(font)
        self.percent_button.setObjectName("percent_button")
        
        self.clear_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("C"))
        self.clear_button.setGeometry(QtCore.QRect(100, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        
        self.back_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove())
        self.back_button.setGeometry(QtCore.QRect(190, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        
        self.change_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.change())
        self.change_button.setGeometry(QtCore.QRect(280, 130, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.change_button.setFont(font)
        self.change_button.setObjectName("change_button")

# --------------------------------------------- ADD EXTRA BUTTONS --------------------------------------------------- #
        self.round_button = QtWidgets.QPushButton(self.centralwidget)
        self.round_button.setGeometry(QtCore.QRect(370, 130, 80, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.round_button.setFont(font)
        self.round_button.setObjectName("round_button")

        self.ceil_button = QtWidgets.QPushButton(self.centralwidget)
        self.ceil_button.setGeometry(QtCore.QRect(370, 200, 80, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ceil_button.setFont(font)
        self.ceil_button.setObjectName("ceil_button")

        self.floor_button = QtWidgets.QPushButton(self.centralwidget)
        self.floor_button.setGeometry(QtCore.QRect(370, 270, 80, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.floor_button.setFont(font)
        self.floor_button.setObjectName("floor_button")

        self.pi_button = QtWidgets.QPushButton(self.centralwidget)
        self.pi_button.setGeometry(QtCore.QRect(370, 340, 80, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pi_button.setFont(font)
        self.pi_button.setObjectName("pi_button")

        self.turned_button = QtWidgets.QPushButton(self.centralwidget)
        self.turned_button.setGeometry(QtCore.QRect(370, 410, 80, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.turned_button.setFont(font)
        self.turned_button.setObjectName("turned_button")

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(370, 480, 80, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")

# -------------------------------------------------------------------------------------------------------------- #
        
        self.five_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("5"))
        self.five_button.setGeometry(QtCore.QRect(100, 340, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        
        self.four_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("4"))
        self.four_button.setGeometry(QtCore.QRect(10, 340, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        
        self.plus_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plus())
        self.plus_button.setGeometry(QtCore.QRect(280, 340, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plus_button.setFont(font)
        self.plus_button.setObjectName("plus_button")
        
        self.six_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("6"))
        self.six_button.setGeometry(QtCore.QRect(190, 340, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        
        self.square_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Square())
        self.square_button.setGeometry(QtCore.QRect(190, 200, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.square_button.setFont(font)
        self.square_button.setObjectName("square_button")
        
        self.factorial_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.factorial())
        self.factorial_button.setGeometry(QtCore.QRect(10, 200, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.factorial_button.setFont(font)
        self.factorial_button.setObjectName("factorial_button")
        
        self.multiply_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.multi())
        self.multiply_button.setGeometry(QtCore.QRect(280, 200, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.multiply_button.setFont(font)
        self.multiply_button.setObjectName("multiply_button")
        
        self.sqrt_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Square_root())
        self.sqrt_button.setGeometry(QtCore.QRect(100, 200, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sqrt_button.setFont(font)
        self.sqrt_button.setObjectName("sqrt_button")
        
        self.nine_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("9"))
        self.nine_button.setGeometry(QtCore.QRect(190, 270, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        
        self.seven_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("7"))
        self.seven_button.setGeometry(QtCore.QRect(10, 270, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        
        self.division_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.divide())
        self.division_button.setGeometry(QtCore.QRect(280, 270, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.division_button.setFont(font)
        self.division_button.setObjectName("division_button")
        
        self.eight_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("8"))
        self.eight_button.setGeometry(QtCore.QRect(100, 270, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        
        self.three_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("3"))
        self.three_button.setGeometry(QtCore.QRect(190, 410, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        
        self.one_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("1"))
        self.one_button.setGeometry(QtCore.QRect(10, 410, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        
        self.minus_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.minus())
        self.minus_button.setGeometry(QtCore.QRect(280, 410, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.minus_button.setFont(font)
        self.minus_button.setObjectName("minus_button")
        
        self.two_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("2"))
        self.two_button.setGeometry(QtCore.QRect(100, 410, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        
        self.plus_minus_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.into_negative())
        self.plus_minus_button.setGeometry(QtCore.QRect(10, 480, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plus_minus_button.setFont(font)
        self.plus_minus_button.setObjectName("plus_minus_button")
        
        self.dot_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.one_dot())
        self.dot_button.setGeometry(QtCore.QRect(190, 480, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dot_button.setFont(font)
        self.dot_button.setObjectName("dot_button")
        
        self.zero_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.display("0"))
        self.zero_button.setGeometry(QtCore.QRect(100, 480, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        
        self.equal_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculation())
        self.equal_button.setGeometry(QtCore.QRect(280, 480, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 365, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# --------------------------------------------------- LOGIC ------------------------------------------------------ #

        # call some methods from here: CORRECT WORKS!
        self.round_button.clicked.connect(self.round_number)
        self.ceil_button.clicked.connect(self.ceil_number)
        self.floor_button.clicked.connect(self.floor_number)
        self.pi_button.clicked.connect(self.show_pi)
        self.turned_button.clicked.connect(self.turn_number)
        self.exit_button.clicked.connect(MainWindow.close)
    
    # define methods for π button: CORRECT WORKS!
    def show_pi(self):
        screen = self.EnterLabel.text()
        self.EnterLabel.setText(f'{screen}3.14159')
    
    # define turn_number method for turned button: CORRECT WORKS!
    def turn_number(self):
        screen = self.EnterLabel.text()
        try:
            screen = float(screen)
            self.StringLabel.setText(f'1/{screen}')
        except:
            a = float(eval(self.EnterLabel.text()))
            self.StringLabel.setText(f'1/{a}')

    # define ceil method for ceil button: CORRECT WORKS!
    def ceil_number(self):
        screen = self.EnterLabel.text()
        try:
            screen = ceil(float(screen))
            self.StringLabel.setText(f'{screen}')
        except:
            a = ceil(float(eval(self.EnterLabel.text())))
            self.StringLabel.setText(f'{a}')
    
    # define floor method for floor button: CORRECT WORKS!
    def floor_number(self):
        screen = self.EnterLabel.text()
        try:
            screen = floor(float(screen))
            self.StringLabel.setText(f'{screen}')
        except:
            a = floor(float(eval(self.EnterLabel.text())))
            self.StringLabel.setText(f'{a}')
    
    # define round method for round button: CORRECT WORKS!
    def round_number(self):
        screen = self.EnterLabel.text()
        try:
            screen = round(float(screen), 2)
            self.StringLabel.setText(f'{screen}')
        except:
            a = round(float(eval(self.EnterLabel.text())), 2)
            self.StringLabel.setText(f'{a}')
    
    # define display method: CORRECT WORKS!
    def display(self, pressed):
        if pressed == "C":
            self.StringLabel.setText("")
            self.EnterLabel.setText("")
        else:
            if self.EnterLabel.text() == "0" and pressed == ".":
                self.EnterLabel.setText(f'{self.EnterLabel.text()}')
            elif self.EnterLabel.text() == "0":
                self.EnterLabel.setText("")
            self.EnterLabel.setText(f'{self.EnterLabel.text()}{pressed}')
        
    # define only one dot between calculation operators: CORRECT WORKS!
    def one_dot(self):
        screen = self.EnterLabel.text()
        action = ["*", "/", "+", "-"]

        for i in action:
            if i not in screen and "." not in screen:
                self.EnterLabel.setText(f'{screen}.')
        
        for i in action: 
            pos = screen.find(i)   
            if i in screen and "." not in screen[pos:]:
                self.EnterLabel.setText(f'{screen}.')

    # only one operation should be possible: CORRECT WORKS!
    def plus(self):
        screen = self.EnterLabel.text()
        if "+" not in screen:
            self.EnterLabel.setText(f'{screen}+')
        if "*" in screen or "/" in screen or screen.count("-") == 2:
            self.EnterLabel.setText(f'{screen}')
        if "-" in screen and screen[0] != "-":
            self.EnterLabel.setText(f'{screen}')

    def minus(self):
        screen = self.EnterLabel.text()
        if screen.count("-") <= 1:
            self.EnterLabel.setText(f'{screen}-')
        if len(screen) == 0:
            self.EnterLabel.setText(f'-{screen}')
        elif "-" in screen[-1]:
            self.EnterLabel.setText(f'{screen}')
        if screen.count("-") == 2:
            self.EnterLabel.setText(f'{screen}')
        if "*" in screen or "/" in screen or "+" in screen:
            self.EnterLabel.setText(f'{screen}')
        if "-" in screen and screen[0] != "-":
            self.EnterLabel.setText(f'{screen}')
                           
    def multi(self):
        screen = self.EnterLabel.text()
        if "*" not in screen:
            self.EnterLabel.setText(f'{screen}*')
        if "+" in screen or "/" in screen or screen.count("-") == 2:
            self.EnterLabel.setText(f'{screen}')
        if "-" in screen and screen[0] != "-":
            self.EnterLabel.setText(f'{screen}')
    
    def divide(self):
        screen = self.EnterLabel.text()
        if "/" not in screen:
            self.EnterLabel.setText(f'{screen}/')
        if "*" in screen or "+" in screen or screen.count("-") == 2:
            self.EnterLabel.setText(f'{screen}')
        if "-" in screen and screen[0] != "-":
            self.EnterLabel.setText(f'{screen}')

    # define calculaion method: CORRECT WORKS! 
    def calculation(self):
        screen = self.EnterLabel.text()
        symbols = ["*", "/", "+", "-"]
        try:
            for i in symbols:
                if i in screen and (i == "+" or i == "/" or i == "*" or i == "-"):
                    self.StringLabel.setText(str(eval(self.EnterLabel.text())))

        except ZeroDivisionError:
            self.EnterLabel.setText("ERROR")

    # define into_negative method for plus_minus button: CORRECT WORKS!
    def into_negative(self):
        screen = self.EnterLabel.text()
        try:
            number = float(screen)
            if "-" not in screen:
                self.StringLabel.setText(f'-{screen}')
                self.EnterLabel.setText(f'-abs({screen})')
            
            if "-" in screen:
                self.StringLabel.setText(f'{str(number*(-1))}')
                self.EnterLabel.setText(f'abs({screen})')
        except ValueError:
            if (screen[0] == "-" and screen.count("-") == 2) or ("-" not in screen and ("*" in screen or "+" in screen or "/" in screen)):
                a = float(eval(self.EnterLabel.text())) * (-1)
                self.StringLabel.setText(f'{a}')
            elif "-" in screen and ("*" in screen or "+" in screen or "/" in screen):
                a = float(eval(self.EnterLabel.text())) * (-1)
                self.StringLabel.setText(f'{a}')
            elif "-" in screen and ("*" not in screen or "+" not in screen or "/" not in screen):
                a = float(eval(self.EnterLabel.text())) * (-1)
                self.StringLabel.setText(f'{a}')
                 
    # define Value change method, from StringLabel into EnterLabel: CORRECT WORKS!
    def change(self):
        answer = self.StringLabel.text()
        self.EnterLabel.setText(f'{answer}')
        self.StringLabel.setText("")

    # define back remove function: CORRECT WORKS!
    def remove(self):
        screen = self.EnterLabel.text()
        screen = screen[:-1]
        self.EnterLabel.setText(screen)
    
    # define SQUARE method: CORRECT WORKS!
    def Square(self):
        screen = self.EnterLabel.text()
        try:
            number = float(screen)
            answer = number**2
            self.StringLabel.setText(str(answer))
            self.EnterLabel.setText(f'{screen}**2')
        except:
            a = float(eval(self.EnterLabel.text()))
            self.StringLabel.setText(f'{a**2}')
            self.EnterLabel.setText(f'{a}**2')
      
    # define SQRT method: CORRECT WORKS!
    def Square_root(self):
        screen = self.EnterLabel.text()
        try:
            number = float(screen)
            answer = sqrt(number)
            self.StringLabel.setText(str(answer))
            self.EnterLabel.setText(f'√{screen}')
        except:
            try:
                a = float(eval(self.EnterLabel.text()))
                self.StringLabel.setText(f'{sqrt(a)}')
                self.EnterLabel.setText(f'√{a}')
            except ValueError:
                self.StringLabel.setText("√-x")
                self.EnterLabel.setText("Negative number doesn't have Root")
    
    # define percentage method: CORRECT WORKS!
    def percent(self):
        screen = self.EnterLabel.text()
        try:
            number = float(screen)
            answer = number / 100
            self.StringLabel.setText(str(answer))
            self.EnterLabel.setText(f'{screen}%')
        except:
            a = float(eval(self.EnterLabel.text()))
            self.StringLabel.setText(f'{a / 100}')
            self.EnterLabel.setText(f'{a}%')
    
    # define factorial method:  CORRECT WORKS!  
    def factorial(self):
        screen = self.EnterLabel.text()
        try:
            answer = int(screen)
            if answer <= 2:
                self.StringLabel.setText(str(answer))
            else:
                for i in range(2, answer):
                    answer = answer * i
                self.StringLabel.setText(str(answer))
                self.EnterLabel.setText(f'{screen}!')
        except:
            self.EnterLabel.setText("Object Must Be Integer!")

# ------------------------------------------------ END --------------------------------------------------------- #
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EnterLabel.setText(_translate("MainWindow", ""))
        self.percent_button.setText(_translate("MainWindow", "%"))
        self.clear_button.setText(_translate("MainWindow", "C"))
        self.back_button.setText(_translate("MainWindow", "<<"))
        self.change_button.setText(_translate("MainWindow", "↑↓"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.square_button.setText(_translate("MainWindow", "^"))
        self.factorial_button.setText(_translate("MainWindow", "!"))
        self.multiply_button.setText(_translate("MainWindow", "*"))
        self.sqrt_button.setText(_translate("MainWindow", "√"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.division_button.setText(_translate("MainWindow", "/"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.plus_minus_button.setText(_translate("MainWindow", "+/-"))
        self.dot_button.setText(_translate("MainWindow", "."))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.round_button.setText(_translate("MainWindow", "≈"))
        self.ceil_button.setText(_translate("MainWindow", "Ceil"))
        self.floor_button.setText(_translate("MainWindow", "Floor"))
        self.pi_button.setText(_translate("MainWindow", "π"))
        self.turned_button.setText(_translate("MainWindow", "1/x"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
