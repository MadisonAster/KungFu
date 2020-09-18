#Imports##########################################
import FooFinder
from FooFinder import KungFu
##################################################

#Test#############################################
#TODO
##################################################

#Code#############################################
import traceback
try:
    from FooFinder import SingletonApp
    globals()['SingletonApp'] = SingletonApp.SingletonApp
except:
    pass
    #print(traceback.format_exc())
try:
    from FooFinder import BasicWindow
    globals()['BasicWindow'] = BasicWindow.BasicWindow
except:
    pass
    #print(traceback.format_exc())
try:
    from FooFinder import BasicWidget
    globals()['BasicWidget'] = BasicWidget.BasicWidget
except:
    pass
    #print(traceback.format_exc())
try:
    from FooFinder import StaticFrameFromSymbol
    globals()['StaticFrame'] = StaticFrameFromSymbol.StaticFrame
    globals()['StaticFrameGO'] = StaticFrameFromSymbol.StaticFrameGO
except:
    pass
    #print(traceback.format_exc())
##################################################
