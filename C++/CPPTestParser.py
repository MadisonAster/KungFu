#Imports##########################################
from FooFinder import KungFu
##################################################

#Code#############################################
import sys, os
import subprocess, shlex
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

if False: #disabling for now, until compiler is done
    test_CPPTestParser.AddTests(CPPTestParser)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################

