import os, sys, importlib, unittest

if 'TestKit' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['TestKit'] = importlib.machinery.SourceFileLoader('TestKit', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',2)[0]+'/TestKit.py').load_module()
import TestKit

class SimpleCluster(TestKit.EKSCluster):
    def __init__(self):
        super(SimpleCluster, self).__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__))

class test_SimpleCluster(TestKit.test_EKSCluster):
    TestCluster = SimpleCluster()
    
    def test_11_SimpleCLuster_init(self): #REPLACEME: Just leaving this as an example for now
        result, returncode = self.__class__.TestCluster.init()
        self.assertEqual(returncode, 0)

if __name__ == '__main__':
    unittest.main()
