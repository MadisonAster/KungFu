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
class test_DockWindow(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_DockWindow, self).__init__(*args)
        PythonBaseClasses.SingletonApp() #Global because it QApplication must be a singleton

    def test_1(self, sleep=0.5):
        self.MainWindow = DockWindow()
        self.MainWindow.show()
        self.MainWindow.resize(self.MainWindow.QAvailableGeo.width()/2, self.MainWindow.QAvailableGeo.height()-self.MainWindow.QStartBarHeight)
        self.MainWindow.move(0,0)
        
        testwidget = PythonBaseClasses.BasicWidget()
        MainWindow.dockThisWidget(testwidget)
        
        time.sleep(sleep)
        self.MainWindow.hide()
        
        
##################################################

#Code#############################################
from Qt import QtCore, QtGui, QtWidgets
class DockWindow(PythonBaseClasses.BasicWindow):
    def __init__(self, *args, **kwargs):
        super(DockWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Dock Window')
        
        #self.setDockOptions(False)
        #self.setDockNestingEnabled(True)
        
        self.AllowNestedDocks
        self.ForceTabbedDocks
        self.setTabPosition(QtCore.Qt.AllDockWidgetAreas, QtWidgets.QTabWidget.North)
        self.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.setDockNestingEnabled(True)

    def dockWidget(self, widget, dockArea = QtCore.Qt.RightDockWidgetArea):
        widgetName = widget.accessibleName()
        if widgetName == '':
            widgetName = type(widget).__name__
        dWidget = QtGui.QDockWidget()
        dWidget.setWidget(widget)
        dWidget.setObjectName(widgetName)
        dWidget.setWindowTitle(widgetName)
        self.addDockWidget(dockArea, dWidget)

    def sizeHint(self):
        return QtCore.QSize(800,600)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
