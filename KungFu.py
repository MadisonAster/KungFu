'''
Recursively searches folders below the location of this file. 
Runs any unittest class that begins with test_

examples:
python3 KungFu.py                          #run all tests, automatically decide if gui is available

python3 KungFu.py -sleep 1.0               #run tests with a sleeptime of 1.0 seconds
python3 KungFu.py -folder Python/Qt        #run all tests in the Python/Qt folder
python3 KungFu.py -folders Python,AWS      #run all tests in the Python and AWS folders
python3 KungFu.py --create                 #Run tests that provision real cloud resources. THIS WILL COST MONEY!
python3 KungFu.py --destroy                #Run tests that destroy real cloud resources. THIS IS POTENTIALLY DESTRUCTIVE!
'''
#Standard Imports#################################
import sys, os
import unittest, inspect, argparse
from importlib import util
from datetime import datetime
import subprocess, shlex
import traceback
import functools
import io
import contextlib
import types
##################################################

#Decorators#######################################
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

def depends(*args):
    dependencylist = args
    def actual_decorator(cls):
        if 'base' in dependencylist:
            return cls
        rNone = False
        for dependency in dependencylist:
            if not DependencyHandler().check(dependency):
                count = 0
                for FunctionName, Function in inspect.getmembers(cls):
                    if 'test_' in FunctionName:
                        count += 1
                print('Skipping '+str(count)+' '+dependency+' test(s).')
                DependencyHandler().SkipCount += count
                rNone = True
        else:
            if rNone:
                return None
            if cls:
                return cls
    return actual_decorator
##################################################

#Base Classes#####################################
class TimedTest(unittest.TestCase):
    def __init__(self, *args):
        super(TimedTest, self).__init__(*args)
        for FunctionName, Function in inspect.getmembers(self.__class__):
            if Function and 'test_' in FunctionName:
                partial = functools.partial(self.GetPartial, Function)
                setattr(self.__class__, FunctionName, partial)

    def GetPartial(self, func):
        if type(func) == functools.partial: return func()
        if func.__defaults__:
            arglist = list(func.__defaults__)
            for key in sys.TestArgs.kwargs:
                if key in func.__code__.co_varnames:
                    i = func.__code__.co_varnames.index(key)
                    arglist[i-1] = sys.TestArgs.kwargs[key]
            func.__defaults__ = tuple(arglist)
        return func(self)

    def setUp(self):
        self.starttime = datetime.now()

    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

class PrototypeTestParser(unittest.TestCase):
    def prototest(self, *args, testname=''):
        (result, testtime) = self.parser.results[testname]
        success = 'executed' if result else 'failed'
        self.assertEqual(result, True)

    def add_tests(cls, parsercls):
        cls.parser = parsercls()
        cls.parser.run()
        for testname in cls.parser.results:
            newtest = cls.copy_func(cls, cls.prototest, testname)
            newtest.__name__ = testname
            setattr(cls, testname, newtest)

    def copy_func(cls, func, testname):
        newfunc = types.FunctionType(func.__code__, func.__globals__)
        newfunc = functools.update_wrapper(newfunc, func)
        newfunc.__kwdefaults__ = {'testname': testname}
        return newfunc
##################################################

#Main#############################################
class DependencyHandler():
    cwd = os.path.dirname(os.path.abspath(__file__))
    Installed = []
    NotInstalled = []
    SkipCount = 0

    def __new__(cls, *args, **kwargs):
        if not hasattr(sys, 'DependencyHandler'): #Global Singleton
            sys.DependencyHandler = super(DependencyHandler, cls).__new__(cls, *args, **kwargs)
        return sys.DependencyHandler

    def check(self, name):
        if name in self.Installed:
            return True
        elif name in self.NotInstalled:
            return False
        else:
            return self.run_check(name)

    def run_check(self, name):
        if name == 'gui':
            return self.check_gui()
        checkpath = self.cwd+'/_installers/'+name+'_check.sh'
        if os.path.exists(checkpath):
            returncodes = 0
            with open(checkpath, 'r') as file:
                for line in file.readlines():
                    result, returncode = RunCmd(line, cwd=self.cwd)
                    returncodes += returncode
            returncodes = not bool(returncodes)
            if returncodes:
                self.Installed.append(name)
            else:
                self.NotInstalled.append(name)
            return returncodes

    def run_installer(self, name):
        checkpath = self.cwd+'/_installers/'+name+'_check.sh'
        if os.path.exists(checkpath):
            returncodes = 0
            with open(checkpath, 'r') as file:
                for line in file.readlines():
                    print('line', line)
                    result, returncode = RunCmd(line, cwd=self.cwd)
                    returncodes += returncode
            returncodes = not bool(returncodes)
            return returncodes

    def offer_installers(self):
        if len(self.NotInstalled) != 0:
            print(str(self.SkipCount)+" tests couldn't run because the following items are missing:")
            for name in self.NotInstalled:
                print('    '+name)
            if 'gui' in self.NotInstalled:
                self.NotInstalled.remove('gui')
            if len(self.NotInstalled) != 0:
                print('----------------------------------------------------------------------')
                print('INSTALLERS ARE STILL UNTESTED! RUN AT YOUR OWN RISK!')
                print('Automated Dependency Installers:')
                for name in self.NotInstalled:
                    answer = input('    Would you like to try installing '+name+'? ')
                    answer = answer.lower() in ['y', 'yes', 'true']
                    if answer == True:
                        run_installer(name)
        else:
            print('Everything OK!')
        print('----------------------------------------------------------------------')
        print('Goodbye!')
    
    ###Still hacking this for now until I find a more general way###
    @contextlib.contextmanager
    def GetStderrIO(self, stderr=None):
        old = sys.stderr
        if stderr is None:
            stderr = io.StringIO()
        sys.stderr = stderr
        yield stderr
        sys.stderr = old

    def check_gui(self):
        try:
            with self.GetStderrIO() as stderr:
                from Qt import QtCore
            if stderr.getvalue() == '':
                self.Installed.append('gui')
                installed = True
            else:
                print('X server not available! Disabling gui tests!')
                self.NotInstalled.append('gui')
                installed = False
        except ImportError as exception:
            print('Qt not available! Disabling gui tests!')
            self.NotInstalled.append('gui')
            installed = False
        print('gui installed', installed)
        return installed
    ################################################################
    pass

class TestRunner():
    SkippedCount = 0
    def __init__(self, *args):
        super(TestRunner, self).__init__()
        self.TestSuite = unittest.TestSuite()
        self.TestArgs = self.LoadTestVars()
        if len(args) > 0:
            for filepath in args:
                print('ImportTests!', filepath)
                self.ImportTests(os.path.abspath(filepath))
        else:
            self.RecursiveImport(folders=self.TestArgs.folders)

    def main(self):
        start = datetime.now()
        #self.Runner = unittest.TextTestRunner(stream=open(os.devnull, 'w'))
        self.Runner = unittest.TextTestRunner()
        result = self.Runner.run(self.TestSuite)
        print('----------------------------------------------------------------------')
        t = datetime.now()-start
        print('KungFu ran '+str(result.testsRun)+' tests in '+str(t.total_seconds())+'s')

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
        if ModuleName in ['KungFu'] or 'BaseClasses' in ModuleName:
            return
        if ModuleName in globals().keys():
            raise Exception('Namespace conflict found. Module name already in use, pick another.', ModuleName)
        ModuleSpec = util.spec_from_file_location("module.name", ModulePath)
        Module = util.module_from_spec(ModuleSpec)
        try:
            ModuleSpec.loader.exec_module(Module)
        except ImportError as exception:
            pass
        for ClassName, Class in inspect.getmembers(Module):
            if 'test_' in ClassName and Class != None:
                if ClassName in globals().keys():
                    raise Exception('Namespace conflict found. Class Name already in use, pick another.', ClassName, Module.__file__)
                globals()[ClassName] = Class
                self.TestSuite.addTest(unittest.makeSuite(Class))
    
    def LoadTestVars(self):
        parser = argparse.ArgumentParser()
        def csv(val): return val.split(',')
        parser.add_argument("-folders", help="Specify a list of test folders to run.", type=csv)
        parser.add_argument("-folder", help="Specify a folder of tests to run.", type=str)
        parser.add_argument("-sleep", help="Specify a sleep time in second for gui tests to remain on the screen.", type=float)
        parser.add_argument("--create", help="provision cloud resources, (this will cost money!)", action="store_true")
        parser.add_argument("--destroy", help="destroy cloud resources, (this will destory resouces!)", action="store_true")

        self.TestArgs, unknown = parser.parse_known_args()
        if self.TestArgs.sleep == None:
            self.TestArgs.sleep = 0.5
        if self.TestArgs.folder != None:
            self.TestArgs.folders = [self.TestArgs.folder]
        self.TestArgs.kwargs = {}
        for (key, value) in self.TestArgs._get_kwargs():
            if key != 'kwargs':
                self.TestArgs.kwargs[key] = value

        #arbitrary keyword parsing
        for i in range(0, len(unknown), 2):
            key = unknown[i].replace('-','')
            value = unknown[i+1]
            self.TestArgs.kwargs[key] = value

        print(self.TestArgs)
        sys.TestArgs = self.TestArgs
        return self.TestArgs

def RunCmd(CommandString, silent=True, cwd=os.path.dirname(os.path.abspath(__file__)).replace('\\','/')):
    if not silent:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('KungFu.RunCmd', CommandString)
        print('run_command', shlex.split(CommandString))
        print('cwd', cwd)
    result = u""
    try:
        with subprocess.Popen(shlex.split(CommandString), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd) as proc:
            stdout, stderr = proc.communicate()
            print('stderr!', stderr)
            #while True:
            #    stdout = proc.stdout.readline()
            #    if stdout:
            #        result += stdout.decode('utf8')
            #        if not silent:
            #            print(stdout.decode('utf8'))
            #    if proc.poll() is not None:
            #        break
            returncode = proc.poll()
            result += stdout.decode('utf8')
            result += stderr.decode('utf8')
    except:
        result += traceback.format_exc()
        returncode = 1
    if not silent:
        print('returncode', returncode)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return result, returncode

def main(*args):
    Dependencies = DependencyHandler()
    TestInstance = TestRunner(*args)
    TestInstance.main()
    Dependencies.offer_installers()

if __name__ == '__main__':
    main()
##################################################
