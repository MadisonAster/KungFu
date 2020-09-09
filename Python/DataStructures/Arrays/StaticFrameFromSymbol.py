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
@KungFu.depends('lxml', 'pandas', 'static_frame', 'yfinance')
#@KungFu.depends('hypothesis', 'xlsxwriter', 'openpyxl', 'xarray', 'tables', 'pyarrow')
class test_static_frame(KungFu.TimedTest):
    #Currencies
    def test_GLD(self):
        frame = static_frame.from_symbol('GLD')
    def test_GOLD(self):
        frame = static_frame.from_symbol('GC=F')
    def test_SLV(self):
        frame = static_frame.from_symbol('SLV')
    def test_SILVER(self):
        frame = static_frame.from_symbol('SI=F')
    def test_BTCUSD(self):
        frame = static_frame.from_symbol('BTC=X')
    def test_USDEUR(self):
        frame = static_frame.from_symbol('EUR=X')
    def test_USDGBP(self):
        frame = static_frame.from_symbol('GBP=X')
    def test_USDCAD(self):
        frame = static_frame.from_symbol('CAD=X')
    def test_USDJPY(self):
        frame = static_frame.from_symbol('JPY=X')
    def test_USDCNY(self):
        frame = static_frame.from_symbol('CNY=X')

    #Indexes 
    def test_DJI(self):
        frame = static_frame.from_symbol('^DJI')
    def test_NDAQ(self):
        frame = static_frame.from_symbol('NDAQ')
    def test_SPX(self):
        frame = static_frame.from_symbol('^GSPC')
    
    #ETFs
    def test_VYM(self):
        frame = static_frame.from_symbol('VYM')
    def test_VOO(self):
        frame = static_frame.from_symbol('VOO')
    def test_MGK(self):
        frame = static_frame.from_symbol('MGK')
    def test_MFEM(self):
        frame = static_frame.from_symbol('MFEM')
    def test_MFUS(self):
        frame = static_frame.from_symbol('MFUS')
    def test_MFDX(self):
        frame = static_frame.from_symbol('MFDX')
    
    #Tech
    def test_FB(self):
        frame = static_frame.from_symbol('FB')
    def test_AAPL(self):
        frame = static_frame.from_symbol('AAPL')
    def test_AMZN(self):
        frame = static_frame.from_symbol('AMZN')
    def test_NFLX(self):
        frame = static_frame.from_symbol('NFLX')
    def test_GOOG(self):
        frame = static_frame.from_symbol('GOOG')
    def test_TSLA(self):
        frame = static_frame.from_symbol('TSLA')
    def test_NVDA(self):
        frame = static_frame.from_symbol('NVDA')
    def test_INTC(self):
        frame = static_frame.from_symbol('INTC')
    def test_MSFT(self):
        frame = static_frame.from_symbol('MSFT')

    #Retail
    def test_KR(self):
        frame = static_frame.from_symbol('KR')
    def test_MCD(self):
        frame = static_frame.from_symbol('MCD')
    def test_WMT(self):
        frame = static_frame.from_symbol('WMT')
    #def test_TGT(self):
    #    frame = static_frame.from_symbol('TGT')
    
    #War
    def test_USOIL(self):
        frame = static_frame.from_symbol('CL=F')
    def test_RTX(self):
        frame = static_frame.from_symbol('RTX')
    def test_AAXN(self):
        frame = static_frame.from_symbol('AAXN')
    def test_CXW(self):
        frame = static_frame.from_symbol('CXW')
    #def test_SWBI(self):
    #    frame = static_frame.from_symbol('SWBI')
    def test_RGR(self):
        frame = static_frame.from_symbol('RGR')
##################################################

#Code#############################################
import static_frame as sf
import yfinance as yf
class static_frame(sf.Frame):
    @classmethod
    def from_symbol(cls, Symbol, period='ytd', interval='1d', silent=False):
        ticker = yf.Ticker(Symbol)
        data = cls.from_pandas(yf.download(
            tickers = Symbol,
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            period = period,
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            interval = interval,
            group_by = 'ticker',
            auto_adjust = True,
            prepost = True,
            threads = True,
            proxy = None
        ))
        if not silent:
            print(data)
        return data
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################