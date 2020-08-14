import unittest
import time

from Qt import QtCore, QtGui, QtWidgets

#from TestKit import *
import TestKit

TestKit.SingletonApp() #Global because it QApplication must be a singleton

class BasicWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BasicWindow, self).__init__(*args, **kwargs)

class test_BasicWindow(TestKit.TimedTest):
    def test_1(self):
        self.MainWindow = BasicWindow()
        self.MainWindow.show()
        time.sleep(0.5)

if __name__ == '__main__':
    unittest.main()