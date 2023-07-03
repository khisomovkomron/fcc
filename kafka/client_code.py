from kafka.kafka import consumer, producer
from confluent_kafka import KafkaException


# basic poll loop
running = True
def basic_consume_loop(consumer, topics):

    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)

            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                    
            elif msg.error():
                raise KafkaException(msg.error())
            else:
                msg_process(msg)
            
    
    finally:
        consumer.close()

def shutdown():
    running = False
