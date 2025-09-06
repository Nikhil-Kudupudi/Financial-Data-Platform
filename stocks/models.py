from django.db import models

# Create your models here.

class StockQuote(models.Model):
    current_price = models.FloatField()
    change_price = models.FloatField()
    change_percent = models.FloatField()
    high_price_day = models.FloatField()
    low_price_day = models.FloatField()
    open_price_day = models.FloatField()
    previous_close = models.FloatField()
    stocktime = models.DateTimeField(default=models.functions.Now, null=True, blank=True)
    stock_symbol= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'stockquote'

class HistoricalStockQuote(models.Model):
    stock_symbol = models.CharField(max_length=100)
    high_price_day = models.FloatField()
    low_price_day = models.FloatField()
    open_price_day = models.FloatField()
    close_price_day= models.FloatField()
    volume= models.FloatField()
    trade_date= models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'historicalstockquote'