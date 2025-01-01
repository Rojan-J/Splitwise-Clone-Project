import requests
import sqlite3
from datetime import datetime


API="037306f9ecd64a4fa2d900d558c17b4f"
URL = "https://openexchangerates.org/api/"

def get_historical_rate(date):
    history_URL=f"{URL}historical/{date}.json"
    response=requests.get(history_URL,params={"app_id":API})
    data=response.json()
    
    if response.status_code!=200:
        raise Exception(f"Failed to fetch rates for {date}: {data}")
    
    rates=data.get("rates",{})
    USD_to_IRR=rates.get("IRR")
    
    return USD_to_IRR


def convert_currency(amount, date=None, from_c="USD", to_c="IRR"):
    
    target_date=date or datetime.now().strftime("%Y-%m-%d")
    
    USD_to_IRR=get_historical_rate(target_date)

    if from_c=="USD" and to_c=="IRR":
        return amount*USD_to_IRR
    
    else: #if same currency is added, no exchange needed
        return amount
    
    


# #fetch real-time exchange data
# def exchange_rate(base_currency="IRR"):  
#     #send the request
#     response=requests.get(f"{URL}?app_id={API}")
#     data=response.json()
    
#     if response.status_code!=200:  #200 is the success code
#         raise Exception(f"Error in fetching exchange rates: {data.get('error', 'Unknown error')}")
    
#     rates=data["rates"]
#     USD_to_IRR=rates.get("IRR", None)
    
    
#     #convert all exchange rates to be based on IRR
#     IRR_based={currency:rate/USD_to_IRR for currency , rate in rates.items()}
#     IRR_based["IRR"]=1.0
    
#     return IRR_based


#examples to check if it does work
result_1 = convert_currency(100, date="2022-09-22", from_c="USD", to_c="IRR")
print(f"100 USD to IRR on 2022-09-22: {result_1}")

result_2 = convert_currency(200, from_c="USD", to_c="IRR")
print(f"200 USD to IRR today: {result_2}")
