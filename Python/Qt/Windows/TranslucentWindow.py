#Imports##########################################
import time
from FooFinder import KungFu
from FooFinder import PythonBaseClasses
##################################################

#Test#############################################
@KungFu.depends('conda.pyside2', 'conda.qt.py', 'gui')
class test_TranslucentWindow(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_TranslucentWindow, self).__init__(*args)
        PythonBaseClasses.SingletonApp() #Global because it QApplication must be a singleton
    
    def test_1(self, sleep=0.5):
        self.MainWindow = TranslucentWindow()
        self.MainWindow.show()
        time.sleep(sleep)
        self.MainWindow.hide()
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
