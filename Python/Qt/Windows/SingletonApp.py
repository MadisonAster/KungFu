#Imports##########################################
import FooFinder
from FooFinder import KungFu
from FooFinder import PythonBaseClasses
##################################################

#Test#############################################
@KungFu.depends('conda.pyside2', 'conda.qt.py', 'gui')
class test_SingletonApp(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_SingletonApp, self).__init__(*args)
        print('test_SingletonApp')
        SingletonApp() #Global because it QApplication must be a singleton
##################################################

#Code#############################################
import sys
from Qt import QtCore, QtGui, QtWidgets
class SingletonApp(QtWidgets.QApplication):
    def __new__(cls):
        if QtWidgets.QApplication.instance() == None:
            print('Starting QtWidgets.QApplication singleton.')
            sys.QApplication = None
            class_instance = super(SingletonApp, cls).__new__(cls)
        else:
            class_instance = QtWidgets.QApplication.instance()
            class_instance.__init__()
        return class_instance

    def __init__(self):
        print('Initializing Integrated QApplication')
        if sys.QApplication == None:
            print('Referencing Integrated QApplication')
            sys.QApplication = self
            super(SingletonApp, self).__init__()
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
