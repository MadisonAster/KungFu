#Imports##########################################
from FooFinder import KungFu
##################################################

#Code#############################################
import os
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

if test_GoTestParser != None and __name__ != '__main__':
    test_GoTestParser.AddTests(GoTestParser)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################

