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
class test_BasicWindow(TestKit.TimedTest):
    def __init__(self, *args):
        super(test_BasicWindow, self).__init__(*args)
        print('test_BasicWindow')
        PythonBaseClasses.SingletonApp() #Global because it QApplication must be a singleton

    @TestKit.depends('qt', 'gui')
    def test_1(self, SleepTime=0.5):
        self.MainWindow = BasicWindow()
        self.MainWindow.show()
        time.sleep(SleepTime)

    @TestKit.depends('qt', 'gui')
    def test_2(self, SleepTime=0.5):
        self.MainWindow = BasicWindow()
        self.MainWindow.show()
        self.MainWindow.resize(self.MainWindow.QAvailableGeo.width()/2, self.MainWindow.QAvailableGeo.height()-self.MainWindow.QStartBarHeight)
        self.MainWindow.move(0,0)
        time.sleep(SleepTime)
##################################################

#Inheritance Check################################
if not TestKit.DependencyHandler().check('qt'):
    raise Exception('return') #Module level return doesn't exist. This is a compelling use case. Maybe a PEP?
##################################################

#Code#############################################
from Qt import QtCore, QtGui, QtWidgets
class BasicWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BasicWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Basic Window')
        self.QAvailableGeo = QtWidgets.QDesktopWidget().availableGeometry()
        self.QStartBarHeight = QtWidgets.QDesktopWidget().screenGeometry(0).height()-self.QAvailableGeo.height()
        
        
        #self.setDockOptions(False)
        #self.setDockNestingEnabled(True)

        
    def sizeHint(self):
        return QtCore.QSize(800,600)
##################################################

#Main#############################################
if __name__ == '__main__':
    TestKit.LoadTestVars()
    unittest.main()
##################################################
