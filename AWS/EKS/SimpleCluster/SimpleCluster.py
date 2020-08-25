import os, sys, imp, unittest

if 'TestKit' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['TestKit'] = imp.load_source('TestKit', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',2)[0]+'/TestKit.py')
import TestKit

class SimpleCluster(TestKit.EKSCluster):
    def __init__(self):
        super(SimpleCluster, self).__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__))

class test_SimpleCluster(TestKit.test_EKSCluster):
    TestCluster = SimpleCluster()
    
    def test_11_SimpleCLuster_init(self):
        result, returncode = self.__class__.TestCluster.init()
        self.assertEqual(returncode, 0)

if __name__ == '__main__':
    unittest.main()