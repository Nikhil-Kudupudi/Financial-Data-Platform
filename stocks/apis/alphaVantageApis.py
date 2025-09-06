import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financeDataPlatform.settings')
import django
django.setup()
from django.db import connection
from utils.envKeys import ALPHAVANTAGE_API_KEY,ALPHAVANTAGE_BASE_URL
import json
import requests
from datetime import datetime
from stocks.models import HistoricalStockQuote

def getStockData(stockSymbol="IBM"):
    try:
        url= f"{ALPHAVANTAGE_BASE_URL}/query"
        params={
            "function": "TIME_SERIES_INTRADAY",
            "interval": "60min",
            "outputsize": "compact",
            "symbol": stockSymbol,
            "apikey":ALPHAVANTAGE_API_KEY
        }
        response= requests.get(url,params)
        return response.json()

    except Exception as e:
        raise Exception(e)

# TIMESERIES_DAILY data of a stock
def getpastStockData(symbol,outputsize="full"):
    url= f"{ALPHAVANTAGE_BASE_URL}/query"
    params={
        "function": "TIME_SERIES_DAILY",
        "symbol":symbol,
        "apikey":ALPHAVANTAGE_API_KEY,
        "outputsize":outputsize
    }
    if HistoricalStockQuote.objects.filter(stock_symbol=symbol).exists():
            outputsize="compact"
            date=getlatestdate(symbol)
            if date:
                latestdate=date.date()
    response=requests.get(url,params)
    # with open("stockdata.json","w") as file:
    #     json.dump(response.json(),file)
    if response:
        data=response.json()
        pastdata=data.get("Time Series (Daily)")
        alldata=[]
        filtereddays=pastdata
        
        if latestdate:
            filtereddays=[daydata for daydata in pastdata if latestdate < datetime.strptime(daydata,"%Y-%m-%d").date() ]
        for day in filtereddays:
            eachday=(
                symbol,
                pastdata[day]['1. open'],
                pastdata[day]['2. high'],
                pastdata[day]['3. low'],
                pastdata[day]['4. close'],
                pastdata[day]['5. volume'],
                datetime.strptime(day,"%Y-%m-%d"),
            )
            alldata.append(eachday)

            
        with connection.cursor() as cursor:
            cursor.executemany("""INSERT INTO historicalstockquote ("stock_symbol", "open_price_day", "high_price_day", "low_price_day", "close_price_day", "volume", "trade_date", created_at)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, NOW()) """,alldata)
        
    print(f"insert of past data of {symbol}successful",filtereddays)
    

    # map data

def getYesterdayStockQuote(symbol):
    url=f"{ALPHAVANTAGE_BASE_URL}/query"
    params={
        "function": "GLOBAL_QUOTE",
        "symbol":symbol,
        "apikey":ALPHAVANTAGE_API_KEY,
    }
    response=requests.get(url,params)
    print(response.json())

def getlatestdate(symbol):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT MAX(trade_date) from historicalstockquote 
                       where stock_symbol = '{symbol}' 
                       """)
        latesttradedate=cursor.fetchone()
    return latesttradedate[0]
        

if __name__=="__main__":
    # data=getStockData("AAPL")
    # print("Stock data for 5 min interval")
    # print(data)
    # print("retreiving ful json of AAPL")
    pastdata=getpastStockData("IBM")
    # getYesterdayStockQuote("AAPL")
    