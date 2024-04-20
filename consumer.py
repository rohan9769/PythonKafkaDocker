import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers=['192.168.1.214:9092'],
        auto_offset_reset = 'earliest'
    )
    for message in consumer:
        print(json.loads(message.value))
