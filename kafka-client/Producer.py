import time
from confluent_kafka import Producer
import os

test_name = os.getenv("TEST_NAME", "test1")
bootstrap = os.getenv("BOOTSTRAP_SERVER", "localhost:9092")
topic = os.getenv("TOPIC", "not_set")
delay = int(os.getenv("DELAY", 1))
expected_messages = os.getenv("EXPECTED_MESSAGES", 10000)

def produce(bootstrap, topic, msg_num, delay=0.01):
    topic = topic
    print("creating new producer, will produce ",msg_num)
    print("warm up a few seconds")
    time.sleep(10)
    p = Producer({
            'bootstrap.servers': bootstrap,
            'broker.version.fallback': '0.10.0.0',
            'acks': 'all',
            'api.version.fallback.ms': 0,
#            'message.timeout.ms': 60000,
            'max.in.flight.requests.per.connection': 1,
#            'delivery.timeout.ms': 30000,
            #'debug': 'msg',
            'enable.idempotence': 'true',
            'retries': 5
    })

    def acked(err, msg):
        """Delivery report callback called (from flush()) on successful or failed delivery of the message."""
        if err is not None:
           print("failed to deliver message: {}".format(err.str()))

            
    i = 0
    while True:
        i += 1
        msg = f"source-cluster:{bootstrap} msg n:{i}"
        p.produce(topic, value=(msg), on_delivery=acked)
        if i % 10 == 0:
            p.flush(10)
            print(f"Wrote total of {i} messages to {bootstrap}")
        time.sleep(delay)
        if i==int(msg_num):
            print(f"Produced Total: {msg_num} to {bootstrap}")
            break

if __name__ == '__main__':
    produce(bootstrap, topic, expected_messages,delay)



