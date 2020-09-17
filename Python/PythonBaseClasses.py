#Standard Imports#################################
import os, sys
from importlib import machinery
import traceback
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',2)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Test#############################################
#TODO
##################################################

#Code#############################################
#TODO
##################################################

#Relative Child Imports###########################
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
##################################################
