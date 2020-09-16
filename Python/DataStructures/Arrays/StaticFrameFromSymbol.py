#Standard Imports#################################
import sys, os, unittest
from importlib import machinery
import subprocess, shlex
from datetime import datetime, timedelta, date
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Test#############################################
@KungFu.depends('lxml', 'numpy', 'pandas', 'static-frame', 'yfinance')
#@KungFu.depends('hypothesis', 'xlsxwriter', 'openpyxl', 'xarray', 'tables', 'pyarrow')
class test_StaticFrame(KungFu.TimedTest):
    #Currencies
    def test_GLD(self):
        frame = StaticFrame.from_symbol('GLD', period='5d', interval='1d')
    '''
    def test_GOLD(self):
        frame = StaticFrame.from_symbol('GC=F')
    def test_SLV(self):
        frame = StaticFrame.from_symbol('SLV')
    def test_SILVER(self):
        frame = StaticFrame.from_symbol('SI=F')
    def test_BTCUSD(self):
        frame = StaticFrame.from_symbol('BTC=X')
    def test_USDEUR(self):
        frame = StaticFrame.from_symbol('EUR=X')
    def test_USDGBP(self):
        frame = StaticFrame.from_symbol('GBP=X')
    def test_USDCAD(self):
        frame = StaticFrame.from_symbol('CAD=X')
    def test_USDJPY(self):
        frame = StaticFrame.from_symbol('JPY=X')
    def test_USDCNY(self):
        frame = StaticFrame.from_symbol('CNY=X')

    #Indexes 
    def test_DJI(self):
        frame = StaticFrame.from_symbol('^DJI')
    def test_NDAQ(self):
        frame = StaticFrame.from_symbol('NDAQ')
    def test_SPX(self):
        frame = StaticFrame.from_symbol('^GSPC')
    
    #ETFs
    def test_VYM(self):
        frame = StaticFrame.from_symbol('VYM')
    def test_VOO(self):
        frame = StaticFrame.from_symbol('VOO')
    def test_MGK(self):
        frame = StaticFrame.from_symbol('MGK')
    def test_MFEM(self):
        frame = StaticFrame.from_symbol('MFEM')
    def test_MFUS(self):
        frame = StaticFrame.from_symbol('MFUS')
    def test_MFDX(self):
        frame = StaticFrame.from_symbol('MFDX')
    
    #Tech
    def test_FB(self):
        frame = StaticFrame.from_symbol('FB')
    def test_AAPL(self):
        frame = StaticFrame.from_symbol('AAPL')
    def test_AMZN(self):
        frame = StaticFrame.from_symbol('AMZN')
    def test_NFLX(self):
        frame = StaticFrame.from_symbol('NFLX')
    def test_GOOG(self):
        frame = StaticFrame.from_symbol('GOOG')
    def test_TSLA(self):
        frame = StaticFrame.from_symbol('TSLA')
    def test_NVDA(self):
        frame = StaticFrame.from_symbol('NVDA')
    def test_INTC(self):
        frame = StaticFrame.from_symbol('INTC')
    def test_MSFT(self):
        frame = StaticFrame.from_symbol('MSFT')

    #Retail
    def test_KR(self):
        frame = StaticFrame.from_symbol('KR')
    def test_MCD(self):
        frame = StaticFrame.from_symbol('MCD')
    def test_WMT(self):
        frame = StaticFrame.from_symbol('WMT')
    #def test_TGT(self):
    #    frame = StaticFrame.from_symbol('TGT')
    
    #War
    def test_USOIL(self):
        frame = StaticFrame.from_symbol('CL=F')
    def test_RTX(self):
        frame = StaticFrame.from_symbol('RTX')
    def test_AAXN(self):
        frame = StaticFrame.from_symbol('AAXN')
    def test_CXW(self):
        frame = StaticFrame.from_symbol('CXW')
    #def test_SWBI(self):
    #    frame = StaticFrame.from_symbol('SWBI')
    def test_RGR(self):
        frame = StaticFrame.from_symbol('RGR')
    '''
    
    #class test_StaticFrameGO(KungFu.TimedTest):
    def test_GOLD(self):
        import numpy
        start = datetime.today() - timedelta(days=10)
        end = datetime.today() - timedelta(days=3)
        frame = StaticFrame.from_symbol('GC=F', start=start, end=end)
        print('frame1', frame)
        frame2 = frame.update_symbol()
        print('frame2', frame2)
        print('len', len(frame.index))
        print('len', len(frame2.index))
        print('busday_count', numpy.busday_count(start.date()+timedelta(days=1), date.today()))
        
    def test_close(self):
        start = datetime.now() - timedelta(days=30)
        end = datetime.now() - timedelta(days=5)
        frame = StaticFrame.from_symbol('GC=F', start=start, end=end)
        print('close1', frame.get_close())
        '''
        s = datetime.now() - timedelta(days=10)
        print('s', s, type(s))
        print('close11', frame.get_close(end=datetime.now()))
        print('close2', frame.get_close(start=s))
        close = frame.get_close(start=datetime.now() - timedelta(days=20))
        print('close3', close)
        '''
    
##################################################

#Code#############################################
import static_frame as sf
import yfinance as yf
class StaticFrame(sf.Frame):
    @classmethod
    def from_symbol(cls, Symbol, start=None, end=None, interval='1d', period=None, silent=True):
        #self.ticker = yf.Ticker(Symbol)
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
        data = data.rename(Symbol)
        data.Symbol = Symbol
        data.interval = interval
        if end:
            data.end = end
        if not silent:
            print(data)
        return data
    
    def get_close(self, start=None, end=None):
        if not start and not end:
            return self.loc[:, 'Close']
        elif start and end:
            #return self.loc[start:end, 'Close']
            return self.loc[(self.index > start) & (self.index < end), 'Close']
        elif start:
            return self.loc[(self.index > start), 'Close']
            #return self.loc[start:, 'Close']
        elif end:
            #return self.loc[(self.index.values < end), 'Close']
            return self.loc[:end, 'Close']
    
    def update_symbol(self, silent=True):
        end = datetime.now()
        newdata = yf.download(
            tickers = self.name,
            start = self.end,
            end = end,
            interval = self.interval,
            group_by = 'ticker',
            auto_adjust = True,
            prepost = True,
            threads = True,
            proxy = None
        )
        self.end = end
        if not silent:
            print(newdata)
        return self.__class__.from_pandas(self.to_pandas().append(newdata))

class StaticFrameGO(StaticFrame):
    pass
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
