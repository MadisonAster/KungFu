'''
Recursively searches folders below the location of this file. Runs any unittest class that begins with test_
sys.argv[1] = SkipCount #Takes int as argument, skips first n tests found during search. Use this to speed test cycling during development. Set to zero or leave blank to run all.
sys.argv[2] = SleepTime #Takes floaat as argument, sets all sleep times to n. Use this to keep test windows on the screen for n seconds. Or leave blank to use defaults.
'''
import sys, os, unittest, inspect
import importlib.util
import TestKit

class TestRunner():
    SkippedCount = 0
    def RecursiveImport(self, SkipCount=0, SleepTime=None, Create=False, Destroy=False):
        wd = os.path.dirname(os.path.abspath(__file__))
        for root, dirs, files in os.walk(wd):
            for file in files:
                if file.rsplit('.',1)[-1] == 'py':
                    self.ImportTests(root.replace('\\','/')+'/'+file, SkipCount=SkipCount, SleepTime=SleepTime, Create=Create, Destroy=Destroy)
    def ImportTests(self, ModulePath, SkipCount=0, SleepTime=None, Create=False, Destroy=False, BlackList=['TestKit']):
        ModuleName = ModulePath.rsplit('/',1)[-1].rsplit('.',1)[0]
        if ModuleName in BlackList:
            return
        if ModuleName in globals().keys():
            raise Exception('Namespace conflict found. Module name already in use, pick another.', ModuleName)
        ModuleSpec = importlib.util.spec_from_file_location("module.name", ModulePath)
        Module = importlib.util.module_from_spec(ModuleSpec)
        ModuleSpec.loader.exec_module(Module)
        inspect.getmembers(Module)
        for ClassName, Class in inspect.getmembers(Module):
            if 'test_' in ClassName:
                if ClassName in globals().keys():
                    raise Exception('Namespace conflict found. Class Name already in use, pick another.', ClassName, Module.__file__)
                if self.SkippedCount >= SkipCount:
                    globals()[ClassName] = Class
                else:
                    self.SkippedCount += 1

if __name__ == '__main__':
    TestKit.LoadTestVars()
    TestInstance = TestRunner()
    TestInstance.RecursiveImport(SkipCount=sys.TestVars['SkipCount'])
    unittest.main()