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
class test_PandasMultiIndex(KungFu.TimedTest):
    def test_1(self):
        PandasMultiIndex()
##################################################

#Code#############################################
import numpy as np
import pandas as pd
def PandasMultiIndex():
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
    
    mi1 = pd.MultiIndex.from_product((tuple('xy'), tuple('ABCD')))
    df3 = pd.DataFrame(np.arange(16).reshape(8,2), index=mi1, columns=tuple('AB'))
    #df3 = pd.DataFrame(np.arange(32).reshape(8,4), index=mi1, columns=tuple('ABCD'))
    df4 = pd.DataFrame(np.arange(64).reshape(8,8), index=mi1, columns=mi1)
    print(df3)
    print(df3.loc[pd.IndexSlice[:,'B']])
    print(df3.loc[pd.IndexSlice[:,'B'], 'B'])
    print(df4)
    print(df4.loc[
            pd.IndexSlice['y', ['A','D']],
            pd.IndexSlice[:, 'B']])
    
    #Iinconsistent axis specification!!
    print(df3.loc['II', 'B']) #This selects row row!
    print(df3.loc[:,'B']) #This selects row column!
    
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
