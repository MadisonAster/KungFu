#Standard Imports#################################
import sys, os, unittest
from importlib import machinery
import subprocess, shlex
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Test#############################################
@KungFu.depends('msgpack')
class test_MessagePack(unittest.TestCase):
    def test_1(self):
        pack = MessagePack([1,2,3])
        print('messagepack!', pack)
        #self.assertEqual(PrintTree(self.mock_path), ExpectedResult)
##################################################

#Code#############################################
import msgpack
def MessagePack(input):
    pack = msgpack.packb(input, use_bin_type=True)
    return pack
##################################################

#Main#############################################
if __name__ == '__main__':
    unittest.main()
##################################################