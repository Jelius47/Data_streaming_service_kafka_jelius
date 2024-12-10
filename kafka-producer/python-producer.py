# Basic imports
import json
import random
import schedule
import time
from json import dumps
from faker import Faker
from kafka import KafkaProducer


kafka_nodes= "kafka:9092"
my_topic = "weather"

# Data generation function
def generate_data():
    faker = Faker()
    producer = KafkaProducer(bootstrap_servers=kafka_nodes,value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    my_data = {'city':faker.city(),'temperature':random.uniform(10.0,110.0)}
    producer.send(topic=my_topic,value=my_data)

    producer.flush()

if __name__== "__main__":
    generate_data()
    schedule.every(10).seconds.do(generate_data)
    while True:
        schedule.run_pending()
        time.sleep(0.5)
