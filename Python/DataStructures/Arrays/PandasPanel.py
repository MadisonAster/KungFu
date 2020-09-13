#Standard Imports#################################
import sys, os, unittest
from importlib import machinery
import subprocess, shlex
from pprint import pprint
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Test#############################################
@KungFu.depends('numpy', 'pandas')
class test_PandasPanel(KungFu.TimedTest):
    def test_1(self):
        PandasPanel()
##################################################

#Code#############################################
import numpy as np
import pandas as pd
def PandasPanel():
    df1 = pd.DataFrame(
            np.arange(8).reshape(4,2),
            index=tuple('ABCD'),
            columns=tuple('xy'))
    df2 = pd.DataFrame(
            np.arange(8).reshape(4,2),
            index=tuple('ABCD'),
            columns=tuple('qz'))
    dfs = {'I': df1, 'II': df2}
    pprint(dfs)
    
    ##deprecated class now removed##
    #pn = pd.Panel(dfs)
    #print(pn)
    #print(pn.loc[:,'C'])
    #print(pn.loc[:,'C', 'x'])
    #print(pn.loc[:,'C'].mean(axis=1))
    
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
