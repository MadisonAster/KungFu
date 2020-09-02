import sys, os
import unittest, importlib
from datetime import datetime
import subprocess, shlex

if 'TestKit' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['TestKit'] = importlib.machinery.SourceFileLoader('TestKit', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',1)[0]+'/TestKit.py').load_module()
import TestKit

class EKSCluster(dict):
    def __init__(self):
        super(EKSCluster, self).__init__()
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
        for line in result.rstrip().split('\n'):
            (var, val) = line.replace(' = ','=').split('=',1)
            self[var] = val
        return result, returncode

    def run_command(self, CommandString, printout=True):
        if printout:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('run_command', CommandString)
        result = u""
        with subprocess.Popen(shlex.split(CommandString), stdout=subprocess.PIPE, cwd=self.cwd) as proc:
            while True:
                stdout = proc.stdout.readline()
                if stdout:
                    result += stdout.decode('utf8')
                    if printout:
                        print(stdout.decode('utf8'))
                if proc.poll() is not None:
                    break
            returncode = proc.poll()
        if printout:
            print('returncode', returncode)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return result, returncode

class test_EKSCluster(TestKit.TimedTest):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    @TestKit.depends('terraform', 'aws')
    def test_01_init(self):
        result, returncode = self.__class__.TestCluster.init()
        self.assertEqual(returncode, 0)
    
    @TestKit.depends('terraform', 'aws')
    def test_02_plan(self):
        result, returncode = self.__class__.TestCluster.plan()
        self.assertEqual(returncode, 0)

    @TestKit.depends('terraform', 'aws')
    def test_03_plan_destroy(self):
        result, returncode = self.__class__.TestCluster.plan_destroy()
        self.assertEqual(returncode, 0)

    @TestKit.depends('terraform', 'aws')
    @TestKit.create
    def test_04_apply(self):
        result, returncode = self.__class__.TestCluster.apply()
        self.assertEqual(returncode, 0)

    @TestKit.depends('terraform', 'aws')
    @TestKit.create
    def test_05_output(self):
        result, returncode = self.__class__.TestCluster.output()
        print('vpc_id', self.__class__.TestCluster['vpc_id'])
        self.assertEqual(returncode, 0)

    @TestKit.depends('terraform', 'aws')
    @TestKit.destroy
    def test_06_destroy(self):
        result, returncode = self.__class__.TestCluster.destroy()
        self.assertEqual(returncode, 0)
