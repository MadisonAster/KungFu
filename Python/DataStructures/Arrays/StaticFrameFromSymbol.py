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
class test_StaticFrameFromSymbol(KungFu.TimedTest):
    #Currencies
    def test_GLD(self):
        frame = StaticFrameFromSymbol('GLD')
    
    def test_GOLD(self):
        frame = StaticFrameFromSymbol('GC=F')
    
    def test_SLV(self):
        frame = StaticFrameFromSymbol('SLV')
    def test_SILVER(self):
        frame = StaticFrameFromSymbol('SI=F')
    
    def test_BTCUSD(self):
        frame = StaticFrameFromSymbol('BTC=X')
    def test_USDEUR(self):
        frame = StaticFrameFromSymbol('EUR=X')
    def test_USDGBP(self):
        frame = StaticFrameFromSymbol('GBP=X')
    def test_USDCAD(self):
        frame = StaticFrameFromSymbol('CAD=X')
    def test_USDJPY(self):
        frame = StaticFrameFromSymbol('JPY=X')
    def test_USDCNY(self):
        frame = StaticFrameFromSymbol('CNY=X')

    #Indexes 
    def test_DJI(self):
        frame = StaticFrameFromSymbol('^DJI')
    def test_NDAQ(self):
        frame = StaticFrameFromSymbol('NDAQ')
    def test_SPX(self):
        frame = StaticFrameFromSymbol('^GSPC')
    
    #ETFs
    def test_VYM(self):
        frame = StaticFrameFromSymbol('VYM')
    def test_VOO(self):
        frame = StaticFrameFromSymbol('VOO')
    def test_MGK(self):
        frame = StaticFrameFromSymbol('MGK')
    def test_MFEM(self):
        frame = StaticFrameFromSymbol('MFEM')
    def test_MFUS(self):
        frame = StaticFrameFromSymbol('MFUS')
    def test_MFDX(self):
        frame = StaticFrameFromSymbol('MFDX')
    
    #Tech
    def test_FB(self):
        frame = StaticFrameFromSymbol('FB')
    def test_AAPL(self):
        frame = StaticFrameFromSymbol('AAPL')
    def test_AMZN(self):
        frame = StaticFrameFromSymbol('AMZN')
    def test_NFLX(self):
        frame = StaticFrameFromSymbol('NFLX')
    def test_GOOG(self):
        frame = StaticFrameFromSymbol('GOOG')
    def test_TSLA(self):
        frame = StaticFrameFromSymbol('TSLA')
    def test_NVDA(self):
        frame = StaticFrameFromSymbol('NVDA')
    def test_INTC(self):
        frame = StaticFrameFromSymbol('INTC')
    def test_MSFT(self):
        frame = StaticFrameFromSymbol('MSFT')

    #Retail
    def test_KR(self):
        frame = StaticFrameFromSymbol('KR')
    def test_MCD(self):
        frame = StaticFrameFromSymbol('MCD')
    def test_WMT(self):
        frame = StaticFrameFromSymbol('WMT')
    #def test_TGT(self):
    #    frame = StaticFrameFromSymbol('TGT')
    
    #War
    def test_USOIL(self):
        frame = StaticFrameFromSymbol('CL=F')
    def test_RTX(self):
        frame = StaticFrameFromSymbol('RTX')
    def test_AAXN(self):
        frame = StaticFrameFromSymbol('AAXN')
    def test_CXW(self):
        frame = StaticFrameFromSymbol('CXW')
    #def test_SWBI(self):
    #    frame = StaticFrameFromSymbol('SWBI')
    def test_RGR(self):
        frame = StaticFrameFromSymbol('RGR')
##################################################

#Code#############################################
import static_frame as sf
import yfinance as yf
class StaticFrameFromSymbol():
    def __init__(self, Symbol, period='ytd', interval='1d'):
        ticker = yf.Ticker(Symbol)
        data = sf.Frame.from_pandas(yf.download(
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
        print(type(data))
        print(data)
        return data
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################