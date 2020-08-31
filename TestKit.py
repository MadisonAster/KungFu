'''
Recursively searches folders below the location of this file. 
Runs any unittest class that begins with test_

examples:
python3 TestKit.py                          #run all tests, automatically decide if gui is available

python3 TestKit.py -sleep 1.0               #run tests with a sleeptime of 1.0 seconds
python3 TestKit.py -folder Python/Qt        #run all tests in the Python/Qt folder
python3 TestKit.py -folders Python,AWS      #run all tests in the Python and AWS folders
python3 TestKit.py -gui True                #Force gui tests to run.
python3 TestKit.py -gui False               #Force gui tests not to run.
python3 TestKit.py --create                 #Run tests that provision real cloud resources. THIS WILL COST MONEY!
python3 TestKit.py --destroy                #Run tests that destroy real cloud resources. THIS IS POTENTIALLY DESTRUCTIVE!
'''
import sys, os
import unittest, inspect, argparse
from importlib import util
from datetime import datetime

import io
import contextlib

@contextlib.contextmanager
def stderrIO(stderr=None):
    old = sys.stderr
    if stderr is None:
        stderr = io.StringIO()
    sys.stderr = stderr
    yield stderr
    sys.stderr = old

def gui(func):
    if not sys.TestArgs.gui:
        print('Skipping gui Test')
        return None
    else:
        return func
def create(func):
    if not sys.TestArgs.create:
        print('Skipping create Test')
        return None
    else:
        return func
def destroy(func):
    if not sys.TestArgs.destroy:
        print('Skipping destroy Test')
        return None
    else:
        return func


class TimedTest(unittest.TestCase):
    def __init__(self, *args):
        super(TimedTest, self).__init__(*args)
        for FunctionName, Function in inspect.getmembers(self.__class__):
            if Function:
                if 'test_' in FunctionName and Function.__defaults__ != None:
                    arglist = list(Function.__defaults__)
                    for (key, value) in sys.TestArgs._get_kwargs():
                        if key in Function.__code__.co_varnames:
                            i = Function.__code__.co_varnames.index(key)
                            arglist[i-1] = value
                    Function.__defaults__ = tuple(arglist)

    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

class TestRunner():
    SkippedCount = 0
    def __init__(self):
        super(TestRunner, self).__init__()
        self.TestSuite = unittest.TestSuite()
        self.TestArgs = self.LoadTestVars()
        self.RecursiveImport(folders=self.TestArgs.folders)

    def main(self):
        self.Runner = unittest.TextTestRunner()
        self.Runner.run(self.TestSuite)

    def RecursiveImport(self, folders=None):
        wd = os.path.dirname(os.path.abspath(__file__))
        if folders == None:
            folders = [wd]
        else:
            for i, folder in enumerate(folders):
                folders[i] = wd+'/'+folder
        for folder in folders:
            for root, dirs, files in os.walk(folder):
                dirs.sort()
                files.sort()
                for file in files:
                    if file.rsplit('.',1)[-1] == 'py':
                        self.ImportTests(root.replace('\\','/')+'/'+file)

    def ImportTests(self, ModulePath):
        ModuleName = ModulePath.rsplit('/',1)[-1].rsplit('.',1)[0]
        if ModuleName in ['TestKit'] or 'BaseClasses' in ModuleName:
            return
        if ModuleName in globals().keys():
            raise Exception('Namespace conflict found. Module name already in use, pick another.', ModuleName)
        ModuleSpec = util.spec_from_file_location("module.name", ModulePath)
        Module = util.module_from_spec(ModuleSpec)
        ModuleSpec.loader.exec_module(Module)
        inspect.getmembers(Module)
        for ClassName, Class in inspect.getmembers(Module):
            if 'test_' in ClassName:
                if ClassName in globals().keys():
                    raise Exception('Namespace conflict found. Class Name already in use, pick another.', ClassName, Module.__file__)
                self.TestSuite.addTest(unittest.makeSuite(Class))

    def LoadTestVars(self):
        parser = argparse.ArgumentParser()
        def csv(val): return val.split(',')
        parser.add_argument("-folders", help="Specify a list of test folders to run.", type=csv)
        parser.add_argument("-folder", help="Specify a folder of tests to run.", type=str)
        parser.add_argument("-sleep", help="Specify a sleep time in second for gui tests to remain on the screen.", type=float)
        parser.add_argument("-gui", help="Specify whether or not to run GUI tests.", type=bool)
        parser.add_argument("--create", help="provision cloud resources, (this will cost money!)", action="store_true")
        parser.add_argument("--destroy", help="destroy cloud resources, (this will destory resouces!)", action="store_true")
        self.TestArgs = parser.parse_args()
        if self.TestArgs.sleep == None:
            self.TestArgs.sleep = 0.5
        if self.TestArgs.folder != None:
            self.TestArgs.folders = [self.TestArgs.folder]
        if self.TestArgs.gui == None:
            try:
                with stderrIO() as stderr:
                    exec("from Qt import QtCore")
                if stderr.getvalue() == '':
                    self.TestArgs.gui = True
                else:
                    print('X server not available! Disabling gui tests!')
                    self.TestArgs.gui = False
            except ImportError as exception:
                raise exception
        print(self.TestArgs)
        sys.TestArgs = self.TestArgs
        return self.TestArgs

if __name__ == '__main__':
    TestInstance = TestRunner()
    TestInstance.main()
    #unittest.main()
