import os, sys, importlib

from Qt import QtCore, QtGui, QtWidgets
if 'BasicWindow' not in sys.modules.keys(): #Relative import handling for base classes
    importlib.machinery.SourceFileLoader('BasicWindow', os.path.dirname(os.path.abspath(__file__))+'/Qt/Windows/BasicWindow.py').load_module()
from BasicWindow import BasicWindow

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
