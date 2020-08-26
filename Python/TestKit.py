import sys, inspect
import unittest
from datetime import datetime
import subprocess, shlex
from pprint import pprint

from Qt import QtCore, QtGui, QtWidgets

class SingletonApp(QtWidgets.QApplication):
    def __new__(cls):
        if QtWidgets.QApplication.instance() == None:
            print('Starting QtWidgets.QApplication singleton.')
            sys.QApplication = None
            class_instance = super(SingletonApp, cls).__new__(cls)
        else:
            class_instance = QtWidgets.QApplication.instance()
            class_instance.__init__()
        return class_instance

    def __init__(self):
        print('Initializing Integrated QApplication')
        if sys.QApplication == None:
            print('Referencing Integrated QApplication')
            sys.QApplication = self
            super(SingletonApp, self).__init__()

class TimedTest(unittest.TestCase):
    def __init__(self, *args):
        super(TimedTest, self).__init__(*args)
        for FunctionName, Function in inspect.getmembers(self.__class__):
            if 'test_' in FunctionName and Function.__defaults__ != None:
                arglist = list(Function.__defaults__)
                for varname in sys.TestVars.keys():
                    if varname in Function.__code__.co_varnames:
                        i = Function.__code__.co_varnames.index(varname)
                        arglist[i-1] = sys.TestVars[varname]
                Function.__defaults__ = tuple(arglist)

    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

def LoadTestVars():
    T = {}
    T['SkipCount'], T['SleepTime'], T['Create'], T['Destroy'] = 0, 0, False, False
    if len(sys.argv) >= 2:
        T['SkipCount'], T['SleepTime'], T['Create'], T['Destroy'] = int(sys.argv[1]), float(sys.argv[2]), (sys.argv[3]=='True'), (sys.argv[4]=='True')
    print('TestVars', T)
    sys.TestVars = T
    del sys.argv[1:]

if __name__ == '__main__':
    LoadTestVars()
    unittest.main()
