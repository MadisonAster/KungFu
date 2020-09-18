#Imports##########################################
import os, sys
from importlib import machinery
import traceback

import FooFinder
from FooFinder import KungFu
##################################################

#Test#############################################
#TODO
##################################################

#Code#############################################
#TODO
##################################################

#Relative Child Imports###########################
try:
    from FooFinder import SingletonApp
    globals()['SingletonApp'] = SingletonApp.SingletonApp
except:
    pass
try:
    from FooFinder import BasicWindow
    globals()['BasicWindow'] = BasicWindow.BasicWindow
except:
    pass
try:
    from FooFinder import BasicWidget
    globals()['BasicWidget'] = BasicWidget.BasicWidget
except:
    pass
try:
    from FooFinder import StaticFrameFromSymbol
    globals()['StaticFrame'] = StaticFrameFromSymbol.StaticFrame
    globals()['StaticFrameGO'] = StaticFrameFromSymbol.StaticFrameGO
except:
    pass

'''
try:
    if 'SingletonApp' not in sys.modules.keys(): #Relative import handling for base classes
        machinery.SourceFileLoader('SingletonApp', os.path.dirname(os.path.abspath(__file__))+'/Qt/Windows/SingletonApp.py').load_module()
    from SingletonApp import SingletonApp
except:
    print(traceback.format_exc())

try:
    if 'BasicWindow' not in sys.modules.keys(): #Relative import handling for base classes
        machinery.SourceFileLoader('BasicWindow', os.path.dirname(os.path.abspath(__file__))+'/Qt/Windows/BasicWindow.py').load_module()
    from BasicWindow import BasicWindow
except:
    print(traceback.format_exc())
    
try:
    if 'BasicWidget' not in sys.modules.keys(): #Relative import handling for base classes
        machinery.SourceFileLoader('BasicWidget', os.path.dirname(os.path.abspath(__file__))+'/Qt/Widgets/BasicWidget.py').load_module()
    from BasicWidget import BasicWidget
except:
    print(traceback.format_exc())

try:
    if 'StaticFrameFromSymbol' not in sys.modules.keys(): #Relative import handling for base classes
        machinery.SourceFileLoader('StaticFrameFromSymbol', os.path.dirname(os.path.abspath(__file__))+'/Datastructures/Arrays/StaticFrameFromSymbol.py').load_module()
    from StaticFrameFromSymbol import StaticFrame, StaticFrameGO
except:
    print(traceback.format_exc())
'''
##################################################
