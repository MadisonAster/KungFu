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
