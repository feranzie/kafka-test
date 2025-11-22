from confluent_kafka import Consumer

import json

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    #group id identifies a group of consumers that are instances of the same application
    'group.id': 'order-tracker',
    #tells kafka what to do when it cant see last messaege consumed by this consumer
    'auto.offset.reset': 'earliest' #start reading at the beginning of the topic if no committed offsets exist
    }



Consumer = Consumer(consumer_config)

#subscribe to the topic orders
consumer.subscribe(['orders'])


print ("consumer is running and subscribed to orders")


# while True:
#     msg= consumeer.poll(1.0) #timeout of 1 second
#     if msg is None:
#         print(" X Error :",msg.error())
#         continue

#     value=msg.value().decode('utf-8')
#     json.loads(value)
#     print(f"📦 Received order: {order['quantity']} x {order['item']} from {order['user']}")


try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        order = json.loads(value)
        print(f"📦 Received order: {order['quantity']} x {order['item']} from {order['user']}")
except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.close()
