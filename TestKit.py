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
import subprocess, shlex
import traceback

import io
import contextlib

######TestArg Decorators######
'''
def TestArgDecorator(func):
    print(inspect.currentframe().f_code.co_name)
    print(inspect.currentframe().f_trace)
    print(dir(inspect.currentframe()))
    if not getattr(sys.TestArgs, func.__name__):
        print('Skipping '+func.__name__+' Test')
        return None
    else:
        return func

globals()['gui'] = TestArgDecorator
globals()['create'] = TestArgDecorator
globals()['destroy'] = TestArgDecorator
'''

def gui(func):
    print('gui decorator')
    if sys.TestArgs.gui == None:
        qt(func)
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
##############################

#####Software Decorators######
'''
def SoftwareDecorator(func):
    print(inspect.currentframe().f_code.co_name)
    print(inspect.currentframe().f_trace)
    print(dir(inspect.currentframe()))
    if not DependencyHandler().check(func.__name__):
        print('Skipping '+func.__name__+' test')
        return None
    else:
        return func

globals()['qt'] = SoftwareDecorator
globals()['terraform'] = SoftwareDecorator
globals()['aws'] = SoftwareDecorator
globals()['kubectl'] = SoftwareDecorator
globals()['docker'] = SoftwareDecorator
globals()['pandas'] = SoftwareDecorator
'''
def terraform(func):
    if not DependencyHandler().check('terraform'):
        print('Skipping terraform test')
        if func != None:
            DependencyHandler().SkipCount += 1
        return None
    else:
        return func

def aws(func):
    if not DependencyHandler().check('aws'):
        print('Skipping aws test')
        if func != None:
            DependencyHandler().SkipCount += 1
        return None
    else:
        return func

def kubectl(func):
    if not DependencyHandler().check('kubectl'):
        print('Skipping kubectl test')
        if func != None:
            DependencyHandler().SkipCount += 1
        return None
    else:
        return func

def qt(func):
    print('qt decorator')
    if not DependencyHandler().check('qt'):
        print('Skipping qt test')
        if func != None:
            DependencyHandler().SkipCount += 1
        return None
    else:
        return func

def docker(func):
    if not DependencyHandler().check('docker'):
        print('Skipping docker test')
        if func != None:
            DependencyHandler().SkipCount += 1
        return None
    else:
        return func
##############################

#####Dependency Handling######
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
                    return Function(self)

    def run_installers(self):
        if 'gui' in self.NotInstalled.keys():
            del self.NotInstalled['gui']
        if len(self.NotInstalled.keys()) == 0:
            return
        else:
            print(str(self.SkipCount)+" tests couldn't run because the following tools were not found on your system:")
            for key in self.NotInstalled.keys():
                print(key)
            print('Would you like to try installing them automatically?')
            print('(THESE ARE 3RD PARTY TOOLS AND THIS IS STILL UNTESTED! RUN AT YOUR OWN RISK!)')
            
            try_installers = False
            if try_installers:
                for function in self.NotInstalled.values():
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
        print('check_terraform')
        result, returncode = self.run_command('terraform -help')
        returncode = not bool(returncode)
        returncode = True
        if returncode:
            self.Installed.append('terraform')
        else:
            self.NotInstalled['terraform'] = self.install_terraform
        return returncode
    def install_terraform(self):
        print('install_terraform')
        self.run_command('curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -')
        self.run_command('sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"')
        self.run_command('sudo apt-get update && sudo apt-get install terraform')
        self.run_command('terraform -help')

    def check_aws(self):
        print('check_aws')
        result, returncode = self.run_command('aws --version')
        returncode = not bool(returncode)
        if returncode:
            self.Installed.append('aws')
        else:
            self.NotInstalled['aws'] = self.install_aws
        return returncode
    def install_aws(self):
        print('install_aws')
        self.run_command('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
        self.run_command('unzip awscliv2.zip')
        self.run_command('sudo ./aws/install')
        self.run_command('aws --version')

    def check_kubectl(self):
        print('check_kubectl')
        result, returncode = self.run_command('kubectl version --short --client')
        returncode = not bool(returncode)
        if returncode:
            self.Installed.append('kubectl')
        else:
            self.NotInstalled['kubectl'] = self.install_kubectl
        return returncode
    def install_kubectl(self):
        print('install_kubectl')
        self.run_command('curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.17.9/2020-08-04/bin/linux/amd64/kubectl')
        self.run_command('chmod +x ./kubectl')
        self.run_command('mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/awskubectl && export PATH=$PATH:$HOME/bin') #naming kubectl binary awskubectl to avoid potential WSL2 conflicts
        #self.run_command('echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc')
        self.run_command('kubectl version --short --client')

    def check_gui(self):
        self.check_qt()
    def check_qt(self):
        print('check_qt')
        try:
            with self.GetStderrIO() as stderr:
                exec("from Qt import QtCore")
            if stderr.getvalue() == '':
                print('installed')
                self.Installed.append('gui')
                installed = True
            else:
                print('X server not available! Disabling gui tests!')
                self.NotInstalled['gui'] = None
                installed = True
        except ImportError as exception:
            print('exception')
            installed = False
        print('installed', installed)
        if installed:
            self.Installed.append('qt')
        else:
            self.NotInstalled['qt'] = self.install_qt
        return installed
    def install_qt(self):
        print('install_qt')
        self.run_command('pip3 install pyside2')
        self.run_command('pip3 install qt.py')

    def check_docker(self):
        print('check_docker')
        result, returncode = self.run_command('docker --version')
        returncode = not bool(returncode)
        if returncode:
            self.Installed.append('docker')
        else:
            self.NotInstalled['docker'] = self.install_docker
        return returncode
    def install_docker(self):
        print('install_docker')

    def check_pandas(self):
        print('check_pandas')
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
        print('install_pandas')
        self.run_command('pip3 install pandas')
##############################

#########Base Classes#########
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
##############################

#############Main#############
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
        print('ImportTests', ModuleName)
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
        self.TestArgs = parser.parse_args()
        if self.TestArgs.sleep == None:
            self.TestArgs.sleep = 0.5
        if self.TestArgs.folder != None:
            self.TestArgs.folders = [self.TestArgs.folder]
        if self.TestArgs.gui == None:
            self.TestArgs.gui = DependencyHandler().check('gui')
        print(self.TestArgs)
        sys.TestArgs = self.TestArgs
        return self.TestArgs

if __name__ == '__main__':
    Dependencies = DependencyHandler()
    TestInstance = TestRunner()
    TestInstance.main()
    Dependencies.run_installers()
    #unittest.main()
##############################