#Imports##########################################
from FooFinder import KungFu
##################################################

#Code#############################################
import os
class UnrealTestParser():
    def run(self):
        self.results = {}
       
        print('#######################################################')
        print('Running Unreal tests:')
        cwd = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
        result, returncode = KungFu.RunCmd('unreal', cwd=cwd, shell=True)
        nextline = False
        return False
        
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
#@KungFu.depends('nodejs', 'npm.jest')
#class test_UnrealTestParser(KungFu.PrototypeTestParser):
#    pass

#if test_UnrealTestParser != None:
#    test_UnrealTestParser.AddTests(UnrealTestParser)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################

