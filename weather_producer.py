import pandas as pd
import random
import time
from kafka import KafkaProducer
import json

# Load CSV
df = pd.read_csv("data/weather.csv")

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='10.20.144.28:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Infinite loop to send random rows
try:
    while True:
        row = df.sample(1).to_dict(orient="records")[0]
        producer.send('weather-data', row)
        print("Sent:", row)
        time.sleep(random.uniform(1, 3))  # sleep 1 to 3 seconds randomly
except KeyboardInterrupt:
    print("Stopped.")