#Imports##########################################
import os
from FooFinder import KungFu
from FooFinder import EKSCluster
##################################################

#Code#############################################
class FullCluster(EKSCluster.EKSCluster):
    def __init__(self):
        super(FullCluster, self).__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__))
##################################################

#Test#############################################
@KungFu.depends('terraform', 'aws')
class test_FullCluster(EKSCluster.test_EKSCluster):
    def __init__(self, *args):
        super().__init__(*args)
        self.TestCluster = FullCluster()
    
    def test_11_FullCluster_init(self): #REPLACEME: Just leaving this as an example for now
        result, returncode = self.TestCluster.init()
        self.assertEqual(returncode, 0)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
