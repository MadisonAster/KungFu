#Imports##########################################
import FooFinder
from FooFinder import KungFu
from FooFinder import PythonBaseClasses
##################################################

#Test#############################################
@KungFu.depends('lxml', 'pandas', 'static-frame', 'yfinance')
@KungFu.depends('msgpack', 'msgpack_numpy')
class test_MessagePack(KungFu.TimedTest):
    def test_1(self):
        frame = PythonBaseClasses.StaticFrame.from_symbol('GLD', period='5d', interval='1d')
        '''
        data = frame.to_msgpack()
        frame2 = static_frame.Frame.from_msgpack(data)
        self.assertEqual(frame, frame2)
        '''
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
    KungFu.main(__file__)
##################################################
