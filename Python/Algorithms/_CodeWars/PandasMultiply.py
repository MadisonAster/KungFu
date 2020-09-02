#Standard Imports#################################
import sys, os, unittest, importlib
from datetime import datetime
import functools
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = importlib.machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Test#############################################
class test_PandasMult(KungFu.TimedTest):
    @KungFu.depends('pandas')
    def test_1(self):
        PandasMult('a', 'b')

    @KungFu.depends('pandas')
    def test_2(self):
        PandasMult('a', 'c')

    @KungFu.depends('pandas')
    def test_3(self):
        PandasMult('b', 'c')
##################################################

#Inheritance Check################################
if not KungFu.DependencyHandler().check('pandas'):
    raise Exception('return') #Module level return doesn't exist. This is a compelling use case. Maybe a PEP?
##################################################

#Code#############################################
import pandas
def PandasMult(left, right):
    a = pandas.Series((100, 1, 10, 65), dtype=object)
    b = pandas.Series((-85, -234, 32, 104), dtype=int)
    c = pandas.Series((205.3, 3.5, 234.3, 8403.32), dtype=float)
    df = pandas.DataFrame(dict(a=a, b=b, c=c))
    for _ in range(int(1e4)):
        df[left] * df[right]
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.LoadTestVars()
    unittest.main()
##################################################
