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
class GoTestParser():
    def run(self):
        self.results = {}

        print('#######################################################')
        print('Running Go tests:')
        cwd = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
        result, returncode = KungFu.RunCmd('go test -v', cwd=cwd)
        print(result)
        nextline = False
        for line in result.rstrip().split('\n'):
            if nextline:
                nextline = False
                result = 'PASS' in line[0:8]
                testtime = line.split(testname,1)[-1].strip()
                self.results[testname] = (result, testtime)
            if 'RUN' in line[0:7]:
                testname = line[10:].rstrip()
                nextline = True
        print('#######################################################')
##################################################

#Test#############################################
@KungFu.depends('go')
class test_GoTestParser(KungFu.PrototypeTestParser):
    pass

if True:
    test_GoTestParser.AddTests(test_GoTestParser, GoTestParser)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################

