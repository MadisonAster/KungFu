#Standard Imports#################################
import sys, os, unittest
from importlib import machinery
from datetime import datetime
import functools
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Test#############################################
class test_PartialExample(KungFu.TimedTest):
    def test_1(self):
        self.assertEqual(DividePartial(8), 4)
##################################################

#Inheritance Check################################
##################################################

#Code#############################################
def PartialExample(y, d = 1):
    return y/d
DividePartial = functools.partial(PartialExample,d=2)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
