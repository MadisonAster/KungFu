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
class NPMTestParser():
    def run(self):
        self.results = {}
       
        print('#######################################################')
        print('Running Javascript tests:')
        cwd = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
        result, returncode = KungFu.RunCmd('npm test', cwd=cwd, shell=True)
        nextline = False
        print(result)
        for line in result.rstrip().split('\n'):
            if u'\u221A' in line:
                result = True
                testinfo = line.split('\u221A')[-1].strip()
                testname = testinfo.rsplit(' (',1)[0]
                testtime = '('+testinfo.rsplit(' (',1)[-1]
                self.results[testname] = (result, testtime)
            elif u'\u00D7' in line:
                result = False
                testinfo = line.split('\u00D7')[-1].strip()
                testname = testinfo.rsplit(' (',1)[0]
                testtime = '('+testinfo.rsplit(' (',1)[-1]
                self.results[testname] = (result, testtime)
            else:
                print(line)
        print('#######################################################')
##################################################

#Test#############################################
@KungFu.depends('nodejs', 'jest')
class test_NPMTestParser(KungFu.PrototypeTestParser):
    pass

if test_NPMTestParser != None:
    test_NPMTestParser.AddTests(NPMTestParser)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################

