from dotenv import load_dotenv
import os 
load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
ALPHAVANTAGE_API_KEY= os.getenv('ALPHAVANTAGE_API_KEY')
ALPHAVANTAGE_BASE_URL= os.getenv('ALPHAVANTAGE_BASE_URL')