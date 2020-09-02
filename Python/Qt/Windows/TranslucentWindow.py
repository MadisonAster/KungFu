#Standard Imports#################################
import sys, os, unittest, importlib
import time
##################################################

#Relative Imports#################################
if 'TestKit' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['TestKit'] = importlib.machinery.SourceFileLoader('TestKit', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/TestKit.py').load_module()
import TestKit

if 'PythonBaseClasses' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['PythonBaseClasses'] = importlib.machinery.SourceFileLoader('PythonBaseClasses', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',2)[0]+'/PythonBaseClasses.py').load_module()
import PythonBaseClasses
##################################################

#Test#############################################
class test_TranslucentWindow(TestKit.TimedTest):
    def __init__(self, *args):
        super(test_TranslucentWindow, self).__init__(*args)
        PythonBaseClasses.SingletonApp() #Global because it QApplication must be a singleton
    
    @TestKit.gui
    @TestKit.qt
    def test_1(self, SleepTime=0.5):
        self.MainWindow = TranslucentWindow()
        self.MainWindow.show()
        time.sleep(SleepTime)
##################################################

#Inheritance Check################################
if not TestKit.DependencyHandler().check('qt'):
    raise Exception('return') #Module level return doesn't exist. This is a compelling use case. Maybe a PEP?
##################################################

#Code#############################################
from Qt import QtCore, QtGui, QtWidgets
class TranslucentWindow(PythonBaseClasses.BasicWindow):
    def __init__(self, *args, **kwargs):
        super(TranslucentWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Translucent Window')
        
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def sizeHint(self):
        return QtCore.QSize(800,600)
##################################################

#Main#############################################
if __name__ == '__main__':
    TestKit.LoadTestVars()
    unittest.main()
##################################################
