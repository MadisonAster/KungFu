#Imports##########################################
import os
from FooFinder import KungFu
from FooFinder import EKSCluster
from FooFinder import envsubst
##################################################

#Code#############################################
class ALBCluster(EKSCluster.EKSCluster):
    def __init__(self):
        super().__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__))
    def apply(self):
        result0, returncode0 = super().apply()
        rdata, returncode1 = self.output()
        print('rdata', rdata)
        result2, returncode2 = self.run_command("eksctl utils associate-iam-oidc-provider --region "+rdata["region_id"]+" --cluster "+rdata["cluster_id"]+" --approve")
        result3, returncode3 = self.run_command("aws iam create-policy --policy-name <ALBIngressControllerIAMPolicy> --policy-document file://iam-policy.json")
        result4, returncode4 = self.run_command("kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.8/docs/examples/rbac-role.yaml")
        
        result5, returncode5 = self.run_command("\
            eksctl create iamserviceaccount \
                --region <region-code> \
                --name <alb-ingress-controller> \
                --namespace kube-system \
                --cluster <prod> \
                --attach-policy-arn arn:aws:iam::<111122223333>:policy/<ALBIngressControllerIAMPolicy> \
                --override-existing-serviceaccounts \
                --approve\
        ")
        
        #result6    create service account
        returncode6 = False

        result7, returncode7 = self.run_command("kubectl annotate serviceaccount -n kube-system alb-ingress-controller \
            eks.amazonaws.com/role-arn=arn:aws:iam::<111122223333>:role/<eks-alb-ingress-controller>")
        
        envsubst.envsubst(self.cwd+"/alb-ingress-controller.yaml", self.cwd+"/alb-ingress-controller_temp.yaml", rdata)
        result8, returncode8 = self.run_command("kubectl apply -f "+self.cwd+"/alb-ingress-controller_temp.yaml")
        
        result9, returncode9 = self.run_command("kubectl get pods -n kube-system")
        print('result9', result9)

        returncodes = 0
        for r in [returncode0, returncode1, returncode2, returncode3, returncode4,  returncode5, returncode6, returncode7, returncode8, returncode9]:
            returncodes += int(r)
        returncodes = bool(returncodes)
        return result0, returncodes
##################################################

#Test#############################################
@KungFu.depends('terraform', 'aws')
class test_ALBCluster(EKSCluster.test_EKSCluster):
    def __init__(self, *args):
        super().__init__(*args)
        self.TestCluster = ALBCluster()
    
    def test_11_ALBCluster_init(self): #REPLACEME: Just leaving this as an example for now
        result, returncode = self.TestCluster.init()
        self.assertEqual(returncode, 0)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
