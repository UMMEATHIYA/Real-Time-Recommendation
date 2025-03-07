from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_user_interaction(user_id, item_id):
    data = {"user_id": user_id, "item_id": item_id}
    producer.send("recommendations", value=data)
    print(f"Sent: {data}")

# Example usage
send_user_interaction(1, 101)
send_user_interaction(2, 202)
