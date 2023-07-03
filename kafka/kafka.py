from confluent_kafka import Producer, Consumer


# KAFKA PRODUCER
producer_config = {
    'bootstrap.server': 'localhost:9082',
    'client.id': 'my_producer'
}

producer = Producer(producer_config)

topic = 'my_topic'
message = 'Hello, Kafka'


# asynchronous writes

producer.produce(topic, key='key', value='value')

def acked(err, msg):
    if err is not None:
        print(f'Failed to deliver message: {msg, err}')
    else:
        print(f'Message produced: {msg}')

producer.produce(topic, key='key', value='value', callback=acked)

# synchronous write 


producer.produce(topic, value=message)
producer.flush() #flush() should be called prior to shutting down the producer to ensure all outstanding/queued/in-flight messages are delivered.

# KAFKA CONSUMER 

conf = {'bootstrap.servers': 'host1:9092, host2:9092',
       'group.id': 'foo',
       'auto.offset.reset': 'smallest',
       'enabl.auto.commit': False}

consumer = Consumer(conf)


