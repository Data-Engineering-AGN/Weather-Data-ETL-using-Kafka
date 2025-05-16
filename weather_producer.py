import pandas as pd
import random
import time
from kafka import KafkaProducer
import json

# Load CSV
df = pd.read_csv("data/weather.csv")  # or use the uploaded file path if running locally

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='**.**.****.**:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Infinite loop to send random rows to country-specific topics
try:
    while True:
        row = df.sample(1).to_dict(orient="records")[0]
        country = row.get("Country", "unknown").lower().replace(" ", "_")
        topic = f"{country}_weather"
        producer.send(topic, row)
        print(f"Sent to [{topic}]:", row)
        time.sleep(random.uniform(1, 3))
except KeyboardInterrupt:
    print("Stopped.")