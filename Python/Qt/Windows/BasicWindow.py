import sys, os, unittest, importlib
import time

from Qt import QtCore, QtGui, QtWidgets

if 'TestKit' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['TestKit'] = importlib.machinery.SourceFileLoader('TestKit', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',2)[0]+'/TestKit.py').load_module()
import TestKit


class BasicWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BasicWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Basic Window')
        #self.setDockOptions(False)
        #self.setDockNestingEnabled(True)
        self.setWindowTitle('Basic Window')

        self.QAvailableGeo = QtWidgets.QDesktopWidget().availableGeometry()
        self.QStartBarHeight = QtWidgets.QDesktopWidget().screenGeometry(0).height()-self.QAvailableGeo.height()
        
    def sizeHint(self):
        return QtCore.QSize(800,600)

class test_BasicWindow(TestKit.TimedTest):
    def __init__(self, *args):
        super(test_BasicWindow, self).__init__(*args)
        if TestKit.TestVars['GUI']:
            TestKit.SingletonApp() #Global because it QApplication must be a singleton

    def test_1(self, SleepTime=0.5, GUI=True):
        if not GUI:
            print('Skipping GUI Test')
            return
        self.MainWindow = BasicWindow()
        self.MainWindow.show()
        time.sleep(SleepTime)

    def test_2(self, SleepTime=0.5, GUI=True):
        if not GUI:
            print('Skipping GUI Test')
            return
        self.MainWindow = BasicWindow()
        self.MainWindow.show()
        self.MainWindow.resize(self.MainWindow.QAvailableGeo.width()/2, self.MainWindow.QAvailableGeo.height()-self.MainWindow.QStartBarHeight)
        self.MainWindow.move(0,0)
        time.sleep(SleepTime)

if __name__ == '__main__':
    TestKit.LoadTestVars()
    print(sys.argv)
    unittest.main()