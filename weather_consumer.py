from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'weather-data',
    bootstrap_servers='**.**.***.**:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    weather_data = message.value
    print("Received:", weather_data)