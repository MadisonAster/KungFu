#Imports##########################################
import os
from FooFinder import KungFu
from FooFinder import EKSCluster
from FooFinder import envsubst
##################################################

#Code#############################################
class EBSCluster(EKSCluster.EKSCluster):
    def __init__(self):
        super().__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__))
    def apply(self):
        result0, returncode0 = super().apply()
        rdata, returncode1 = self.output()
        result2, returncode2 = self.run_command('kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=master"')
        #envsubst.envsubst(self.cwd+'/eks_ebsvolume.yaml', self.cwd+'/eks_ebsvolume_temp.yaml', rdata)
        
        #result3, returncode3 = self.run_command('kubectl apply -f '+self.cwd+'/eks_ebsvolume_temp.yaml')

        returncodes = 0
        for r in [returncode0, returncode1, returncode2]:
            returncodes += int(r)
        returncodes = bool(returncodes)
        return result0, returncodes
##################################################

#Test#############################################
@KungFu.depends('terraform', 'aws')
class test_EBSCluster(EKSCluster.test_EKSCluster):
    def __init__(self, *args):
        super().__init__(*args)
        self.TestCluster = EBSCluster()
    
    def test_11_EBSCluster_init(self): #REPLACEME: Just leaving this as an example for now
        result, returncode = self.TestCluster.init()
        self.assertEqual(returncode, 0)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
