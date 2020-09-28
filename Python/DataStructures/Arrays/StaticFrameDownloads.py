#Imports##########################################
from FooFinder import KungFu
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
        frame = StaticFrame.from_symbol('GC=F', period='5d', interval='1d')
    def test_SLV(self):
        frame = StaticFrame.from_symbol('SLV', period='5d', interval='1d')
    def test_SILVER(self):
        frame = StaticFrame.from_symbol('SI=F', period='5d', interval='1d')
    def test_BTCUSD(self):
        frame = StaticFrame.from_symbol('BTC=X', period='5d', interval='1d')
    def test_USDEUR(self):
        frame = StaticFrame.from_symbol('EUR=X', period='5d', interval='1d')
    def test_USDGBP(self):
        frame = StaticFrame.from_symbol('GBP=X', period='5d', interval='1d')
    def test_USDCAD(self):
        frame = StaticFrame.from_symbol('CAD=X', period='5d', interval='1d')
    def test_USDJPY(self):
        frame = StaticFrame.from_symbol('JPY=X', period='5d', interval='1d')
    def test_USDCNY(self):
        frame = StaticFrame.from_symbol('CNY=X', period='5d', interval='1d')

    #Indexes 
    def test_DJI(self):
        frame = StaticFrame.from_symbol('^DJI', period='5d', interval='1d')
    def test_NDAQ(self):
        frame = StaticFrame.from_symbol('NDAQ', period='5d', interval='1d')
    def test_SPX(self):
        frame = StaticFrame.from_symbol('^GSPC', period='5d', interval='1d')
    
    #ETFs
    def test_VYM(self):
        frame = StaticFrame.from_symbol('VYM', period='5d', interval='1d')
    def test_VOO(self):
        frame = StaticFrame.from_symbol('VOO', period='5d', interval='1d')
    def test_MGK(self):
        frame = StaticFrame.from_symbol('MGK', period='5d', interval='1d')
    def test_MFEM(self):
        frame = StaticFrame.from_symbol('MFEM', period='5d', interval='1d')
    def test_MFUS(self):
        frame = StaticFrame.from_symbol('MFUS', period='5d', interval='1d')
    def test_MFDX(self):
        frame = StaticFrame.from_symbol('MFDX', period='5d', interval='1d')
    
    #Tech
    def test_FB(self):
        frame = StaticFrame.from_symbol('FB', period='5d', interval='1d')
    def test_AAPL(self):
        frame = StaticFrame.from_symbol('AAPL', period='5d', interval='1d')
    def test_AMZN(self):
        frame = StaticFrame.from_symbol('AMZN', period='5d', interval='1d')
    def test_NFLX(self):
        frame = StaticFrame.from_symbol('NFLX', period='5d', interval='1d')
    def test_GOOG(self):
        frame = StaticFrame.from_symbol('GOOG', period='5d', interval='1d')
    def test_TSLA(self):
        frame = StaticFrame.from_symbol('TSLA', period='5d', interval='1d')
    def test_NVDA(self):
        frame = StaticFrame.from_symbol('NVDA', period='5d', interval='1d')
    def test_INTC(self):
        frame = StaticFrame.from_symbol('INTC', period='5d', interval='1d')
    def test_MSFT(self):
        frame = StaticFrame.from_symbol('MSFT', period='5d', interval='1d')

    #Retail
    def test_KR(self):
        frame = StaticFrame.from_symbol('KR', period='5d', interval='1d')
    def test_MCD(self):
        frame = StaticFrame.from_symbol('MCD', period='5d', interval='1d')
    def test_WMT(self):
        frame = StaticFrame.from_symbol('WMT', period='5d', interval='1d')
    #def test_TGT(self):
    #    frame = StaticFrame.from_symbol('TGT', period='5d', interval='1d')
    
    #War
    def test_USOIL(self):
        frame = StaticFrame.from_symbol('CL=F', period='5d', interval='1d')
    def test_RTX(self):
        frame = StaticFrame.from_symbol('RTX', period='5d', interval='1d')
    def test_AAXN(self):
        frame = StaticFrame.from_symbol('AAXN', period='5d', interval='1d')
    def test_CXW(self):
        frame = StaticFrame.from_symbol('CXW', period='5d', interval='1d')
    #def test_SWBI(self):
    #    frame = StaticFrame.from_symbol('SWBI')
    def test_RGR(self):
        frame = StaticFrame.from_symbol('RGR', period='5d', interval='1d')
    '''
    
    def test_fred_d4oil(self):
        frame = StaticFrame.from_fred('SP500')
        print('d4oil', frame)
    
        #DAILY fredcode:
        'd4defl'             # synthetic deflator dataframe, see deflator()

        'JPY3MTD156N'        # 3-m LIBOR JPY, daily
        'EUR3MTD156N'        # 3-m LIBOR EUR, daily
        'USD3MTD156N'        # 3-m LIBOR USD, daily
        'DFF'                # Fed Funds, daily since 1954
        'd4ff30'             # Fed Funds synthetic, "30-day" exp.mov.avg.
        'DTB3'               # Treasury bills, daily
        'd4zero10'           # Zero-coupon price of Treasury 10-y, daily
        'DGS10'              # Treasury 10-y constant, daily
        'DFII10'             # TIPS 10-y constant, daily
        'd4curve'            # Treasury 10_y-bills, getfred synthetic
        'd4bei'              # 10_y Break-even inflation, getfred synthetic

        'DEXJPUS'            # USDJPY, daily
        'DEXUSEU'            # EURUSD, daily
        'd4eurjpy'           # EURJPY, daily, getfred synthetic
        'DEXCHUS'            # USDCNY, daily since 1981, not offshore USDCNH

        'GOLDPMGBD228NLBM'   # London PM Gold fix, daily

        'VIXCLS'             # CBOE volatility on S&P options, daily
        'SP500'              # S&P 500 index a.k.a. SPX, daily

        'DCOILBRENTEU'        # Oil Brent, DoE NSA daily
        'DCOILWTICO'          # Oil WTI,   DoE NSA daily
        'd4oil'               # Oil av. Brent and WTI, synthetic daily
        'd4gas'               # Reg. gasoline $/gal. w/ tax, synthetic daily

        #MONTHLY fredcode:
        'm4gdpus'    # U.S. GDP in billions, SA monthly synthetic
        'm4gdpusr'   # U.S. real GDP in current billions, SA monthly synthetic
        'HOUST'      # U.S. Housing Starts, SA monthly
        'm4homepx'   # Home price index Case-Shiller 20-city, SA monthly synthetic

        'AHETPI'     # Hourly earnings, all private nonfarm, SA monthly
                             #    production/nonsupervisory since 1964.
        'CES0500000003'  # Hourly earnings, all private nonfarm, SA monthly
        'UNRATE'     # Unemployment rate, SA monthly
        'EMRATIO'    # Civilian employment/population, percent SA monthly
        'POP'        # Total US population in thousands, NSA monthly
        'm4workers'  # Total US working population in thousands, NSA monthly
        'PAYEMS'     # US Nonfarm Payroll workers  in thousands,  SA monthly
        'm4debt'     # U.S. Federal debt in millions, NSA monthly synthetic

        'm4defl'     # synthetic deflator, see getdeflator().
        'CPIAUCSL'   # Consumer Price Index, SA monthly since 1947
        'CPILFESL'   # CPI core, SA monthly since 1957
                             #     core excludes food and energy.
        'PCEPI'      # Personal Consumption Expenditure, SA monthly
        'PCEPILFE'   # PCE core, SA monthly
        'm4infl'     # synthetic inflation, see getinflations().
        'm4inflbei'  # synthetic inflation averaged with BEI, see getfred.

        'TB3MS'      # Treasury bills, monthly
        'm4zero10'   # Zero-coupon price of Treasury 10-y, monthly
        'GS10'       # Treasury 10-y constant, monthly
        'FII10'      # TIPS 10-y constant, monthly
        'm4bei'      # 10_y Break-even inflation, getfred synthetic

        'TWEXBPA'    # Real trade-weighted USD index: Broad, monthly
        'm4xau'      # London Gold PM fix, synthetic monthly for getfred
        'm4xaueur'   # Gold euro-denominated, synthetic monthly
        'm4xaujpy'   # Gold  yen-denominated,           monthly
        'm4xaurtb'   # Real trade-weighted Gold index, synthetic monthly

        'm4usdjpy'   # USDJPY monthly, getfred synthetic
        'm4eurusd'   # EURUSD, DEM FRF synthetic 1971-2002, getfred monthly
        'm4eurjpy'   # EURJPY monthly, getfred synthetic back to 1971

        'AMBSL'      # U.S. Adjusted Monetary Base in billions, SA monthly

        'm4spx'      # S&P 500 index a.k.a. SPX, synthetic monthly for getfred
        'm4spxrtb'   # Real trade-weighted SPX index, synthetic monthly

        'm4oil'      # Oil av. Brent and WTI, synthetic monthly

        #QUARTERLY fredcode:
        'GDP'        # U.S. GDP in billions, SA quarterly
        'GDPC1'      # U.S. real GDP in 2009 billions, SA quarterly
        'GFDEBTN'    # U.S. Federal debt in millions, NSA quarterly

        'q4spx'      # S&P 500 index, synthetic quarterly for getfred
        
        #EUROZONE fredcode:
        'EUNGDP'           # EU GDP in million euros, Eurostat SA quarterly
        'm4gdpeur'         # EU GDP in real billions, synthetic SA monthly
        'm4infleu'         # EU Consumer Prices, synthetic Eurostat monthly
        'm4defleu'         # EU deflator, synthetic monthly

        'LRHUTTTTEZM156S'  # EU Unemployment rate, OECD SA monthly
        'LRHUTTTTFRM156S'  # FR Unemployment rate, OECD SA monthly 

##################################################

#Code#############################################
from urllib.request import urlopen
from datetime import datetime, timedelta, date
import static_frame as sf
import yfinance as yf
import pandas as pd
class StaticFrame(sf.Frame):
    @classmethod
    def from_fred(cls, fredcode):
        url = 'http://research.stlouisfed.org/fred2/series/'
        url += fredcode + '/downloaddata/' + fredcode + '.csv'
        fredcsv = urlopen(url)
        #data = cls.from_csv(fredcsv) #why doesn't this work?
        data = cls.from_pandas(pd.read_csv(fredcsv))
        
        data = data.rename(fredcode)
        data.symbol = fredcode
        return data

    @classmethod
    def from_symbol(cls, symbol, start=None, end=None, interval='1d', period=None, silent=True):
        #self.ticker = yf.Ticker(symbol)
        data = cls.from_pandas(yf.download(
            tickers = symbol,
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
        data = data.rename(symbol)
        data.symbol = symbol
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
