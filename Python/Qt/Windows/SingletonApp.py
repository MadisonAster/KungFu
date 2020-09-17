#Standard Imports#################################
import sys, os
from importlib import machinery
import time
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/KungFu.py').load_module()
import KungFu
if 'PythonBaseClasses' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['PythonBaseClasses'] = machinery.SourceFileLoader('PythonBaseClasses', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',2)[0]+'/PythonBaseClasses.py').load_module()
import PythonBaseClasses
##################################################

#Test#############################################
@KungFu.depends('pyside2', 'qt.py', 'gui')
class test_SingletonApp(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_SingletonApp, self).__init__(*args)
        print('test_SingletonApp')
        SingletonApp() #Global because it QApplication must be a singleton
##################################################

#Code#############################################
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
