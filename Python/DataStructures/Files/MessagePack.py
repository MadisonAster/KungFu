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

#Relative Imports#################################
if 'PythonBaseClasses' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['PythonBaseClasses'] = machinery.SourceFileLoader('PythonBaseClasses', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',2)[0]+'/PythonBaseClasses.py').load_module()
import PythonBaseClasses
#Code#############################################

#Test#############################################
@KungFu.depends('lxml', 'pandas', 'static_frame', 'yfinance')
@KungFu.depends('msgpack')
class test_MessagePack(unittest.TestCase):
    def test_1(self):
        frame = PythonBaseClasses.static_frame.from_symbol('GLD')
        data = [1,2,3]
        print('_index', frame._index)
        print('_columns', frame._columns)
        print('_name', frame._name)
        print('_blocks', frame._blocks)
        #for array in frame._blocks.axis_values(0):
        #    data.append(list(array))
        #print(type(data), type(data[0]))
        pack = MessagePack(data)
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
