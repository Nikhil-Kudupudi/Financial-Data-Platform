from utils.envKeys import ALPHAVANTAGE_API_KEY,ALPHAVANTAGE_BASE_URL
import requests

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
    

if __name__=="__main__":
    data=getStockData("AAPL")
    print("Stock data for 5 min interval")
    print(data)