import requests
import sqlite3
from datetime import datetime

API="037306f9ecd64a4fa2d900d558c17b4f"
URL = "https://openexchangerates.org/api/"

#2526dd8667b954d9305f593f2e7508e836445d7b


def get_historical_rate(date):
    print(f"Fetching historical rates for {date}...")
    history_URL=f"{URL}historical/{date}.json"
    response=requests.get(history_URL,params={"app_id":API})
    data=response.json()
    
    if response.status_code!=200:
        raise Exception(f"Failed to fetch rates for {date}: {data}")
    
    rates=data.get("rates",{})
    
    return rates

def convert_to_IRR(amount,date=None, from_c=None):
    
    try:
        target_date = date or datetime.now().strftime("%Y-%m-%d")
        print(f"Converting {amount} {from_c} to IRR on {target_date}...")
        rates = get_historical_rate(target_date)

        from_to_USD = rates.get(from_c)
        USD_to_IRR = rates.get("IRR")

        if from_to_USD is None or USD_to_IRR is None:
            raise ValueError(f"Currency rates not available for {from_c} or IRR on {target_date}.")

        converted_amount = (amount / from_to_USD) * USD_to_IRR
        print(f"Converted amount: {converted_amount} IRR.")
        return converted_amount
    except Exception as e:
        raise ValueError(f"Error in currency conversion: {e}")
    
    
