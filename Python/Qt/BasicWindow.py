from Qt import QtCore, QtGui, QtWidgets

from TestKit import *

SingeltonApp() #Global because it QApplication must be a singleton

class test_BasicWindow(TimedTest):
	def test_1(self):
		self.MainWindow = 