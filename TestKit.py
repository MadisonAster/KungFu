'''
Recursively searches folders below the location of this file. Runs any unittest class that begins with test_
sys.argv[1] = SkipCount #Takes int as argument, skips first n tests found during search. Use this to speed test cycling during development. Set to zero or leave blank to run all.
sys.argv[2] = SleepTime #Takes float as argument, sets all sleep times to n. Use this to keep test windows on the screen for n seconds. Or leave blank to use defaults.
sys.argv[3] = Create #Takes bool as argument, creates cloud resources. This will cost money!
sys.argv[4] = Destroy #Takes bool as argument, destroys cloud resources. This can do damage!
sys.argv[5] = Destroy #Takes bool as argument, displays gui during unit tests. Turn this False to run tests without an X server.
'''
import sys, os
import unittest, inspect
import importlib
from datetime import datetime
import subprocess, shlex
from pprint import pprint

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

class TestRunner():
    SkippedCount = 0
    def RecursiveImport(self, SkipCount=0):
        wd = os.path.dirname(os.path.abspath(__file__))
        for root, dirs, files in os.walk(wd):
            for file in files:
                if file.rsplit('.',1)[-1] == 'py':
                    self.ImportTests(root.replace('\\','/')+'/'+file, SkipCount=SkipCount)
    def ImportTests(self, ModulePath, SkipCount=0):
        ModuleName = ModulePath.rsplit('/',1)[-1].rsplit('.',1)[0]
        if ModuleName in ['TestKit'] or 'BaseClasses' in ModuleName:
            return
        if ModuleName in globals().keys():
            raise Exception('Namespace conflict found. Module name already in use, pick another.', ModuleName)
        ModuleSpec = importlib.util.spec_from_file_location("module.name", ModulePath)
        Module = importlib.util.module_from_spec(ModuleSpec)
        ModuleSpec.loader.exec_module(Module)
        inspect.getmembers(Module)
        for ClassName, Class in inspect.getmembers(Module):
            if 'test_' in ClassName:
                if ClassName in globals().keys():
                    raise Exception('Namespace conflict found. Class Name already in use, pick another.', ClassName, Module.__file__)
                if self.SkippedCount >= SkipCount:
                    globals()[ClassName] = Class
                else:
                    self.SkippedCount += 1

def LoadTestVars():
    T = {}
    T['SkipCount'], T['SleepTime'], T['Create'], T['Destroy'], T['GUI'] = 0, 0.5, False, False, True
    if len(sys.argv) >= 2:
        T['SkipCount'], T['SleepTime'], T['Create'], T['Destroy'], T['GUI'] = int(sys.argv[1]), float(sys.argv[2]), (sys.argv[3]=='True'), (sys.argv[4]=='True'), (sys.argv[5]=='True')
    
    global TestVars
    TestVars = T
    print('TestVars', TestVars)

    sys.TestVars = TestVars
    del sys.argv[1:]
    return TestVars

if __name__ == '__main__':
    TestVars = LoadTestVars()
    TestInstance = TestRunner()
    TestInstance.RecursiveImport(SkipCount=TestVars['SkipCount'])
    unittest.main()
