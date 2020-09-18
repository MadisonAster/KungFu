#Imports##########################################
import time
from FooFinder import KungFu
from FooFinder import PythonBaseClasses
##################################################

#Test#############################################
@KungFu.depends('conda.pyside2', 'conda.qt.py', 'gui')
class test_BasicWidget(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_BasicWidget, self).__init__(*args)
        PythonBaseClasses.SingletonApp() #Global because it QApplication must be a singleton

    def test_1(self, sleep=0.5):
        testwidget = BasicWidget()
        testwidget.show()
        time.sleep(sleep)
        testwidget.hide()
##################################################

#Code#############################################
from Qt import QtCore, QtGui, QtWidgets
class BasicWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(BasicWidget, self).__init__(*args, **kwargs)
        
    def sizeHint(self):
        return QtCore.QSize(800,600)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
