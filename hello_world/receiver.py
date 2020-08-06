import pika


def callback(ch, method, properties, body):
    print(' [x] Received %r' % body)


queueName = 'hello'

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create queue
channel.queue_declare(queue=queueName)
# consume message
channel.basic_consume(queue=queueName, auto_ack=True,
                      on_message_callback=callback)
print(' [x] Waiting for message. To exit press CTRL+C')
# start process
channel.start_consuming()
