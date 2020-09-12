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
        frame = StaticFrame.from_symbol('GLD')
        StaticFrame.implied_volatility()
    def test_GOLD(self):
        frame = StaticFrame.from_symbol('GC=F')
        StaticFrame.implied_volatility()
    def test_SLV(self):
        frame = StaticFrame.from_symbol('SLV')
        StaticFrame.implied_volatility()
    def test_SILVER(self):
        frame = StaticFrame.from_symbol('SI=F')
        StaticFrame.implied_volatility()
    def test_BTCUSD(self):
        frame = StaticFrame.from_symbol('BTC=X')
        StaticFrame.implied_volatility()
    def test_USDEUR(self):
        frame = StaticFrame.from_symbol('EUR=X')
        StaticFrame.implied_volatility()
    def test_USDGBP(self):
        frame = StaticFrame.from_symbol('GBP=X')
        StaticFrame.implied_volatility()
    def test_USDCAD(self):
        frame = StaticFrame.from_symbol('CAD=X')
        StaticFrame.implied_volatility()
    def test_USDJPY(self):
        frame = StaticFrame.from_symbol('JPY=X')
        StaticFrame.implied_volatility()
    def test_USDCNY(self):
        frame = StaticFrame.from_symbol('CNY=X')
        StaticFrame.implied_volatility()

    #Indexes 
    def test_DJI(self):
        frame = StaticFrame.from_symbol('^DJI')
        StaticFrame.implied_volatility()
    def test_NDAQ(self):
        frame = StaticFrame.from_symbol('NDAQ')
        StaticFrame.implied_volatility()
    def test_SPX(self):
        frame = StaticFrame.from_symbol('^GSPC')
        StaticFrame.implied_volatility()
    
    #ETFs
    def test_VYM(self):
        frame = StaticFrame.from_symbol('VYM')
        StaticFrame.implied_volatility()
    def test_VOO(self):
        frame = StaticFrame.from_symbol('VOO')
        StaticFrame.implied_volatility()
    def test_MGK(self):
        frame = StaticFrame.from_symbol('MGK')
        StaticFrame.implied_volatility()
    def test_MFEM(self):
        frame = StaticFrame.from_symbol('MFEM')
        StaticFrame.implied_volatility()
    def test_MFUS(self):
        frame = StaticFrame.from_symbol('MFUS')
        StaticFrame.implied_volatility()
    def test_MFDX(self):
        frame = StaticFrame.from_symbol('MFDX')
        StaticFrame.implied_volatility()
    
    #Tech
    def test_FB(self):
        frame = StaticFrame.from_symbol('FB')
        StaticFrame.implied_volatility()
    def test_AAPL(self):
        frame = StaticFrame.from_symbol('AAPL')
        StaticFrame.implied_volatility()
    def test_AMZN(self):
        frame = StaticFrame.from_symbol('AMZN')
        StaticFrame.implied_volatility()
    def test_NFLX(self):
        frame = StaticFrame.from_symbol('NFLX')
        StaticFrame.implied_volatility()
    def test_GOOG(self):
        frame = StaticFrame.from_symbol('GOOG')
        StaticFrame.implied_volatility()
    def test_TSLA(self):
        frame = StaticFrame.from_symbol('TSLA')
        StaticFrame.implied_volatility()
    def test_NVDA(self):
        frame = StaticFrame.from_symbol('NVDA')
        StaticFrame.implied_volatility()
    def test_INTC(self):
        frame = StaticFrame.from_symbol('INTC')
        StaticFrame.implied_volatility()
    def test_MSFT(self):
        frame = StaticFrame.from_symbol('MSFT')
        StaticFrame.implied_volatility()

    #Retail
    def test_KR(self):
        frame = StaticFrame.from_symbol('KR')
        StaticFrame.implied_volatility()
    def test_MCD(self):
        frame = StaticFrame.from_symbol('MCD')
        StaticFrame.implied_volatility()
    def test_WMT(self):
        frame = StaticFrame.from_symbol('WMT')
        StaticFrame.implied_volatility()
    #def test_TGT(self):
    #    frame = StaticFrame.from_symbol('TGT')
    #    StaticFrame.implied_volatility()
    
    #War
    def test_USOIL(self):
        frame = StaticFrame.from_symbol('CL=F')
        StaticFrame.implied_volatility()
    def test_RTX(self):
        frame = StaticFrame.from_symbol('RTX')
        StaticFrame.implied_volatility()
    def test_AAXN(self):
        frame = StaticFrame.from_symbol('AAXN')
        StaticFrame.implied_volatility()
    def test_CXW(self):
        frame = StaticFrame.from_symbol('CXW')
        StaticFrame.implied_volatility()
    #def test_SWBI(self):
    #    frame = StaticFrame.from_symbol('SWBI')
    #    StaticFrame.implied_volatility()
    def test_RGR(self):
        frame = StaticFrame.from_symbol('RGR')
        StaticFrame.implied_volatility()
##################################################

#Code#############################################
import static_frame as sf
import yfinance as yf
class StaticFrame(PythonBaseClasses.StaticFrame):
    @classmethod
    def implied_volatility(cls):
        print('implied_volatility')
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
