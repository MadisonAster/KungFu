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
@KungFu.depends('lxml', 'pandas', 'static_frame', 'yfinance')
class test_implied_volatility(KungFu.TimedTest):
    #Currencies
    def test_GLD(self):
        frame = static_frame.from_symbol('GLD')
        static_frame.implied_volatility()
    def test_GOLD(self):
        frame = static_frame.from_symbol('GC=F')
        static_frame.implied_volatility()
    def test_SLV(self):
        frame = static_frame.from_symbol('SLV')
        static_frame.implied_volatility()
    def test_SILVER(self):
        frame = static_frame.from_symbol('SI=F')
        static_frame.implied_volatility()
    def test_BTCUSD(self):
        frame = static_frame.from_symbol('BTC=X')
        static_frame.implied_volatility()
    def test_USDEUR(self):
        frame = static_frame.from_symbol('EUR=X')
        static_frame.implied_volatility()
    def test_USDGBP(self):
        frame = static_frame.from_symbol('GBP=X')
        static_frame.implied_volatility()
    def test_USDCAD(self):
        frame = static_frame.from_symbol('CAD=X')
        static_frame.implied_volatility()
    def test_USDJPY(self):
        frame = static_frame.from_symbol('JPY=X')
        static_frame.implied_volatility()
    def test_USDCNY(self):
        frame = static_frame.from_symbol('CNY=X')
        static_frame.implied_volatility()

    #Indexes 
    def test_DJI(self):
        frame = static_frame.from_symbol('^DJI')
        static_frame.implied_volatility()
    def test_NDAQ(self):
        frame = static_frame.from_symbol('NDAQ')
        static_frame.implied_volatility()
    def test_SPX(self):
        frame = static_frame.from_symbol('^GSPC')
        static_frame.implied_volatility()
    
    #ETFs
    def test_VYM(self):
        frame = static_frame.from_symbol('VYM')
        static_frame.implied_volatility()
    def test_VOO(self):
        frame = static_frame.from_symbol('VOO')
        static_frame.implied_volatility()
    def test_MGK(self):
        frame = static_frame.from_symbol('MGK')
        static_frame.implied_volatility()
    def test_MFEM(self):
        frame = static_frame.from_symbol('MFEM')
        static_frame.implied_volatility()
    def test_MFUS(self):
        frame = static_frame.from_symbol('MFUS')
        static_frame.implied_volatility()
    def test_MFDX(self):
        frame = static_frame.from_symbol('MFDX')
        static_frame.implied_volatility()
    
    #Tech
    def test_FB(self):
        frame = static_frame.from_symbol('FB')
        static_frame.implied_volatility()
    def test_AAPL(self):
        frame = static_frame.from_symbol('AAPL')
        static_frame.implied_volatility()
    def test_AMZN(self):
        frame = static_frame.from_symbol('AMZN')
        static_frame.implied_volatility()
    def test_NFLX(self):
        frame = static_frame.from_symbol('NFLX')
        static_frame.implied_volatility()
    def test_GOOG(self):
        frame = static_frame.from_symbol('GOOG')
        static_frame.implied_volatility()
    def test_TSLA(self):
        frame = static_frame.from_symbol('TSLA')
        static_frame.implied_volatility()
    def test_NVDA(self):
        frame = static_frame.from_symbol('NVDA')
        static_frame.implied_volatility()
    def test_INTC(self):
        frame = static_frame.from_symbol('INTC')
        static_frame.implied_volatility()
    def test_MSFT(self):
        frame = static_frame.from_symbol('MSFT')
        static_frame.implied_volatility()

    #Retail
    def test_KR(self):
        frame = static_frame.from_symbol('KR')
        static_frame.implied_volatility()
    def test_MCD(self):
        frame = static_frame.from_symbol('MCD')
        static_frame.implied_volatility()
    def test_WMT(self):
        frame = static_frame.from_symbol('WMT')
        static_frame.implied_volatility()
    #def test_TGT(self):
    #    frame = static_frame.from_symbol('TGT')
    #    static_frame.implied_volatility()
    
    #War
    def test_USOIL(self):
        frame = static_frame.from_symbol('CL=F')
        static_frame.implied_volatility()
    def test_RTX(self):
        frame = static_frame.from_symbol('RTX')
        static_frame.implied_volatility()
    def test_AAXN(self):
        frame = static_frame.from_symbol('AAXN')
        static_frame.implied_volatility()
    def test_CXW(self):
        frame = static_frame.from_symbol('CXW')
        static_frame.implied_volatility()
    #def test_SWBI(self):
    #    frame = static_frame.from_symbol('SWBI')
    #    static_frame.implied_volatility()
    def test_RGR(self):
        frame = static_frame.from_symbol('RGR')
        static_frame.implied_volatility()
##################################################

#Code#############################################
import static_frame as sf
import yfinance as yf
class static_frame(PythonBaseClasses.static_frame):
    @classmethod
    def implied_volatility(cls):
        print('implied_volatility')
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
