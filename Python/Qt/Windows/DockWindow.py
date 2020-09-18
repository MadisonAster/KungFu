#Imports##########################################
import time
import FooFinder
from FooFinder import KungFu
from FooFinder import PythonBaseClasses
##################################################

#Test#############################################
@KungFu.depends('conda.pyside2', 'conda.qt.py', 'gui')
class test_DockWindow(KungFu.TimedTest):
    def __init__(self, *args):
        super(test_DockWindow, self).__init__(*args)
        PythonBaseClasses.SingletonApp() #Global because it QApplication must be a singleton

    def test_1(self, sleep=0.5):
        MainWindow = DockWindow()
        MainWindow.show()
        MainWindow.resize(MainWindow.QAvailableGeo.width()/2, MainWindow.QAvailableGeo.height()-MainWindow.QStartBarHeight)
        MainWindow.move(0,0)
        
        testwidget = PythonBaseClasses.BasicWidget()
        MainWindow.dockWidget(testwidget)
        
        time.sleep(sleep)
        MainWindow.hide()
        
        
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
        dWidget = QtWidgets.QDockWidget()
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
