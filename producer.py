import time
import json
import random
from datetime import datetime
from datagenerator import generate_message
from kafka import KafkaProducer

#Message will be serialized as Json
def serializer(message):
    return json.dumps(message).encode('utf-8')

#kafka producer
producer = KafkaProducer(
    bootstrap_servers=['192.168.1.214:9092'],
    value_serializer = serializer
)

if __name__ == '__main__':
    while True:
        dummy_message = generate_message()
        print(f'Producing message @ {datetime.now()} | Message @ {str(dummy_message)}')
        producer.send('messages',dummy_message)

        time_to_sleep = random.randint(1,11)
        time.sleep(time_to_sleep)
