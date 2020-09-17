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
@KungFu.depends('conda.pyside2', 'conda.qt.py', 'gui')
class test_FramelessWindow(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_FramelessWindow, self).__init__(*args)
        PythonBaseClasses.SingletonApp() #Global because it QApplication must be a singleton

    def test_1(self, sleep=0.5):
        self.MainWindow = FramelessWindow()
        self.MainWindow.show()
        time.sleep(sleep)
        self.MainWindow.hide()
##################################################

#Code#############################################
from Qt import QtCore, QtGui, QtWidgets
class FramelessWindow(PythonBaseClasses.BasicWindow):
    def __init__(self, *args, **kwargs):
        super(FramelessWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Frameless Window')
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def sizeHint(self):
        return QtCore.QSize(800,600)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
