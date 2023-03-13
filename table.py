import sys
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget, QTableWidgetItem, QAbstractItemView
import subprocess

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('layout.ui', self)
        
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 200)
        self.loaddata()

    def loaddata(self):
        people=[{"Name":"Abdullah","Section":"A","Address":"Islamabad"}, {"Name":"Hamza","Section":"B","Address":"Lahore"}, {"Name":"Ali","Section":"C","Address":"Karachi"}]
        row =0
        self.tableWidget.setRowCount(len(people))

        for person in people:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(person["Name"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(person["Section"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(person["Address"]))
            row=row+1



app = QApplication(sys.argv)
window = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(600)
widget.setFixedHeight(300)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print('Exiting')
