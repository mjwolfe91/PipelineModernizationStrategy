from kafka import KafkaProducer
import json
from datetime import datetime
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

messages = [
    {
        "customer_id": 'abc1',
        "activity": 'click1',
        "timestamp": datetime.now()
    },
    {
        "customer_id": 'abc2',
        "activity": 'click1',
        "timestamp": datetime.now()
    },
    {
        "customer_id": 'abc1',
        "activity": 'click2',
        "timestamp": datetime.now()
    },
    {
        "customer_id": 'abc2',
        "activity": 'exit',
        "timestamp": datetime.now()
    },
    {
        "customer_id": 'abc1',
        "activity": 'exit',
        "timestamp": datetime.now()
    },
]

for message in messages:
    msg = json.dumps(message, default=str)
    producer.send('web_traffic', value=msg)
    print("Sent:", msg)
    time.sleep(5)
