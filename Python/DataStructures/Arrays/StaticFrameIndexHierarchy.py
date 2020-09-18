#Imports##########################################
from FooFinder import KungFu
from FooFinder import PythonBaseClasses
##################################################

#Test#############################################
@KungFu.depends('lxml', 'numpy', 'pandas', 'static-frame', 'yfinance')
#@KungFu.depends('hypothesis', 'xlsxwriter', 'openpyxl', 'xarray', 'tables', 'pyarrow')
class test_StaticFrameIndexHierarchy(KungFu.TimedTest):
    #class test_StaticFrameGO(KungFu.TimedTest):
    def test_GOLD(self):
        import numpy
        start = datetime.today() - timedelta(days=10)
        end = datetime.today() - timedelta(days=3)
        frame = StaticFrameIndexHierarchy.from_symbol('GC=F', start=start, end=end)
##################################################

#Code#############################################
from datetime import datetime, timedelta, date
import numpy as np
import static_frame as sf
import yfinance as yf
class StaticFrameIndexHierarchy(sf.IndexHierarchy):
    @classmethod
    def from_symbol(cls, Symbol, start=None, end=None, interval='1d', period=None, silent=True):
        #self.ticker = yf.Ticker(Symbol)
        '''
        data = cls.from_pandas(yf.download(
            tickers = Symbol,
            #datetime objects
            start = start,
            end = end,
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            interval = interval,
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            period = period, #if not using start/end
            group_by = 'ticker',
            auto_adjust = True,
            prepost = True,
            threads = True,
            proxy = None
        ))
        '''
        ih1 = sf.IndexHierarchy.from_product(tuple('ABCD'), tuple('1234'))
        ih2 = sf.IndexHierarchy.from_product(tuple('EFGH'), tuple('5678'))
        f1 = sf.Frame(np.arange(256).reshape(16, 16), index=ih1, columns=ih2)
        print(f1)
        print('@@@@@@')
        return
        #print(f1.loc['x', 'B']) #KeyError! try Hloc!
        print(f1.loc[sf.HLoc['x','B']])
        print(f1.loc[sf.HLoc[:, ['B','D']]])
        print('ih1', type(ih1))
        print('ih1', dir(ih1))
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
