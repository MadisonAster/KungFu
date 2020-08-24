import unittest
from datetime import datetime

import subprocess
import shlex


class SimpleCluster():
    def __init__(self):
        super(SimpleCluster, self).__init__()
    def init(self):
        return run_command('terraform init')
    def plan(self):
        return run_command('terraform plan -out=KungFu.tfplan')
    def plan_destroy(self):
        return run_command('terraform plan -destroy -out=KungFu_destroy.tfplan')
    def apply(self):
        return run_command('terraform apply "KungFu.tfplan"')
    def destroy(self):
        return run_command('terraform apply "KungFu_destroy.tfplan"')

def run_command(CommandString):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('run_command', CommandString)
    result = u""
    with subprocess.Popen(shlex.split(CommandString), stdout=subprocess.PIPE) as proc:
        while True:
            stdout = proc.stdout.readline()
            if stdout:
                result += stdout.decode('utf8')
                print(stdout.decode('utf8'))
            if proc.poll() is not None:
                break
        returncode = proc.poll()
    print('returncode', returncode)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return result, returncode

class test_SimpleCluster(unittest.TestCase):
    TestCluster = SimpleCluster()
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_01_init(self):
        result, returncode = self.__class__.TestCluster.init()
        self.assertEqual(returncode, 0)
    def test_02_plan(self):
        result, returncode = self.__class__.TestCluster.plan()
        self.assertEqual(returncode, 0)
    def test_03_plan_destroy(self):
        result, returncode = self.__class__.TestCluster.plan_destroy()
        self.assertEqual(returncode, 0)
    #def test_04_apply(self):
    #    result, returncode = self.__class__.TestCluster.apply()
    #    self.assertEqual(returncode, 0)
    #def test_05_destroy(self):
    #    result, returncode = self.__class__.TestCluster.destroy()
    #    self.assertEqual(returncode, 0)

if __name__ == '__main__':
    unittest.main()