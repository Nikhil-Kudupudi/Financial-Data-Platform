from stocks.mainApp import app 
from stocks.mainApp import finnhub_client
import json 
finhubbClient=finnhub_client

def getstockSymbols(exchange="US"):
    """
    gets the stock exchange symbols list of exchange country
    """
    try:
        exchange=exchange.upper()
        symbols=finhubbClient.stock_symbols(exchange=exchange)
        print(symbols)
    except Exception as e:
        raise Exception(e)
    
def getCompanyBasicFinances(symbol,metric="all"):
    """
    Get company basic financials such as margin, P/E ratio, 52-week high/low etc.
    Arguments:
        symbol (REQUIRED)
        Symbol of the company: AAPL.

        metric (REQUIRED)
        Metric type. Can be 1 of the following values all
    """
    try:
        basicFinances=finhubbClient.company_basic_financials(symbol,metric)
        with open("basicFinancen.json","w") as file:
            json.dump(basicFinances,file)

        return basicFinances
    except Exception as e:
        raise Exception(e)
        

    
if __name__=="__main__":
    details=getCompanyBasicFinances(symbol="AAPL",metric='52WeekHigh')
    print("basic details of {} ".format("AAPL"))
    # print("printing stock symbols of US Exchange")
    # getstockSymbols("US")
    # print("printing stock symbols of INDIA Exchange")
    # getstockSymbols("NS")