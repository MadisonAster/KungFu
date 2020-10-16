#Imports##########################################
import os
from FooFinder import KungFu
##################################################

#Code#############################################
import subprocess, shlex, json
class EKSCluster(dict):
    def __init__(self):
        super(EKSCluster, self).__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__))

    def init(self):
        return self.run_command('terraform init')
    def plan(self):
        return self.run_command('terraform plan -out=KungFu.tfplan')
    def plan_destroy(self):
        return self.run_command('terraform plan -destroy -out=KungFu_destroy.tfplan')
    def apply(self):
        result0, returncode0 = self.run_command('terraform apply "KungFu.tfplan"')

        rdata, returncode1 = self.output()

        #cluster_name = rdata['cluster_name']
        #kubernetes_namespace = rdata['kubernetes_namespace']
        #fargate_profile_name = rdata['fargate_profile_name']
        
        #create fargate profile
        #result3, returncode3 = self.run_command('eksctl create fargateprofile --cluster '+rdata['cluster_name']+' --name '+rdata['fargate_profile_name']+' --namespace '+rdata['kubernetes_namespace'])
        #print('result3')
        #print(result3)
        
        #recreate existing pods?
        #result4, returncode4 = self.run_command('kubectl rollout restart -n <kube-system> <deployment coredns>')
        
        returncodes = 0
        for r in [returncode0, returncode1]:
            returncodes += int(r)
        returncodes = bool(returncodes)
        return rdata, returncode0

    def destroy(self):
        return self.run_command('terraform apply "KungFu_destroy.tfplan"')

    def output(self):
        result, returncode = self.run_command('terraform output -json')
        rdata = json.loads(result)
        if 'EKSCluster' in rdata.keys():
            for key, value in rdata['EKSCluster']['value'].items():
                rdata[key] = value
        for key, value in rdata.items():
            if hasattr(value, 'keys') and 'value' in value.keys():
                rdata[key] = value['value']
                #self[key] = value['value']
        return rdata, returncode

    def run_command(self, CommandString, silent=True):
        if not silent:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('run_command', CommandString)
        result = u""
        with subprocess.Popen(shlex.split(CommandString), stdout=subprocess.PIPE, cwd=self.cwd) as proc:
            while True:
                stdout = proc.stdout.readline()
                if stdout:
                    result += stdout.decode('utf8')
                    if not silent:
                        print(stdout.decode('utf8'))
                if proc.poll() is not None:
                    break
            returncode = proc.poll()
        if not silent:
            print('returncode', returncode)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return result, returncode
##################################################

#Test#############################################
@KungFu.depends('base', 'terraform', 'aws')
class test_EKSCluster(KungFu.TimedTest):
    def __init__(self, *args):
        super().__init__(*args)
        self.TestCluster = EKSCluster()

    def test_01_init(self):
        result, returncode = self.TestCluster.init()
        self.assertEqual(returncode, 0)
    
    def test_02_plan(self):
        result, returncode = self.TestCluster.plan()
        self.assertEqual(returncode, 0)

    def test_03_plan_destroy(self):
        result, returncode = self.TestCluster.plan_destroy()
        self.assertEqual(returncode, 0)

    @KungFu.create
    def test_04_apply(self):
        result, returncode = self.TestCluster.apply()
        self.assertEqual(returncode, 0)

    @KungFu.create
    def test_05_output(self):
        result, returncode = self.TestCluster.output()
        #print('vpc_id', self.TestCluster['vpc_id'])
        self.assertEqual(returncode, 0)

    @KungFu.destroy
    def test_99_destroy(self):
        result, returncode = self.TestCluster.destroy()
        self.assertEqual(returncode, 0)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################

