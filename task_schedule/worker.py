import pika
import time


def callback(ch, method, properties, body):
    print(' [x] Received {}'.format(body))
    time.sleep(body.count(b'.'))
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


queueName = 'hello'

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create channel
channel = connection.channel()
# create queue
channel.queue_declare(queue=queueName, durable=True)
print(' [x] Waiting for message. To exit press CTRL+C')
# use qos protocol with prefetch 1 setting
# that worker will accept the queue when the processing already completed
channel.basic_qos(prefetch_count=1)
# consume message
channel.basic_consume(queue=queueName, on_message_callback=callback)
# start process
channel.start_consuming()
