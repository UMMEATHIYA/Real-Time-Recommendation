from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "recommendations",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

for message in consumer:
    data = message.value
    print(f"Received: {data}")
