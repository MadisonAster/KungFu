import unittest
from datetime import datetime

import subprocess
import shlex


class SimpleCluster():
    def __init__(self):
        super(SimpleCluster, self).__init__()
        run_command('terraform init')
        run_command('terraform plan -out=KungFu.plan')
        #run_command('terraform plan -target=SimpleCluster.tf')
        

def run_command(CommandString):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('run_command', CommandString)
    result = u""
    proc = subprocess.Popen(shlex.split(CommandString), stdout=subprocess.PIPE)
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
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        TestCluster = SimpleCluster()

if __name__ == '__main__':
    unittest.main()