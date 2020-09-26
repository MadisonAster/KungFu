#Imports##########################################
from FooFinder import KungFu
from FooFinder import StaticFrameFromSymbol
##################################################

#Test#############################################
@KungFu.depends('lxml', 'pandas', 'static-frame', 'yfinance')
class test_implied_volatility(KungFu.TimedTest):
    #Currencies
    def test_GLD(self):
        frame = StaticFrame.from_symbol('GLD', period='5d', interval='1d')
        StaticFrame.implied_volatility()
##################################################

#Code#############################################
import static_frame as sf
import yfinance as yf
class StaticFrame(StaticFrameFromSymbol.StaticFrame):
    @classmethod
    def implied_volatility(cls):
        print('implied_volatility')
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
