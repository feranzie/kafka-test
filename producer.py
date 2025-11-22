from connfluent_kafka import Producer
import json
import uuid
#boot strap refers to kafka using the adres to discover all brokers, odes, servers at the address


producer_config = {
    'bootstrap.servers': 'localhost:9092'
    }
producer = Producer(producer_config)

def delivery_report(err, msg):
    if err :
        print(f"Message delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode("utf-8")}")
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

order =(
    "order_id" : str(uuid.uuid4()),
    "user":"nana",
    "item" : "pizza",
    "quantity": 5 )

#turn json to str then bytes
value=json.dumps(order).encode('utf-8')

#creates topic called orders and sends the value
producer.produce(
    topic='orders', 
    value=value
    ##track whether message was successfully delivered or not
    callback=delivery_report
    )

#forces all messages in the producer queue to be delivered
producer.flush()

