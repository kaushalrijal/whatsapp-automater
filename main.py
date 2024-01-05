"""
Project Name: Whatsapp Automater
Project Author: Kaushal Rijal
Project Start Date: 2023/06/30, 3:20 PM
Project End Date: 2023/07/06, 1:35 PM
"""

import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QDialog
import pandas as pd
import pywhatkit
import win32clipboard
import webbrowser

from main_ui import Ui_MainWindow

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.numbers = []
        self.imgpath = ""
        self.n = 59
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.button_import.clicked.connect(self.import_csv)
        self.button_pick.clicked.connect(self.pick)
        self.button_send.clicked.connect(self.send)
        self.actionCreator.triggered.connect(self.about)
        self.actionHow_To_Use.triggered.connect(self.howto)
        self.actionExit.triggered.connect(self.close)

    @pyqtSlot()
    def pick(self):
        ipath = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Pick attachment image",
            "${HOME}",
            "All Files (*);; JPEG Files (*.jpg);; PNG Files (*.png)",
        )
        self.imgpath = ipath[0]


    @pyqtSlot()
    def import_csv(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Pick CSV file containing numbers",
            "${HOME}",
            "CSV Files (*.csv)",
        )
        k = pd.read_csv(fname[0])
        data = k['numbers'].tolist()
        for i in data:
            k = "+977" + str(i)
            self.numbers.append(k)

    def about(self):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("About")
        dlg.setText("All the contents in this app is created by Kaushal Rijal")
        button = dlg.exec()

        if button == QtWidgets.QMessageBox.StandardButton.Ok:
            webbrowser.open("https://kaushalrijal.com.np")

    def howto(self):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("How to Use?")
        dlg.setText("""
            <h1>HOW TO USE WHATSAPP AUTOMATER?</h1>
            <h3>Using this app is pretty simple. Just follow the steps below:<br />
            (Before starting make sure that you have logged into Whatsapp web 
            in your default browser)<br /></h3>
            <h4>
            1) Create a CSV file.<br />
            2) Name the first element of first column "numbers"<br />
            3) Insert all your contacts below first row in the first column<br />
            4) Import it from this app<br />
            5) If you want to send any image import.<br />
            6) Subject field is just for developer purposes(keeping logs), so
               if you don't want to fill it you can just leave it.<br />
            7) Type any message in the messages field if you want<br />
            8) You can fill only one of the two fields: Image and Message, but 
               both the fields cannot be empty<br />
            9) Click on send and watch on as your computer sends all the 
               messages by itself.<br />
            10) If you get any errors contact me via my website: https://kaushalrijal.com.np
            </h4>
        """)
        dlg.exec()

    def send(self):
        
        subject = self.input_message.toPlainText()

        if self.numbers != [] and (self.imgpath != "" or subject != ""):            
            for i in self.numbers:
                try:
                    pywhatkit.sendwhats_image(i, self.imgpath, subject, 22, self.n)
                except:
                    pass
                self.n += 1
        elif self.numbers == []:
            button = QtWidgets.QMessageBox.critical(
            self,
            "Error",
            "You must import numbers",
            buttons=QtWidgets.QMessageBox.StandardButton.Ok,
            defaultButton=QtWidgets.QMessageBox.StandardButton.Ok,
        )

            if button == QtWidgets.QMessageBox.StandardButton.Ok:
                pass
            else:
                pass
        elif self.imgpath == "" or subject == "":
            button = QtWidgets.QMessageBox.critical(
            self,
            "Error",
            "Both image field and message field cannot be empty. You must fill at least on of them!",
            buttons=QtWidgets.QMessageBox.StandardButton.Ok,
            defaultButton=QtWidgets.QMessageBox.StandardButton.Ok,
        )

            if button == QtWidgets.QMessageBox.StandardButton.Ok:
                pass
            else:
                pass
        else:
            button = QtWidgets.QMessageBox.critical(
            self,
            "Error",
            "Make sure all fields are filled in properly!",
            buttons=QtWidgets.QMessageBox.StandardButton.Ok,
            defaultButton=QtWidgets.QMessageBox.StandardButton.Ok,
        )

            if button == QtWidgets.QMessageBox.StandardButton.Ok:
                pass
            else:
                pass

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About")

        QBtn = QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Website

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("All the contents in this app is Created By Kaushal Rijal")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
