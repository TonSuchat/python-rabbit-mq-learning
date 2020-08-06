import pika

exchangeName = 'logs'

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create exchange
channel.exchange_declare(exchange=exchangeName, exchange_type='fanout')
# create a queue
result = channel.queue_declare(queue='', exclusive=True)
queueName = result.method.queue
channel.queue_bind(exchange=exchangeName, queue=queueName)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(' [x] {}'.format(body))


# create consume
channel.basic_consume(
    queue=queueName, on_message_callback=callback, auto_ack=True)

# start consume
channel.start_consuming()
