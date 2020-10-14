#Imports##########################################
import os
from FooFinder import KungFu
##################################################

#Code#############################################
import subprocess, shlex
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
        return self.run_command('terraform apply "KungFu.tfplan"')
    def destroy(self):
        return self.run_command('terraform apply "KungFu_destroy.tfplan"')

    def output(self):
        result, returncode = self.run_command('terraform output')
        print('result')
        for line in result.rstrip().split('\n'):
            print(line,)
            print('\n\n')
        for line in result.rstrip().split('\n'):
            if ' = ' in line:
                (var, val) = line.replace(' = ','=').split('=',1)
                self[var] = val
        return result, returncode

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
    def test_01_init(self):
        self.TestCluster = EKSCluster()
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
        print('vpc_id', self.TestCluster['vpc_id'])
        self.assertEqual(returncode, 0)

    @KungFu.destroy
    def test_06_destroy(self):
        result, returncode = self.TestCluster.destroy()
        self.assertEqual(returncode, 0)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################

