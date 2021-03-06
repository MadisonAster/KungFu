#Imports##########################################
from FooFinder import KungFu
##################################################

#Test#############################################
@KungFu.depends('pandas')
class test_PandasMult(KungFu.TimedTest):
    def test_1(self):
        PandasMult('a', 'b')

    def test_2(self):
        PandasMult('a', 'c')

    def test_3(self):
        PandasMult('b', 'c')
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
    KungFu.main(__file__)
##################################################
