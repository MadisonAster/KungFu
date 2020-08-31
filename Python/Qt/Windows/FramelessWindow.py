import sys, os, unittest, importlib
import time

from Qt import QtCore, QtGui, QtWidgets

if 'PythonBaseClasses' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['PythonBaseClasses'] = importlib.machinery.SourceFileLoader('PythonBaseClasses', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',2)[0]+'/PythonBaseClasses.py').load_module()
if 'TestKit' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['TestKit'] = importlib.machinery.SourceFileLoader('TestKit', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/TestKit.py').load_module()
import PythonBaseClasses
import TestKit


class FramelessWindow(PythonBaseClasses.BasicWindow):
    def __init__(self, *args, **kwargs):
        super(FramelessWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Frameless Window')
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def sizeHint(self):
        return QtCore.QSize(800,600)

class test_FramelessWindow(TestKit.TimedTest):
    def __init__(self, *args):
        super(test_FramelessWindow, self).__init__(*args)
        PythonBaseClasses.SingletonApp() #Global because it QApplication must be a singleton

    @TestKit.gui
    @TestKit.qt
    def test_1(self, SleepTime=0.5):
        self.MainWindow = FramelessWindow()
        self.MainWindow.show()
        time.sleep(SleepTime)

if __name__ == '__main__':
    TestKit.LoadTestVars()
    unittest.main()
