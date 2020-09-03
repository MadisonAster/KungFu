'''
Recursively searches folders below the location of this file. 
Runs any unittest class that begins with test_

examples:
python3 KungFu.py                          #run all tests, automatically decide if gui is available

python3 KungFu.py -sleep 1.0               #run tests with a sleeptime of 1.0 seconds
python3 KungFu.py -folder Python/Qt        #run all tests in the Python/Qt folder
python3 KungFu.py -folders Python,AWS      #run all tests in the Python and AWS folders
python3 KungFu.py -gui True                #Force gui tests to run.
python3 KungFu.py -gui False               #Force gui tests not to run.
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

#Dependency Handling##############################
class DependencyHandler():
    cwd = os.path.dirname(os.path.abspath(__file__))
    Installed = []
    NotInstalled = {}
    SkipCount = 0
    def __new__(cls, *args, **kwargs):
        if not hasattr(sys, 'DependencyHandler'): #Global Singleton
            sys.DependencyHandler = super(DependencyHandler, cls).__new__(cls, *args, **kwargs)
        return sys.DependencyHandler

    def check(self, name):
        if name in self.Installed:
            return True
        elif name in self.NotInstalled.keys():
            return False
        else:
            for FunctionName, Function in inspect.getmembers(self.__class__):
                if FunctionName == 'check_'+name:
                    print('check_'+name)
                    return Function(self)

    def run_installers(self):
        if len(self.NotInstalled.keys()) == 0:
            return
        else:
            print(str(self.SkipCount)+" tests couldn't run because the following tools were not found on your system:\n")
            for key in self.NotInstalled.keys():
                print(key)
            print('\n')

            print('----------------------------------------------------------------------')
            print('Automated Dependency Installers:')
            print('\n')
            print('THIS CODE IS STILL UNTESTED! RUN AT YOUR OWN RISK!')

            if 'gui' in self.NotInstalled.keys():
                del self.NotInstalled['gui']
            for key in self.NotInstalled.keys():
                function = self.NotInstalled[key]
                if function:
                    answer = input('Would you like to try installing '+key+'? ')
                    answer = answer.lower() in ['y', 'yes', 'true']
                    if answer == True:
                        function()
        
    @contextlib.contextmanager
    def GetStderrIO(self, stderr=None):
        old = sys.stderr
        if stderr is None:
            stderr = io.StringIO()
        sys.stderr = stderr
        yield stderr
        sys.stderr = old

    def run_command(self, CommandString, silent=True):
        if not silent:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('run_command', CommandString)
        result = u""
        try:
            with subprocess.Popen(shlex.split(CommandString), stdout=subprocess.PIPE, cwd=self.cwd) as proc:
                while True:
                    stdout = proc.stdout.readline()
                    if stdout:
                        result += stdout.decode('utf8')
                        if not silent:
                            print(stdout.decode('utf8'))
                    if proc.poll() is not None:
                        break
                returncode = proc.poll()
        except:
            result += traceback.format_exc()
            returncode = 1
        if not silent:
            print('returncode', returncode)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return result, returncode

    def check_terraform(self):
        result, returncode = self.run_command('terraform -help')
        returncode = not bool(returncode)
        if returncode:
            self.Installed.append('terraform')
        else:
            self.NotInstalled['terraform'] = self.install_terraform
        return returncode
    def install_terraform(self):
        self.run_command('curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -')
        self.run_command('sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"')
        self.run_command('sudo apt-get update && sudo apt-get install terraform')
        self.run_command('terraform -help')

    def check_aws(self):
        result, returncode = self.run_command('aws --version')
        returncode = not bool(returncode)
        if returncode:
            self.Installed.append('aws')
        else:
            self.NotInstalled['aws'] = self.install_aws
        return returncode
    def install_aws(self):
        self.run_command('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
        self.run_command('unzip awscliv2.zip')
        self.run_command('sudo ./aws/install')
        self.run_command('aws --version')

    def check_kubectl(self):
        result, returncode = self.run_command('kubectl version --short --client')
        returncode = not bool(returncode)
        if returncode:
            self.Installed.append('kubectl')
        else:
            self.NotInstalled['kubectl'] = self.install_kubectl
        return returncode
    def install_kubectl(self):
        self.run_command('curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.17.9/2020-08-04/bin/linux/amd64/kubectl')
        self.run_command('chmod +x ./kubectl')
        self.run_command('mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/awskubectl && export PATH=$PATH:$HOME/bin') #naming kubectl binary awskubectl to avoid potential WSL2 conflicts
        #self.run_command('echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc')
        self.run_command('kubectl version --short --client')

    def check_gui(self):
        try:
            with self.GetStderrIO() as stderr:
                from Qt import QtCore
            if stderr.getvalue() == '':
                self.Installed.append('gui')
                installed = True
            else:
                print('X server not available! Disabling gui tests!')
                self.NotInstalled['gui'] = None
                installed = False
        except ImportError as exception:
            print('Qt not available! Disabling gui tests!')
            self.NotInstalled['gui'] = None
            installed = False
        print('gui installed', installed)
        return installed
    def check_qt(self):
        try:
            from Qt import QtCore
            installed = True
        except ImportError as exception:
            installed = False
        if installed:
            self.Installed.append('qt')
        else:
            self.NotInstalled['qt'] = self.install_qt
        print('qt installed', installed)
        return installed
    def install_qt(self):
        self.run_command('pip3 install pyside2')
        self.run_command('pip3 install qt.py')

    def check_docker(self):
        result, returncode = self.run_command('docker --version')
        returncode = not bool(returncode)
        if returncode:
            self.Installed.append('docker')
        else:
            self.NotInstalled['docker'] = self.install_docker
        return returncode
    def install_docker(self):
        pass

    def check_pandas(self):
        try:
            import pandas    
            installed = True
        except ImportError as exception:
            installed = False
        if installed:
            self.Installed.append('pandas')
        else:
            self.NotInstalled['pandas'] = self.install_pandas
        return installed
    def install_pandas(self):
        self.run_command('pip3 install pandas')
##################################################

#Base Classes#####################################
def PartialWrapper(func, self, **kwargs):
    if type(func)==functools.partial:
        return func(**kwargs)
    new_kwargs = {}
    arglist = list(func.__defaults__)
    for key in kwargs:
        if key in func.__code__.co_varnames:
            i = func.__code__.co_varnames.index(key)
            arglist[i-1] = kwargs[key]
    func.__defaults__ = tuple(arglist)
    return func(self)

class TimedTest(unittest.TestCase):
    def __init__(self, *args):
        super(TimedTest, self).__init__(*args)
        for FunctionName, Function in inspect.getmembers(self.__class__):
            if Function and 'test_' in FunctionName:
                partial = functools.partial(PartialWrapper, Function, self, **sys.TestArgs.kwargs)
                setattr(self.__class__, FunctionName, partial)

    def setUp(self):
        self.starttime = datetime.now()

    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())
##################################################

#Main#############################################
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
        self.Runner = unittest.TextTestRunner(descriptions=0)
        result = self.Runner.run(self.TestSuite)
        print('----------------------------------------------------------------------')
        print('Ran '+str(result.testsRun)+' tests.')
        print('\n')

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
        print('ImportTests', ModuleName)
        if ModuleName in ['KungFu'] or 'BaseClasses' in ModuleName:
            return
        if ModuleName in globals().keys():
            raise Exception('Namespace conflict found. Module name already in use, pick another.', ModuleName)
        ModuleSpec = util.spec_from_file_location("module.name", ModulePath)
        Module = util.module_from_spec(ModuleSpec)
        try:
            ModuleSpec.loader.exec_module(Module)
        except Exception as e: #Module level return doesn't exist. This is a compelling use case. Maybe a PEP?
            if str(e) == 'return':
                pass
            else:
                print(traceback.format_exc())
                raise e

        inspect.getmembers(Module)
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
        parser.add_argument("-gui", help="Specify whether or not to run GUI tests.", type=bool)
        parser.add_argument("--create", help="provision cloud resources, (this will cost money!)", action="store_true")
        parser.add_argument("--destroy", help="destroy cloud resources, (this will destory resouces!)", action="store_true")

        self.TestArgs, unknown = parser.parse_known_args()
        if self.TestArgs.sleep == None:
            self.TestArgs.sleep = 0.5
        if self.TestArgs.folder != None:
            self.TestArgs.folders = [self.TestArgs.folder]
        if self.TestArgs.gui == None:
            print('testargs check gui!')
            self.TestArgs.gui = DependencyHandler().check('gui')
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

def main(*args):
    Dependencies = DependencyHandler()
    TestInstance = TestRunner(*args)
    TestInstance.main()
    Dependencies.run_installers()

if __name__ == '__main__':
    main()
##################################################
