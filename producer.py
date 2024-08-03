import requests
from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'

def fetch_coinbase_data():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

while True:
    data = fetch_coinbase_data()
    if data:
        producer.send('coinbase', data)
        print(f"Sent: {data}")
    time.sleep(10)  # Adjust the frequency as needed

producer.close()



