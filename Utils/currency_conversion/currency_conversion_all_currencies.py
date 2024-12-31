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
    
    return rates

def convert_to_IRR(amount,date=None, from_c=None):
    
    target_date=date or datetime.now().strftime("%Y-%m-%d")
    rates = get_historical_rate(target_date)
    
    from_to_USD = rates.get(from_c)
    USD_to_IRR = rates.get("IRR")
    
    converted_amount = (amount / from_to_USD) * USD_to_IRR
    return converted_amount
    
    
#EXAMPLES TO CHECK IF IT DES WORK    
amount_in_IRR = convert_to_IRR(100, date="2022-09-22", from_c="EUR")
print(f"100 EUR to IRR on 2022-09-22: {amount_in_IRR}")