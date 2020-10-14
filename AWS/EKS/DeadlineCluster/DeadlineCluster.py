#Imports##########################################
import os
from FooFinder import KungFu
from FooFinder.EKS import EKSCluster
##################################################

#Code#############################################
class DeadlineCluster(EKSCluster.EKSCluster):
    def __init__(self):
        super(DeadlineCluster, self).__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__))
##################################################

#Test#############################################
@KungFu.depends('terraform', 'aws')
class test_DeadlineCluster(EKSCluster.test_EKSCluster):
    TestCluster = DeadlineCluster()
    
    def test_11_DeadlineCluster_init(self): #REPLACEME: Just leaving this as an example for now
        result, returncode = self.__class__.TestCluster.init()
        self.assertEqual(returncode, 0)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
