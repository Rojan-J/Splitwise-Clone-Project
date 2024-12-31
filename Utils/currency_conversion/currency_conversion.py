import requests
import sqlite3
from datetime import datetime


API="037306f9ecd64a4fa2d900d558c17b4f"
URL = "https://openexchangerates.org/api/"

#fetch real-time exchange data
def exchange_rate(base_currency="IRR"):  
    #send the request
    response=requests.get(f"{URL}?app_id={API}")
    data=response.json()
    
    if response.status_code!=200:  #200 is the success code
        raise Exception(f"Error in fetching exchange rates: {data.get('error', 'Unknown error')}")
    
    rates=data["rates"]
    USD_to_IRR=rates.get("IRR", None)
    
    
    #convert all exchange rates to be based on IRR
    IRR_based={currency:rate/USD_to_IRR for currency , rate in rates.items()}
    IRR_based["IRR"]=1.0
    
    return IRR_based