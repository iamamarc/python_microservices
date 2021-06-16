import pika

# params = pika.URLParameters('amqps://ykmmxszr:tKJFn5bgPC3lfOZrHEgI0SJXf6-HLTCU@snake.rmq2.cloudamqp.com/ykmmxszr')
# params = pika.URLParameters('amqp://ykmmxszr:tKJFn5bgPC3lfOZrHEgI0SJXf6-HLTCU@snake.rmq2.cloudamqp.com/ykmmxszr')
# connection = pika.BlockingConnection(params)
params = pika.URLParameters('amqp://admin:mypass@rabbit:5672/')
connection = pika.BlockingConnection(params)
channel = connection.channel()

# channel.queue_declare(queue='admin')


def publish():
    channel.basic_publish(exchange='', routing_key='main',body='Hello Main')


