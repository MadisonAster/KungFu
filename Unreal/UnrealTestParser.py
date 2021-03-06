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
        result, returncode = KungFu.RunCmd("UE4Editor-Cmd.exe '"+cwd+"/KungFu.uproject' -ExecCmds='Automation RunFilter Engine; quit' -stdout", cwd=cwd)
        #result, returncode = KungFu.RunCmd("UE4Editor-Cmd.exe '"+cwd+"/KungFu.uproject' -Game -ExecCmds='Automation RunFilter Smoke; quit' -log", cwd=cwd, silent=False, shell=True)
        #result, returncode = KungFu.RunCmd("UE4Editor-Cmd.exe '"+cwd+"/KungFu.uproject' -ExecCmds='Automation RunFilter Engine; quit' -stdout", cwd=cwd, shell=True)
        #W:\"Epic Games"\UnrealEngine\Engine\Build\BatchFiles\GenerateProjectFiles.bat "W:\Portfolio\KungFu\Unreal\KungFu.uproject"
        
        #epath, _ = KungFu.RunCmd('where UE4Editor-Cmd.exe')
        #epath = epath.replace('\\','/').split('/Binaries',1)[0]
        #result, returncode = KungFu.RunCmd(epath+'/Build/BatchFiles/Build.bat UE4Editor Win64 Debug "'+cwd+'/KungFu.uproject" -waitmutex', cwd=cwd)

        print(result)
        for line in result.rstrip().split('\n'):
            if 'Result={Passed}' in line:
                result = True
                testname = line.split('Name={',1)[-1].split('}',1)[0]
                testtime = line.split('[',2)[-1].split(']',1)[0]
                self.results[testname] = (result, testtime)
            elif 'Result={Failed}' in line:
                result = False
                testname = line.split('Name={',1)[-1].split('}',1)[0]
                testtime = line.split('[',2)[-1].split(']',1)[0]
                self.results[testname] = (result, testtime)
            else:
                pass
                #print(line)
        print('#######################################################')
##################################################

#Test#############################################
@KungFu.depends('unreal')
class test_UnrealTestParser(KungFu.PrototypeTestParser):
    pass

if test_UnrealTestParser != None and __name__ != '__main__':
    test_UnrealTestParser.AddTests(UnrealTestParser)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################

