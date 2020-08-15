import unittest
import time

from Qt import QtCore, QtGui, QtWidgets

#from TestKit import *
import TestKit

TestKit.SingletonApp() #Global because it QApplication must be a singleton

class BasicWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BasicWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Basic Window')
        #self.setDockOptions(False)
        #self.setDockNestingEnabled(True)
        self.setWindowTitle('Basic Window')

        self.QAvailableGeo = QtWidgets.QDesktopWidget().availableGeometry()
        self.QStartBarHeight = QtWidgets.QDesktopWidget().screenGeometry(0).height()-self.QAvailableGeo.height()
        
    def sizeHint(self):
        return QtCore.QSize(800,600)

class test_BasicWindow(TestKit.TimedTest):
    def test_1(self, SleepTime = 0.5):
        self.MainWindow = BasicWindow()
        self.MainWindow.show()
        time.sleep(SleepTime)

    def test_2(self, SleepTime = 0.5):
        self.MainWindow = BasicWindow()
        self.MainWindow.show()
        self.MainWindow.resize(self.MainWindow.QAvailableGeo.width()/2, self.MainWindow.QAvailableGeo.height()-self.MainWindow.QStartBarHeight)
        self.MainWindow.move(0,0)
        time.sleep(SleepTime)

if __name__ == '__main__':
    unittest.main()