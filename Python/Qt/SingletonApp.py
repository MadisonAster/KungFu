#Imports##########################################
from FooFinder import KungFu
##################################################

#Test#############################################
@KungFu.depends('pip.pyside2', 'pip.qt.py', 'gui')
class test_SingletonApp(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_SingletonApp, self).__init__(*args)
        SingletonApp() #Global because it QApplication must be a singleton
##################################################

#Code#############################################
import sys
from Qt import QtCore, QtGui, QtWidgets
class SingletonApp(QtWidgets.QApplication):
    def __new__(cls):
        if QtWidgets.QApplication.instance() == None:
            print('Initializing Integrated QApplication.')
            sys.QApplication = None
            class_instance = super(SingletonApp, cls).__new__(cls)
        else:
            class_instance = QtWidgets.QApplication.instance()
            class_instance.__init__()
        return class_instance

    def __init__(self):
        if sys.QApplication == None:
            sys.QApplication = self
            super(SingletonApp, self).__init__()
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
