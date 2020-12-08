#Imports##########################################
import time
from FooFinder import KungFu
##################################################

#Test#############################################
@KungFu.depends('pip.pyside2', 'pip.qt.py', 'gui')
class test_UiWindow(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_UiWindow, self).__init__(*args)
        from FooFinder import SingletonApp
        self.QApp = SingletonApp.SingletonApp() #Global because it QApplication must be a singleton
    
    def test_1(self, sleep=0.5):
        self.MainWindow = UiWindow()
        self.MainWindow.show()
        self.QApp.processEvents()
        time.sleep(sleep)
        self.MainWindow.hide()
##################################################

#Code#############################################
from Qt import QtCore, QtGui, QtWidgets, QtCompat
from FooFinder import BasicWindow
class UiWindow(BasicWindow.BasicWindow):
    def __init__(self, *args, **kwargs):
        super(UiWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('UiWindow')
        print('Ui MainWindow __init__!!!!')
        ui = __file__.rsplit('.',1)[0]+'.ui'
        QtCompat.loadUi(ui, baseinstance=self)

    def sizeHint(self):
        return QtCore.QSize(800,600)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
