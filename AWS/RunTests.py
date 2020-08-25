'''
Recursively searches folders below the location of this file. Runs any unittest class that begins with test_
sys.argv[1] = SkipCount #Takes int as argument, skips first n tests found during search. Use this to speed test cycling during development. Set to zero or leave blank to run all.
sys.argv[2] = SleepTime #Takes floaat as argument, sets all sleep times to n. Use this to keep test windows on the screen for n seconds. Or leave blank to use defaults.
'''
import sys, os, unittest, inspect
import importlib.util

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
                for FunctionName, Function in inspect.getmembers(Class):
                    if 'test_' in FunctionName:
                        if SleepTime and 'SleepTime' in Function.__code__.co_varnames:
                            i = Function.__code__.co_varnames.index('SleepTime')
                            arglist = list(Function.__defaults__)
                            arglist[i-1] = SleepTime
                            Function.__defaults__ = tuple(arglist)
                        if Create and 'Create' in Function.__code__.co_varnames:
                            i = Function.__code__.co_varnames.index('Create')
                            arglist = list(Function.__defaults__)
                            arglist[i-1] = Create
                            Function.__defaults__ = tuple(arglist)
                        if Destroy and 'Destroy' in Function.__code__.co_varnames:
                            i = Function.__code__.co_varnames.index('Destroy')
                            arglist = list(Function.__defaults__)
                            arglist[i-1] = Destroy
                            Function.__defaults__ = tuple(arglist)
                if ClassName in globals().keys():
                    raise Exception('Namespace conflict found. Class Name already in use, pick another.', ClassName, Module.__file__)
                if self.SkippedCount >= SkipCount:
                    globals()[ClassName] = Class
                else:
                    self.SkippedCount += 1

if __name__ == '__main__':
    TestInstance = TestRunner()
    if len(sys.argv) < 2:
        TestInstance.RecursiveImport()
    else:
        SkipCount = 0
        SleepTime = None
        Create = False
        Destroy = False
        if len(sys.argv) >= 2:
            SkipCount = int(sys.argv[1])
            print('SkipCount', SkipCount)
        if len(sys.argv) >= 3:
            SleepTime = float(sys.argv[2])
            print('SleepTime', SleepTime)
        if len(sys.argv) >= 4:
            Create = sys.argv[3] == 'True'
            print('Create', Create)
        if len(sys.argv) >= 5:
            Destroy = sys.argv[4] == 'True'
            print('Destroy', Destroy)
        TestInstance.RecursiveImport(SkipCount=SkipCount, SleepTime=SleepTime, Create=Create, Destroy=Destroy)
    del sys.argv[1:]
    unittest.main()
