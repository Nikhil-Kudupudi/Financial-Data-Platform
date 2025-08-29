from fastapi import FastAPI
import finnhub
from dotenv import load_dotenv
import os
load_dotenv(override=True)

FINNHUB_API_KEY=os.getenv('FINNHUB_API_KEY')

app=FastAPI()
try:
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
    print("connected to finnhub ")
except Exception as e:
    raise Exception(e)