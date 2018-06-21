#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[Author] : KeyLo99
[Contact] : twitter.com/KeyLo_99
"""

"""PyQT4"""

from PyQt4 import QtCore, QtGui
import sys, os
from PyQt4.Qt import *
from src import ducky_compiler


commands = ["REM", "DELAY", "STRING", "GUI", "MENU", "SHIFT", "ALT", "CTRL",
            "DOWN", "LEFT", "RIGHT", "UP", "BREAK", "CAPSLOCK", "DELETE", "END", "ESC", "HOME",
            "INSERT", "NUMLOCK", "PAGEUP", "PAGEDOWN", "PRINTSCREEN", "SCROLLLOCK", "SPACE", "TAB", "REPLAY", "ENTER"]
global realtime
realtime = True
global currentLine

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(532, 555)
        MainWindow.setMinimumSize(QtCore.QSize(532, 555))
        MainWindow.setMaximumSize(QtCore.QSize(532, 555))
        MainWindow.setStyleSheet("background-color:#222;")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 531, 531))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet("background-color : #222;")
        self.tabWidget.setObjectName("tabWidget")
        self.tabMain = QtGui.QWidget()
        self.tabMain.setStyleSheet("")
        self.tabMain.setObjectName("tabMain")
        self.lblPic = QtGui.QLabel(self.tabMain)
        self.lblPic.setGeometry(QtCore.QRect(0, 0, 555, 521))
        self.lblPic.setStyleSheet("background-color:#181829;")
        self.lblPic.setText("")
        self.lblPic.setObjectName("lblPic")
        self.tabWidget.addTab(self.tabMain, "")
        self.tabCompiler = QtGui.QWidget()
        self.tabCompiler.setObjectName("tabCompiler")
        self.progressBar = QtGui.QProgressBar(self.tabCompiler)
        self.progressBar.setGeometry(QtCore.QRect(10, 480, 501, 16))
        self.progressBar.setStyleSheet("color:white;")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.txDucky = QtGui.QTextEdit(self.tabCompiler)
        self.txDucky.setGeometry(QtCore.QRect(10, 120, 501, 151))
        self.txDucky.setStyleSheet("background-color:white; color:black;")
        self.txDucky.setObjectName("txDucky")
        self.lblInput = QtGui.QLabel(self.tabCompiler)
        self.lblInput.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblInput.setFont(font)
        self.lblInput.setStyleSheet("color:white;")
        self.lblInput.setObjectName("lblInput")
        self.leDelay = QtGui.QLineEdit(self.tabCompiler)
        self.leDelay.setGeometry(QtCore.QRect(180, 70, 41, 20))
        self.leDelay.setStyleSheet("color:white;")
        self.leDelay.setObjectName("leDelay")
        self.pbCompile = QtGui.QPushButton(self.tabCompiler)
        self.pbCompile.setGeometry(QtCore.QRect(310, 70, 191, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbCompile.setFont(font)
        self.pbCompile.setStyleSheet("background-color:white; color:green;")
        self.pbCompile.setObjectName("pbCompile")
        self.lblArduinoCode = QtGui.QLabel(self.tabCompiler)
        self.lblArduinoCode.setGeometry(QtCore.QRect(10, 280, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblArduinoCode.setFont(font)
        self.lblArduinoCode.setStyleSheet("color:white;")
        self.lblArduinoCode.setObjectName("lblArduinoCode")
        self.pbIBrowse = QtGui.QPushButton(self.tabCompiler)
        self.pbIBrowse.setGeometry(QtCore.QRect(410, 8, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbIBrowse.setFont(font)
        self.pbIBrowse.setStyleSheet("background-color:white;")
        self.pbIBrowse.setObjectName("pbIBrowse")
        self.leInput = QtGui.QLineEdit(self.tabCompiler)
        self.leInput.setGeometry(QtCore.QRect(80, 10, 321, 20))
        self.leInput.setStyleSheet("background-color:white;")
        self.leInput.setObjectName("leInput")
        self.lblOutput = QtGui.QLabel(self.tabCompiler)
        self.lblOutput.setGeometry(QtCore.QRect(10, 40, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblOutput.setFont(font)
        self.lblOutput.setStyleSheet("color:white;")
        self.lblOutput.setObjectName("lblOutput")
        self.cbxFunc = QtGui.QCheckBox(self.tabCompiler)
        self.cbxFunc.setGeometry(QtCore.QRect(230, 70, 70, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cbxFunc.setFont(font)
        self.cbxFunc.setStyleSheet("color:white;")
        self.cbxFunc.setObjectName("cbxFunc")
        self.lblDelay = QtGui.QLabel(self.tabCompiler)
        self.lblDelay.setGeometry(QtCore.QRect(10, 70, 161, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDelay.setFont(font)
        self.lblDelay.setStyleSheet("color:white;")
        self.lblDelay.setObjectName("lblDelay")
        self.txArduinoCode = QtGui.QTextEdit(self.tabCompiler)
        self.txArduinoCode.setGeometry(QtCore.QRect(10, 300, 501, 171))
        self.txArduinoCode.setStyleSheet("background-color:white; color:black;")
        self.txArduinoCode.setObjectName("txArduinoCode")
        self.leOutput = QtGui.QLineEdit(self.tabCompiler)
        self.leOutput.setGeometry(QtCore.QRect(80, 40, 321, 20))
        self.leOutput.setStyleSheet("background-color:white;")
        self.leOutput.setObjectName("leOutput")
        self.lblDuckyScript = QtGui.QLabel(self.tabCompiler)
        self.lblDuckyScript.setGeometry(QtCore.QRect(10, 100, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDuckyScript.setFont(font)
        self.lblDuckyScript.setStyleSheet("color:white;")
        self.lblDuckyScript.setObjectName("lblDuckyScript")
        self.pbOBrowse = QtGui.QPushButton(self.tabCompiler)
        self.pbOBrowse.setGeometry(QtCore.QRect(410, 38, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbOBrowse.setFont(font)
        self.pbOBrowse.setStyleSheet("background-color:white;")
        self.pbOBrowse.setObjectName("pbOBrowse")
        self.lblSuccess = QtGui.QLabel(self.tabCompiler)
        self.lblSuccess.setGeometry(QtCore.QRect(310, 100, 201, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSuccess.setFont(font)
        self.lblSuccess.setStyleSheet("color : lime;")
        self.lblSuccess.setObjectName("lblSuccess")
        self.tabWidget.addTab(self.tabCompiler, "")
        self.tabCreator = QtGui.QWidget()
        self.tabCreator.setObjectName("tabCreator")
        self.teCreated = QtGui.QTextEdit(self.tabCreator)
        self.teCreated.setGeometry(QtCore.QRect(10, 60, 501, 391))
        self.teCreated.setStyleSheet("background-color:white; color:black")
        self.teCreated.setObjectName("teCreated")
        self.pbCC = QtGui.QPushButton(self.tabCreator)
        self.pbCC.setGeometry(QtCore.QRect(360, 460, 151, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbCC.setFont(font)
        self.pbCC.setStyleSheet("background-color:white; color:darkorange;")
        self.pbCC.setObjectName("pbCC")
        self.lblCommand = QtGui.QLabel(self.tabCreator)
        self.lblCommand.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCommand.setFont(font)
        self.lblCommand.setStyleSheet("color:white;")
        self.lblCommand.setObjectName("lblCommand")
        self.cbxCommand = QtGui.QComboBox(self.tabCreator)
        self.cbxCommand.setGeometry(QtCore.QRect(80, 10, 91, 22))
        self.cbxCommand.setStyleSheet("background-color:white; color:black")
        self.cbxCommand.setObjectName("cbxCommand")
        self.lblKey = QtGui.QLabel(self.tabCreator)
        self.lblKey.setGeometry(QtCore.QRect(190, 10, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblKey.setFont(font)
        self.lblKey.setStyleSheet("color:white;")
        self.lblKey.setObjectName("lblKey")
        self.leKey = QtGui.QLineEdit(self.tabCreator)
        self.leKey.setGeometry(QtCore.QRect(262, 10, 101, 20))
        self.leKey.setStyleSheet("background-color:white; color:black;")
        self.leKey.setObjectName("leKey")
        self.cbxKey = QtGui.QComboBox(self.tabCreator)
        self.cbxKey.setGeometry(QtCore.QRect(262, 33, 101, 20))
        self.cbxKey.setStyleSheet("background-color:white; color:black")
        self.cbxKey.setObjectName("cbxKey")
        self.pbAdd = QtGui.QPushButton(self.tabCreator)
        self.pbAdd.setGeometry(QtCore.QRect(410, 10, 101, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbAdd.setFont(font)
        self.pbAdd.setStyleSheet("background-color:white; color:green;")
        self.pbAdd.setObjectName("pbAdd")
        self.lblDuckyScript_2 = QtGui.QLabel(self.tabCreator)
        self.lblDuckyScript_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDuckyScript_2.setFont(font)
        self.lblDuckyScript_2.setStyleSheet("color:white;")
        self.lblDuckyScript_2.setObjectName("lblDuckyScript_2")
        self.cbxRealTimeCreate = QtGui.QCheckBox(self.tabCreator)
        self.cbxRealTimeCreate.setGeometry(QtCore.QRect(410, 37, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cbxRealTimeCreate.setFont(font)
        self.cbxRealTimeCreate.setStyleSheet("color:white;")
        self.cbxRealTimeCreate.setObjectName("cbxRealTimeCreate")
        self.pbClear = QtGui.QPushButton(self.tabCreator)
        self.pbClear.setGeometry(QtCore.QRect(10, 460, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbClear.setFont(font)
        self.pbClear.setStyleSheet("background-color:white;")
        self.pbClear.setObjectName("pbClear")
        self.pbCSave = QtGui.QPushButton(self.tabCreator)
        self.pbCSave.setGeometry(QtCore.QRect(90, 460, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbCSave.setFont(font)
        self.pbCSave.setStyleSheet("background-color:white;")
        self.pbCSave.setObjectName("pbCSave")
        self.tabWidget.addTab(self.tabCreator, "")
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LeonarDucky v1.0 | DuckyScript Converter & Generator | Coded by KeyLo99"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain), _translate("MainWindow", "Main"))
        self.lblInput.setText(_translate("MainWindow", "Input File:"))
        self.leDelay.setText(_translate("MainWindow", "500"))
        self.pbCompile.setText(_translate("MainWindow", "Compile"))
        self.lblArduinoCode.setText(_translate("MainWindow", "Arduino Code:"))
        self.pbIBrowse.setText(_translate("MainWindow", "Browse"))
        self.lblOutput.setText(_translate("MainWindow", "Output File:"))
        self.cbxFunc.setText(_translate("MainWindow", "Function"))
        self.lblDelay.setText(_translate("MainWindow", "Delay between key presses:"))
        self.lblDuckyScript.setText(_translate("MainWindow", "DuckyScript:"))
        self.pbOBrowse.setText(_translate("MainWindow", "Browse"))
        self.lblSuccess.setText(_translate("MainWindow", "Compiled and saved successfully."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCompiler), _translate("MainWindow", "DuckyScript Compiler"))
        self.pbCC.setText(_translate("MainWindow", "Compile DuckyScript"))
        self.lblCommand.setText(_translate("MainWindow", "Command:"))
        self.lblKey.setText(_translate("MainWindow", "Key/String:"))
        self.pbAdd.setText(_translate("MainWindow", "ADD"))
        self.lblDuckyScript_2.setText(_translate("MainWindow", "DuckyScript:"))
        self.cbxRealTimeCreate.setText(_translate("MainWindow", "Real-Time "))
        self.pbClear.setText(_translate("MainWindow", "Clear"))
        self.pbCSave.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCreator), _translate("MainWindow", "DuckyScript Creator"))
        try:
            MainWindow.setWindowIcon(QtGui.QIcon(os.getcwd() + "/src/icon.png"))
            self.lblPic.setPixmap(QtGui.QPixmap(os.getcwd() + "/src/main.png"))
        except:
            pass
        self.lblSuccess.setVisible(False)
        self.addCommandList()
        self.cbxKey.setVisible(False)
        self.cbxCommand.currentIndexChanged.connect(self.cbxCommand_IndexChanged)
        self.pbAdd.clicked.connect(self.pbAdd_Clicked)
        self.cbxKey.currentIndexChanged.connect(self.realTimeCreate)
        self.leKey.textChanged.connect(self.realTimeCreate)
        self.pbClear.clicked.connect(self.pbClear_Clicked)
        self.pbCC.clicked.connect(self.pbCC_Clicked)
        self.pbCSave.clicked.connect(self.pbCSave_Clicked)
        self.pbIBrowse.clicked.connect(self.pbIBrowse_Clicked)
        self.pbOBrowse.clicked.connect(self.pbOBrowse_Clicked)
        self.pbCompile.clicked.connect(self.pbCompile_Clicked)

    def addCommandList(self):
        for item in commands:
            self.cbxCommand.addItem(item)

    def cbxCommand_IndexChanged(self):
        self.cbxKey.setVisible(True)
        self.cbxKey.clear()
        if(self.cbxCommand.currentText() == "ALT"):
            for item in ducky_compiler.altCommands:
                self.cbxKey.addItem(item)
        elif (self.cbxCommand.currentText() == "CTRL"):
            for item in ducky_compiler.ctrlCommands:
                self.cbxKey.addItem(item)
        elif (self.cbxCommand.currentText() == "SHIFT"):
            for item in ducky_compiler.shiftCommands:
                self.cbxKey.addItem(item)
        else:
            self.cbxKey.setVisible(False)
            self.cbxKey.clear()

    def pbAdd_Clicked(self):
        try:
            global realtime
            if(realtime == False):
                global currentLine
                self.teCreated.setText(self.teCreated.toPlainText().replace(currentLine, str(currentLine).replace("*", "")))
            elif(self.cbxKey.isVisible()) and (self.leKey.text()  == "" ) or (self.leKey.text() == " "):
                self.teCreated.append(self.cbxCommand.currentText() + " " + self.cbxKey.currentText())
            else:
                self.teCreated.append(self.cbxCommand.currentText() + " " + self.leKey.text())
            self.leKey.setText("")
        except Exception as e:
            print(e)
        realtime = True

    def realTimeCreate(self):
        try:
            if(self.cbxRealTimeCreate.isChecked()):
                if (self.cbxKey.isVisible()) and (self.leKey.text() == "") or (self.leKey.text() == " "):
                    cl = self.cbxCommand.currentText() + " " + self.cbxKey.currentText()
                else:
                    cl = self.cbxCommand.currentText() + " " + self.leKey.text()
                global realtime
                global currentLine
                if(realtime):
                    currentLine = cl + "*"
                    realtime = False
                    self.teCreated.append(currentLine)
                else:
                    self.teCreated.setText(self.teCreated.toPlainText().replace(currentLine, cl + "*"))
                    currentLine = cl + "*"

        except Exception as e:
            print(e)

    def pbClear_Clicked(self):
        self.teCreated.clear()

    def pbCC_Clicked(self):
        self.tabWidget.setCurrentWidget(self.tabCompiler)
        self.txDucky.setText(self.teCreated.toPlainText())
        self.pbCSave_Clicked()
        self.pbCompile_Clicked()

    def pbCSave_Clicked(self):
        try:
            filename = QFileDialog.getSaveFileName(None, 'Save File', os.getenv('HOME'), "All Files (*);;Text Files (*.txt)")
            with open(filename, "w+") as f:
                f.writelines(str(self.teCreated.toPlainText()))
            self.leInput.setText(filename)
        except Exception as e:
            pass

    def pbIBrowse_Clicked(self):
        try:
            filename = QFileDialog.getOpenFileName(None, 'Open File', os.getenv('HOME'))
            self.leInput.setText(filename)	
            self.txDucky.clear()
            with open(filename, "r") as f:
                line = f.readline()
                while line != "":
                    line = f.readline()
                    self.txDucky.append(line)
        except Exception as e:
            pass

    def pbOBrowse_Clicked(self):
        try:
            filename = QFileDialog.getSaveFileName(None, 'Save File', os.getenv('HOME'))
            self.leOutput.setText(filename)
        except Exception as e:
            print(e)

    def pbCompile_Clicked(self):

        self.lblSuccess.setVisible(False)
        self.lblSuccess.setText("Compiled and saved successfully.")
        inputfile = self.leInput.text()
        delay = self.leDelay.text()
        func = self.cbxFunc.isChecked()
        output = self.leOutput.text()
        self.txArduinoCode.clear()
        if (len(inputfile) > 2) or (len(output) > 2):
            try:
                delayint = int(delay)
                try:
                    self.progressBar.setValue(10)
                    with open(inputfile, "r") as f:
                        lines = f.readlines()
                    self.progressBar.setValue(40)
                    with open(output, "w+") as f:
                        codes = ducky_compiler.Compile(lines, delay, func)
                        self.progressBar.setValue(70)
                        f.write(codes)
                        self.txArduinoCode.setText(codes)
                        self.lblSuccess.setVisible(True)
                    self.progressBar.setValue(100)
                except Exception as e:
                    self.lblSuccess.setVisible(True)
                    self.lblSuccess.setText("Error: " + e)
                    print(e)
            except:
                QMessageBox.critical(None, "Error", "Please enter valid values.")
        else:
            QMessageBox.critical(None, "Error", "Please enter valid values.")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

