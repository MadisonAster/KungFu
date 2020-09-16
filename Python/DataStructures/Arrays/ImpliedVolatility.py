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
@KungFu.depends('lxml', 'pandas', 'static-frame', 'yfinance')
class test_implied_volatility(KungFu.TimedTest):
    #Currencies
    def test_GLD(self):
        frame = StaticFrame.from_symbol('GLD', period='5d', interval='1d')
        StaticFrame.implied_volatility()
##################################################

#Code#############################################
import static_frame as sf
import yfinance as yf
class StaticFrame(PythonBaseClasses.StaticFrame):
    @classmethod
    def implied_volatility(cls):
        print('implied_volatility')
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
