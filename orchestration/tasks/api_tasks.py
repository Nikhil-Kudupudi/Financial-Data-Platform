from prefect import  task
from stocks.apis.alphaVantageApis import getpastStockData
from stocks.apis.finhubbApis import getstockSymbols,getstockQuote

# @task
# def getSymbols():
    


@task
def update_paststock_data():
    getpastStockData("AAPL")

@task 
def get_currentStockData():
    getstockQuote("AAPL")

    
