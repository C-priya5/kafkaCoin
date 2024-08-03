import os 
from dotenv import load_dotenv 
import requests
load_dotenv()

res=requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell')
# from coinbase.wallet.client import Client
# client = Client(os.getenv('api_key'), os.getenv('api_secret'))

# price = client.get_buy_price(currency_pair = 'BTC-USD')
# print(price)

print(res.json())
