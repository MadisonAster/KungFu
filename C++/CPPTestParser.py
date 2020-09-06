#Standard Imports#################################
import sys, os, unittest
from importlib import machinery
import subprocess, shlex
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
        #insert compile command, and os check here
        print('sys.platform', sys.platform)
        self.exepath = self.cwd+'/x64/Debug/Kata.exe'
        self.results = {}

    def run(self):
        print('#######################################################')
        print('Running C++ tests:')
        result, returncode = KungFu.RunCmd(self.exepath, cwd=self.cwd)
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
    
    
##################################################

#Test#############################################
#@KungFu.depends('msvc', 'gcc')
class test_CPPTestParser(KungFu.PrototypeTestParser):
    pass

if False:
    test_CPPTestParser.add_tests(test_CPPTestParser, CPPTestParser)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################

