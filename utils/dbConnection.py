from django.db import connection
import os

def createTable(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return 

def insertData(query,records):
    with connection.cursor() as cursor:
        cursor.execute_many(query,records)
        return 