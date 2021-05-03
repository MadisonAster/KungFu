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
@KungFu.depends('pandas')
class test_Darts(KungFu.TimedTest):
    def test_Darts1(self):
        pass
        #game = Darts()
##################################################

#Code#############################################
import pandas
class Darts():
    def __init__(self):
        self.start_location = (0,0,0)
        self.start_rotation = (0,0,0)
        self.initial_velocity = (0,0,0)
        self.initial_rvelocity = (0,0,0)
        self.drag_coefficient = 0
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################