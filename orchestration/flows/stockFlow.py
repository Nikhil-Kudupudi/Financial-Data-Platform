from prefect import flow 
from orchestration.tasks.api_tasks import update_paststock_data,get_currentStockData

@flow
def stockFlow():
    update_paststock_data()
    get_currentStockData()



if __name__ == "__main__":
    stockFlow.serve(name="test deploymenty")