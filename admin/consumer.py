import pika

params = pika.URLParameters('amqp://admin:mypass@rabbit:5672/')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def callback(channel, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
