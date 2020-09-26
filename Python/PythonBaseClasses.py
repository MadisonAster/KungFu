#Imports##########################################
from FooFinder import KungFu
##################################################

#Test#############################################
#TODO
##################################################

#Code#############################################
import traceback
try:
    print('StaticFrameFromSymbol!')
    from FooFinder import StaticFrameFromSymbol
    globals()['StaticFrame'] = StaticFrameFromSymbol.StaticFrame
except:
    pass
    #print(traceback.format_exc())
##################################################
