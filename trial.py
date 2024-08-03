import os 
from dotenv import load_dotenv 

load_dotenv()

from coinbase.wallet.client import Client
client = Client(os.getenv('api_key'), os.getenv('api_secret'))

price = client.get_buy_price(currency_pair = 'BTC-USD')
print(price)


