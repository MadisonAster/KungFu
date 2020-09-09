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
@KungFu.depends('static_frame', 'yfinance')
class test_StaticFrameFromSymbol(KungFu.TimedTest):
    #Currencies
    def test_GLD(self):
        frame = StaticFrameFromSymbol('GLD')
    def test_GOLD(self):
        frame = StaticFrameFromSymbol('GOLD')
    def test_SLV(self):
        frame = StaticFrameFromSymbol('SLV')
    def test_SILVER(self):
        frame = StaticFrameFromSymbol('SILVER')
    def test_BTCUSD(self):
        frame = StaticFrameFromSymbol('BTCUSD')
    def test_EURUSD(self):
        frame = StaticFrameFromSymbol('EURUSD')
    def test_USDGBP(self):
        frame = StaticFrameFromSymbol('USDGBP')
    def test_USDCAD(self):
        frame = StaticFrameFromSymbol('USDCAD')
    def test_USDJPY(self):
        frame = StaticFrameFromSymbol('USDJPY')
    def test_USDCNY(self):
        frame = StaticFrameFromSymbol('USDCNY')

    #Indexes 
    def test_DJI(self):
        frame = StaticFrameFromSymbol('DJI')
    def test_NDAQ(self):
        frame = StaticFrameFromSymbol('NDAQ')
    def test_SPX(self):
        frame = StaticFrameFromSymbol('SPX')

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
    def test_TGT(self):
        frame = StaticFrameFromSymbol('TGT')

    #War
    def test_USOIL(self):
        frame = StaticFrameFromSymbol('USOIL')
    def test_RTX(self):
        frame = StaticFrameFromSymbol('RTX')
    def test_AAXN(self):
        frame = StaticFrameFromSymbol('AAXN')
    def test_CXW(self):
        frame = StaticFrameFromSymbol('CXW')

    
##################################################

#Code#############################################
import static_frame as sf
import yfinance as yf
class StaticFrameFromSymbol():
    def __init__(self, Symbol):
        pass
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################