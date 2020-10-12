#Imports##########################################
import os
from FooFinder import KungFu
from FooFinder import AWSBaseClasses
##################################################

#Code#############################################
class SimpleCluster(AWSBaseClasses.EKSCluster):
    def __init__(self):
        super(SimpleCluster, self).__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__))
##################################################

#Test#############################################
@KungFu.depends('terraform', 'aws')
class test_SimpleCluster(AWSBaseClasses.test_EKSCluster):
    TestCluster = SimpleCluster()
    
    def test_11_SimpleCLuster_init(self): #REPLACEME: Just leaving this as an example for now
        result, returncode = self.__class__.TestCluster.init()
        self.assertEqual(returncode, 0)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
