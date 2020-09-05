#Standard Imports#################################
import sys, os
import unittest
from importlib import machinery
import subprocess, shlex
import types
import functools
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',1)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Code#############################################
class CPPTestParser():
    def __init__(self):
        super(CPPTestParser, self).__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
        self.exepath = self.cwd+'/x64/Debug/Kata.exe'
        self.results = {}

    def run(self):
        print('#######################################################')
        print('Running C++ tests:')
        result, returncode = self.run_command(self.exepath)
        print(result)
        nextline = False
        for line in result.rstrip().split('\n'):
            if nextline:
                nextline = False
                result = 'OK' in line[0:12]
                testtime = line.split(testname,1)[-1].strip()
                self.results[testname] = (result, testtime)
            if 'RUN' in line[0:12]:
                testname = line[13:].strip().rstrip().split('.',1)[-1]
                nextline = True
        print('#######################################################')
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
##################################################

#Test#############################################
#@KungFu.depends('msvc', 'gcc')
class test_CPPTestParser(unittest.TestCase):
    def prototest(self, *args, testname=''):
        (result, testtime) = self.parser.results[testname]
        success = 'executed' if result else 'failed'
        self.assertEqual(result, True)

    def add_tests(cls):
        cls.parser = CPPTestParser()
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

if False: #Need to run the compiler still before I enable this
    test_CPPTestParser.add_tests(test_CPPTestParser)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################

