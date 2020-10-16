#Imports##########################################
import os
from FooFinder import KungFu
from FooFinder import EKSCluster
##################################################

#Code#############################################
class EFSCluster(EKSCluster.EKSCluster):
    def __init__(self):
        super().__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__))
    def apply(self):
        result0, returncode0 = super().apply()
        rdata, returncode1 = self.output()
        result2, returncode2 = self.run_command('kubectl apply -k "github.com/kubernetes-sigs/aws-efs-csi-driver/deploy/kubernetes/overlays/stable/?ref=master"')
        
        returncodes = 0
        for r in [returncode0, returncode1, returncode2]:
            returncodes += int(r)
        returncodes = bool(returncodes)
        return result0, returncodes
##################################################

#Test#############################################
@KungFu.depends('terraform', 'aws')
class test_EFSCluster(EKSCluster.test_EKSCluster):
    def __init__(self, *args):
        super().__init__(*args)
        self.TestCluster = EFSCluster()
    
    def test_11_EFSCluster_init(self): #REPLACEME: Just leaving this as an example for now
        result, returncode = self.TestCluster.init()
        self.assertEqual(returncode, 0)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
