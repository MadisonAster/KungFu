#Imports##########################################
import time
from FooFinder import KungFu
##################################################

#Test#############################################
@KungFu.depends('pip.pyside2', 'pip.qt.py', 'gui')
class test_TranslucentWindow(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_TranslucentWindow, self).__init__(*args)
        from FooFinder import SingletonApp
        SingletonApp.SingletonApp() #Global because it QApplication must be a singleton
    
    def test_1(self, sleep=0.5):
        self.MainWindow = TranslucentWindow()
        self.MainWindow.show()
        time.sleep(sleep)
        self.MainWindow.hide()
##################################################

#Code#############################################
from Qt import QtCore, QtGui, QtWidgets
from FooFinder import BasicWindow
class TranslucentWindow(BasicWindow.BasicWindow):
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
