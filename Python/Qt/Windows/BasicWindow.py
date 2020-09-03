#Standard Imports#################################
import sys, os
from importlib import machinery
import time
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Test#############################################
@KungFu.depends('qt', 'gui')
class test_BasicWindow(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_BasicWindow, self).__init__(*args)
        print('test_BasicWindow')
        PythonBaseClasses.SingletonApp() #Global because it QApplication must be a singleton

    def test_1(self, sleep=0.5):
        print('self', self)
        print('sleep', sleep)
        self.MainWindow = BasicWindow()
        self.MainWindow.show()
        time.sleep(sleep)
        self.MainWindow.hide()

    def test_2(self, sleep=0.5):
        self.MainWindow = BasicWindow()
        self.MainWindow.show()
        self.MainWindow.resize(self.MainWindow.QAvailableGeo.width()/2, self.MainWindow.QAvailableGeo.height()-self.MainWindow.QStartBarHeight)
        self.MainWindow.move(0,0)
        time.sleep(sleep)
        self.MainWindow.hide()
##################################################

#Inheritance Check################################
if not KungFu.DependencyHandler().check('qt'):
    raise Exception('return') #Module level return doesn't exist. This is a compelling use case. Maybe a PEP?
##################################################

#Relative Imports#################################
if 'PythonBaseClasses' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['PythonBaseClasses'] = machinery.SourceFileLoader('PythonBaseClasses', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',2)[0]+'/PythonBaseClasses.py').load_module()
import PythonBaseClasses
#Code#############################################

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
    KungFu.main(__file__)
##################################################
