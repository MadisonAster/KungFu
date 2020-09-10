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
@KungFu.depends('msgpack', 'msgpack_numpy')
class test_MessagePack(unittest.TestCase):
    def test_1(self):
        frame = PythonBaseClasses.static_frame.from_symbol('GLD')
        
        '''
        print('~~~~prototype~~~~')
        proto = {
            'index' : [index for index in frame._index],
            'columns' : [column for column in frame._columns],
            'name' : frame._name,
            'blocks' : [[value[0] for value in block.values] for block in frame._blocks],
        }
        print('index', type(proto['index'][0]))
        print('columns', proto['columns'])
        print('name', proto['name'])
        print('blocks', len(proto['blocks']))
        for block in proto['blocks']:
            print('    block', type(block[0]))
        '''
        
        #print('~~~~datatype~~~~')
        data = {
            '_index' : MessagePack(index for index in frame._index),
            '_columns' : MessagePack(column for column in frame._columns),
            '_name' : MessagePack(frame._name),
            '_blocks' : [MessagePack(value[0] for value in block.values) for block in frame._blocks],
        }
        print('index', data['_index'][:40], '...')
        print('columns', data['_columns'])
        print('name', data['_name'])
        print('blocks', len(data['_blocks']))
        for block in data['_blocks']:
            print('    block', block[:20], '...')
        
        #self.assertEqual(data, ExpectedResult)
##################################################

#Code#############################################
import msgpack
import msgpack_numpy
def MessagePack(input):
    try:
        data = msgpack.packb(input, use_bin_type=True)
    except:
        try:
            data = msgpack.packb(input, default=msgpack_numpy.encode)
        except:
            data = msgpack.packb([a.__str__() for a in input], use_bin_type=True)
    return data
    #input_rec = msgpack.unpackb(input_enc, object_hook=m.decode)
##################################################

#Main#############################################
if __name__ == '__main__':
    unittest.main()
##################################################
