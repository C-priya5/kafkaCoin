import sys
from kafka import KafkaConsumer
import json

if len(sys.argv) != 2:
    print("Usage: python consumer.py <group_id>")
    sys.exit(1)

group_id = sys.argv[1]

consumer = KafkaConsumer(
    'coinbase', 'sell','buy',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=group_id,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    print(f"[{group_id}] Received: {data}")

consumer.close()