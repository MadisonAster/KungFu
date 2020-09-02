#Standard Imports#################################
import os, sys, importlib
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = importlib.machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',2)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Test#############################################
#TODO
##################################################

#3rd Party Inheritance Check######################
if not KungFu.DependencyHandler().check('qt'):
    raise Exception('return')
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

#Relative Child Imports###########################
if 'BasicWindow' not in sys.modules.keys(): #Relative import handling for base classes
    importlib.machinery.SourceFileLoader('BasicWindow', os.path.dirname(os.path.abspath(__file__))+'/Qt/Windows/BasicWindow.py').load_module()
from BasicWindow import BasicWindow
##################################################
