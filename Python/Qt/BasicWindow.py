#Imports##########################################
import time
from FooFinder import KungFu
##################################################

#Test#############################################
@KungFu.depends('pip.pyside2', 'pip.qt.py', 'gui')
class test_BasicWindow(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_BasicWindow, self).__init__(*args)
        from FooFinder import SingletonApp
        SingletonApp.SingletonApp() #Global because it QApplication must be a singleton

    def test_1(self, sleep=0.5):
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
