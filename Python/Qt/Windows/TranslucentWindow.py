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
@KungFu.depends('qt', 'gui')
class test_TranslucentWindow(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_TranslucentWindow, self).__init__(*args)
        PythonBaseClasses.SingletonApp() #Global because it QApplication must be a singleton
    
    def test_1(self, SleepTime=0.5):
        self.MainWindow = TranslucentWindow()
        self.MainWindow.show()
        time.sleep(SleepTime)
##################################################

#Inheritance Check################################
if not KungFu.DependencyHandler().check('qt'):
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
    KungFu.main(__file__)
##################################################
