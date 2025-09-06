import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financeDataPlatform.settings')
import django
django.setup()

from stocks.mainApp import app 
from stocks.mainApp import finnhub_client
from datetime import datetime
from stocks.models import StockQuote
import os
import json


finhubbClient=finnhub_client

def getstockSymbols(exchange="US"):
    """
    gets the stock exchange symbols list of exchange country
    """
    try:
        exchange=exchange.upper()
        symbols=finhubbClient.stock_symbols(exchange=exchange)
        
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
        
def getstockQuote(symbol):
    """
    get realtime quote of a stock
    use websocket for streaming data 
    """
    quote=finhubbClient.quote(symbol)

    # insert data to db
    stockquote={
    "current_price":quote["c"],
    "change_price":quote.get("d",0),
    "change_percent":quote.get("dp",0),
    "high_price_day":quote.get("h",0),
    "low_price_day":quote.get("l",0),
    "open_price_day":quote.get("o",0),
    "previous_close":quote.get("pc",0),
    "stocktime":datetime.fromtimestamp(quote.get("t",0)),
    "stock_symbol":symbol
    }
    existingstockData=StockQuote.objects.update_or_create(stock_symbol=symbol,defaults=stockquote)
    # it is giving timely basis stock of curretn day so no need to save show based on hit
    return quote

    
if __name__=="__main__":
    # details=getCompanyBasicFinances(symbol="AAPL",metric='52WeekHigh')
    
    quote=getstockQuote("IBM")
    print("quote:", quote)