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
@KungFu.depends('static_frame')
class test_StaticFrameHello(KungFu.TimedTest):
    def test_1(self):
        myframe = StaticFrameHello()
##################################################

#Code#############################################
import static_frame as sf
class StaticFrameHello():
    def __init__(self):
        pass
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################